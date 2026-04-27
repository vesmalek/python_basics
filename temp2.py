# Clean the list and print only the valid prices with no extra spaces or empty entries.

prices = "  29.99, 5.50,  , 12.00, , 8.75  "

# THE LONG WAY

# 1. split the list
# 2. iterate through the list and clean one by one
# 3. check for empty items
# 4. save each item in the list

prices_list = []

for price in prices.split(","):
    cleaned = price.strip()
    if cleaned:
        prices_list.append(cleaned)

print()
print("Before Cleaning")
print(prices)

print()
print("After Cleaning")
print(prices_list)

