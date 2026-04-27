# Challenge 01: You have a list of cart items with names and prices. Loop through and print each item with its price formatted to 2 decimal places, then print the total at the end.

cart_items = {
    "tomato": 12.99,
    "onion": 5.57,
    "oranges": 10.88,
    "butter": 37.99,
    "wrapping papers": 1.60,
    "ketchup": 2.50
}

total = 0
for key, value in cart_items.items():
    total += value
    print(f"{key}: {value:.2f}")

print(f"Total: {total:.2f}")
