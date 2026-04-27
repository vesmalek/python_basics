# Simulate a login system — give the user 3 attempts using a while loop. Each iteration check if the password matches "python123". If it does, print "Login successful" and stop. If all 3 attempts fail, print "Account locked".

attempts = 0

while attempts < 3:
    password = input("Enter user password: ")
    attempts += 1
    if password == "python123":
        print("Login successful")
        break
    else:
        print(f"Wrong password, {3 - attempts} tries left.")
else:
    print("Account locked")