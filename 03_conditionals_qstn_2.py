# 2. Simulate a login check — given an email and password variable, validate that neither is empty, the email contains "@", and the password is at least 8 characters. Print the appropriate message for each failure case and "Login successful" if everything passes.

email = "johndoe@example.co"
password = "abc12345"

if not email:
    print("Email is empty. Write the correct email address")
elif "@" not in email:
    print("Invalid email format.Please write it correctly")
elif not password:
    print("Password is empty. Write the correct password")
elif len(password) < 8:
    print("Password is less than 8 characters")
else:
    print("Login successful")


