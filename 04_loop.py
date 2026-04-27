# Python Loops
# [for loops ✅, while loops ✅, break ✅, continue ✅, range() ✅, nested loops — how to repeat actions]


# continue

programs = ["PCM", "HGE", "EGM", "HKL", "PGM"]

for program in programs:
    if program == "HGE" or program == "HKL":
        continue
    print(f"{program} holders can join Computer Science")