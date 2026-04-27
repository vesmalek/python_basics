# Looping through Dictionaries

car = {
    "name": "IST",
    "brand": "Toyota",
    "year": "2006",
    "country": "Japan"
}

# Looping through keys only
print()
print("Looping through keys only:")
for key in car:
    print(key)

# looping through values only
print()
print("Looping through values only:")
for value in car.values():
    print(value)

# looping through key and their values
print()
print("Looping through keys and values:")

for key, value in car.items():
    print(f"{key}: {value}")