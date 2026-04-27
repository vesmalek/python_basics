# 4. Given a cart_total variable, apply a discount: 20% off if total is above 500, 10% off if above 200, no discount otherwise. Print the final amount.

cart_total = 100
discount = 0

if cart_total > 500:
    discount = 20
elif cart_total > 200:
    discount = 10
else:
    discount = 0

print(f"You got a {discount}%. The total amount now is ${(cart_total * (1 - (discount/100))):.2f}")