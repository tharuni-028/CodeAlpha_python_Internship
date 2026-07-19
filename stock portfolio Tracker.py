print("=" * 20)
print("STOCK PORTFOLIO")
print("=" * 20)

stock_prices = {
    "apple": 180,
    "tesla": 250,
    "google": 150,
    "microsoft": 300,
    "amazon": 200
}

total_value = 0

print("\nAvailable Stocks:")
for stock in stock_prices:
    print(stock.title(), ":", "₹", stock_prices[stock])

while True:

    stock_name = input("\nEnter Stock Name: ").lower()

    if stock_name not in stock_prices:
        print("❌ Stock Not Available!")
        continue

    quantity = int(input("Enter Quantity: "))

    price = stock_prices[stock_name]

    stock_value = price * quantity

    total_value = total_value + stock_value

    print("\n" + "-" * 20)
    print("Stock Name :", stock_name.title())
    print("Price      : ₹", price)
    print("Quantity   :", quantity)
    print("Value      : ₹", stock_value)
    print("-" * 20)

    choice = input("Add Another Stock? (yes/no): ").lower()

    if choice == "no":
        break

print("\n" + "=" * 20)
print("PORTFOLIO SUMMARY")
print("=" * 20)

print("Total Portfolio Value : ₹", total_value)

if total_value >= 3000:
    print("Portfolio Status : Excellent")

elif total_value >= 2000:
    print("Portfolio Status : Very Good")

elif total_value >= 1000:
    print("Portfolio Status : Good")

else:
    print("Portfolio Status : Beginner")

print("=" * 20)
print("THANK YOU")
print("=" * 20)