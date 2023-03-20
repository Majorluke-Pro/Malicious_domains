import smtplib
import whois

from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.mime.application import MIMEApplication

#email configurations
from_address = "it-notifications@uspeglobal.com"
to_address = "luke.luus@uspeglobal.com;johan.longland@uspglobal.com"
password = "Qih8#Yr66DLp5kxX*ie$"
smtp_server = "smtp.office365.com"
smtp_port = 587



# read the list of domain names from the file
with open('now_available.txt') as f:
    domains = f.read().splitlines()

# loop through the list of domain names and check their availability
for domain in domains:
    try:
        w = whois.whois(domain)
        if not w.status:
            print(f"{domain} has not been registered")
        else:
            print(f"{domain} is now registered!")
            # create the email message
            msg = MIMEMultipart()
            msg['From'] = from_address
            msg['To'] = to_address
            msg['Subject'] = f"{domain} is now registered"
            body = f"{domain} is now registered, this domain is potentially malicious."
            msg.attach(MIMEText(body, 'plain'))

            # attach the file containing the list of domains
            with open('now_available.txt', 'rb') as f:
                attachment = MIMEApplication(f.read(), _subtype='txt')
                attachment.add_header('content-disposition', 'attachment', filename='now_available.txt')
                msg.attach(attachment)

            # send the email
            server = smtplib.SMTP(smtp_server, smtp_port)
            server.starttls()
            server.login(from_address, password)
            text = msg.as_string()
            server.sendmail(from_address, to_address, text)
            server.quit()
    except:
        print(f"An error occurred while checking {domain}")









# port = 587
# smtp_server = "smtp.office365.com"
# sender_email = "smartpower-support@uspeglobal.com"
# password = "72QJ$XREci$Tf@$"
# receiver_email = "test@email.com"





#gpoikvqkgaawxtmt = Luke
