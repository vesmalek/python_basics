# Enumerate in Python Loops

gadgets = ["Laptop", "Magic Mouse", "Keyboard", "Apple Pencil"]


for index, gadget in enumerate(gadgets):
    if gadget == "Keyboard":
        continue
    print(f"{index + 1}. {gadget}")