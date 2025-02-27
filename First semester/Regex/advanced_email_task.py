import re
from collections import Counter
from datetime import datetime


def email(filename):
    with open(filename, 'r') as f:
        lines = f.readlines()

    senders = []
    receivers = []
    subjects = []
    fridays_emails = []
    urgent_important_subjects = []

    # Loop through each line (email)
    for line in lines:
        # Use regex to extract date, sender, receiver, and subject
        date_match = re.search(r'Date: ([0-9]{4}-[0-9]{2}-[0-9]{2})', line)
        sender_match = re.search(r'From: ([\w.-]+@[\w.-]+\.\w+)', line)
        receiver_match = re.search(r'To: ([\w.-]+@[\w.-]+\.\w+)', line)
        subject_match = re.search(r'Subject: (.+)', line)

        if date_match and sender_match and receiver_match and subject_match:
            # Convert date string to a datetime object to find out if it is a Friday
            date_obj = datetime.strptime(date_match.group(1), '%Y-%m-%d')
            if date_obj.weekday() == 4:  # Monday is 0 and Sunday is 6, so Friday is 4
                fridays_emails.append(line)

            # Check for 'Urgent' or 'Important' in the subject
            if 'Urgent' in subject_match.group(1) or 'Important' in subject_match.group(1):
                urgent_important_subjects.append(subject_match.group(1))

            senders.append(sender_match.group(1))
            receivers.append(receiver_match.group(1))
            subjects.append(subject_match.group(1))

    # Find most common words in subjects
    words = ' '.join(subjects).split()
    word_count = Counter(words)
    most_common_words = word_count.most_common()

    print(f"Emails sent on Fridays: {len(fridays_emails)}")
    print(f"Subjects with 'Urgent' or 'Important': {urgent_important_subjects}")
    print(f"Most common words in subjects: {most_common_words}")


email('advanced_fictional_emails.txt')