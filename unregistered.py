import whois
import smtplib
from email.mime.text import MIMEText

# Read domain names from the unregistered_domains.txt file
with open('unregistered_domains.txt', 'r') as file:
    unregistered_domains = file.readlines()
unregistered_domains = [x.strip() for x in unregistered_domains]

# Create an empty list to store newly registered domain names
newly_registered_domains = []

# Check each domain name in the WHOIS database
for domain in unregistered_domains:
    try:
        w = whois.whois(domain)
        # Check if the domain is registered
        if w.status:
            # Add the newly registered domain to the list
            newly_registered_domains.append(domain)
    except whois.parser.PywhoisError:
        # Ignore any errors during the WHOIS lookup
        pass

# Send an email if a new domain has been registered
if newly_registered_domains:
    # Set up email parameters
    sender_email = 'luke.r.uus@gmail.com'
    recipient_email = 'luke.r.luus@gmail.com'
    subject = 'Newly registered domain name(s)'
    body = '\n'.join(newly_registered_domains)
    msg = MIMEText(body)
    msg['Subject'] = subject
    msg['From'] = sender_email
    msg['To'] = recipient_email

    # Send the email using the SMTP protocol
    with smtplib.SMTP('smtp.gmail.com', 587) as smtp:
        smtp.starttls()
        smtp.login(sender_email, 'gpoikvqkgaawxtmt')
        smtp.send_message(msg)

    print(f"An email has been sent to {recipient_email} with the newly registered domain name(s).")
else:
    print("No new domain names have been registered.")
