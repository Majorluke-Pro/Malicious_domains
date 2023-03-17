import argparse
import requests
import tldextract

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

def check_domain_availability(domain):
    try:
        response = requests.get('http://' + domain)
        if response.status_code < 400:
            return True
        else:
            return False
    except:
        return False

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('domain', help='The domain name to check')
    args = parser.parse_args()

    variations = generate_domain_variations(args.domain)
    for variation in variations:
        if check_domain_availability(variation):
            print(variation + ' is live')
        else:
            print(variation + ' is available')

if __name__ == '__main__':
    main()
