# Challenge 3: Given a list of usernames, loop through and stop the moment you find a username that starts with the letter "A" — print that username and a message saying it was found.

usernames = ["Ali", "Hamad", "Issam", "Kassim", "Arshad", "Ahmed"]

for username in usernames:
    if username.startswith("A"):
        print(f"{username} was found!")
        break
    