# roles.py

def check_role_access(role):
    # Convert to lowercase just like in your original script
    role_clean = role.lower()
    
    if role_clean == "admin":
        return "You can do everything."
    elif role_clean == "editor":
        return "You can create and edit."
    elif role_clean == "viewer":
        return "You can only read."
    else:
        return "Invalid role. Denied!"