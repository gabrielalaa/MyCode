import re
from collections import Counter


# Read the text file
def email_regex(filename):
    with open(filename, 'r') as f:
        content = f.read()

    # Extract all unique senders' email addresses
    # Find all email addresses
    emails = re.findall(r'[a-zA-Z0-9_.+-]+@[a-zA-Z0-9_.+-]+\.[a-zA-Z0-9-.]+', content)

    # We know that the first email is the sender and the second one is the receiver
    senders = []
    receivers = []
    for i in range(0, len(emails)):
        if i % 2 == 0:
            senders.append(emails[i])
        else:
            receivers.append(emails[i])
    # print(senders)
    # print(receivers)
    list_of_unique_senders = []
    for email in senders:
        if email not in list_of_unique_senders:
            list_of_unique_senders.append(email)
    print(f"Unique senders are: {list_of_unique_senders}")

    # Count the number of emails sent from each domain
    # example.com, test.org ...
    # Create a list in which I have only domains
    domains = re.findall(r'@[a-zA-Z0-9_.+-]+\.[a-zA-Z0-9-.]+', content)
    # Count domains
    count_domains = Counter(domains)
    print(f"The number of emails sent from each domain are: {count_domains}")

    # Find all email headers where the sender and receivers have the same domain
    for i in range(0, len(domains), 2):
        if domains[i] == domains[i+1]:
            print(f"{emails[i]} and {emails[i+1]} have the same domain")


email_regex('fictional_emails.txt')