# Challenge: Simulate a shopping cart — store a price and quantity as variables, calculate the total, and print it formatted nicely.

from decimal import Decimal

print()

price = 4.99
quantity = 11

total = price * quantity

total_decimal = (Decimal(str(total))).quantize(Decimal('0.00'))

print("Thank you for shopping with us!")
print()

print("--------- Order Summary ---------")
print()
print(f"Price: ${price}")
print(f"Quantity: {quantity}")
print()

# Using round() method - okay, but the other ways are better
print(f"Total (UsingRound Method): ${round(total, 2)}")

# Using string formatting method - this is the most preferred way to format nicely
print(f"Total (Using String Formatting): ${total:.2f}")

# Using Decimal method - this is heavy artillery (only use for banking apps)
print(f"Total (Using Decimal Method): ${total_decimal}")

print()
print("--------------- End -------------")

