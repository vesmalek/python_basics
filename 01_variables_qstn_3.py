# Use type() on each of your variables to confirm what Python sees them as.

product_name = "Hibiscus Flower"
quantity = 7
price = 15.50
is_artificial = True

print()
print("Data and their types:")
print()

print(f"Price: {price}, Type: {type(price).__name__}")
print(f"Quantity: {quantity}, Type: {type(quantity).__name__}")
print(f"Product Name: {product_name}, Type: {type(product_name).__name__}")
print(f"Boolean: {is_artificial}, Type: {type(is_artificial).__name__}")

print()


