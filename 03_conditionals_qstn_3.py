# 3. Given a role variable, print what the user can do — admins can do everything, editors can create and edit, viewers can only read, and anything else should be denied.

role = "Admin".lower()

if role == "admin":
    print("You can do everything.")
elif role == "editor":
    print("You can create and edit.")
elif role == "viewer":
    print("You can only read.")
else:
    print("Invalid role. Denied!")
