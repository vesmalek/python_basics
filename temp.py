# Clean the list and print only the valid prices with no extra spaces or empty entries.

prices = "  29.99, 5.50,  , 12.00, , 8.75  "

prices_clean = [price.strip() for price in prices.split(",") if price.strip()]

for price in prices_clean:
    print(price)


