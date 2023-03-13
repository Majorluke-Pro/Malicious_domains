# Read domain names from the known_domains.txt file
with open('known_domains.txt', 'r') as file:
    known_domains = file.readlines()
known_domains = [x.strip() for x in known_domains]

# Read domain names from the registered_domains.txt file
with open('registered_domains.txt', 'r') as file:
    registered_domains = file.readlines()
registered_domains = [x.strip() for x in registered_domains]

# Find domain names that are in the known_domains.txt file but not in the registered_domains.txt file
unregistered_domains = list(set(known_domains) - set(registered_domains))

# Print out the unregistered domain names
for domain in unregistered_domains:
    print(domain)
