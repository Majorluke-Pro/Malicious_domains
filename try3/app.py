
# This code is to check different permutations of a domain name usiing the DSNTWIST library, then write it into either a live.txt file or available.txt file

import streamlit as st
import requests
import tldextract
import argparse
import concurrent.futures

def generate_domain_variations(domain):
    subdomains = ['', 'www', 'mail', 'admin', 'blog', 'ftp', 'secure', 'm']
    tld = tldextract.extract(domain).suffix
    domain = domain.replace('.' + tld, '')

    variations = []
    for subdomain in subdomains:
        variations.append(subdomain + '.' + domain + '.' + tld)
        for i in range(1, len(domain)):
            variations.append(subdomain + '.' + domain[:i] + '.' + domain[i:] + '.' + tld)
            variations.append(subdomain + '.' + domain[:i] + '-' + domain[i:] + '.' + tld)
            variations.append(subdomain + '.' + domain[:i] + '_' + domain[i:] + '.' + tld)

    return variations

def check_domain_availability(domain, variation, live_domains_file, available_domains_file):
    try:
        response = requests.get('http://' + domain)
        if response.status_code < 400:
            st.write(variation + ' is live')
            with open(live_domains_file, 'a') as f:
                f.write(variation + '\n')
            return True
        else:
            st.write(variation + ' is available')
            with open(available_domains_file, 'a') as f:
                f.write(variation + '\n')
            return False
    except:
        st.write(variation + ' is available')
        with open(available_domains_file, 'a') as f:
            f.write(variation + '\n')
        return False


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('domain', help='The domain name to check')
    args = parser.parse_args()

    live_domains_file = open("live.txt", "w")
    available_domains_file = open("available.txt", "w")

    variations = generate_domain_variations(args.domain)

    # Use ThreadPoolExecutor to run the check_domain_availability function concurrently
    with concurrent.futures.ThreadPoolExecutor(max_workers=8) as executor:
        future_to_variation = {executor.submit(check_domain_availability, args.domain, variation, "live.txt", "available.txt"): variation for variation in variations}
        for future in concurrent.futures.as_completed(future_to_variation):
            variation = future_to_variation[future]
            try:
                result = future.result()
            except Exception as exc:
                print(f"{variation} generated an exception: {exc}")
            else:
                if result:
                    st.write(variation + ' is live')
                else:
                    st.write(variation + ' is available')

    live_domains_file.close()
    available_domains_file.close()


if __name__ == '__main__':
    main()


