# Challenge 02: You have a list of emails where some are empty and some are missing "@". Loop through, skip the invalid ones using continue, and print only the valid ones.

emails = ["john@example.com", "paulgmail.com", "", "ally@hotmail.com", "rashidyahoo.com"]

print()
print("Valid Emails:")

for email in emails:
    if not email or ("@" not in email):
        continue
    print(f"{email}")