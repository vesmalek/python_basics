# Python Loops
# [for loops ✅, while loops ✅, break, continue, range() ✅, nested loops — how to repeat actions]


# break

teams = ["Man United", "Chelsea", "Aston Villa", "Crystal Palace", "Nottingham Forest", "Liverpool", "Arsenal"]

for  team in teams:
    if team == "Liverpool":
        print(f"Found: {team}")
        break
    print(f"Checking: {team}")
