import whois
import smtplib

# Read domain names from file
with open('known_domains.txt', 'r') as file:
    domain_names = file.readlines()
domain_names = [x.strip() for x in domain_names]

# Check if domain is registered in WHOIS database
for domain_name in domain_names:
    try:
        whois.whois(domain_name)
        # If domain is registered, send email
        sender_email = "luke.r.luus@gmail.com"  # replace with your email address
        receiver_email = "luke.r.luus@gmail.com"  # replace with recipient email address
        message = f"""\
Subject: Registered domain name

The domain name {domain_name} has been registered.

"""
        with smtplib.SMTP('smtp.gmail.com', 587) as smtp_server:
            smtp_server.starttls()
            smtp_server.login(sender_email, 'gpoikvqkgaawxtmt')  # replace with your email password
            smtp_server.sendmail(sender_email, receiver_email, message)
            print(f"Email sent for domain {domain_name}")
    except:
        # If domain is not registered, continue checking the next domain
        continue
