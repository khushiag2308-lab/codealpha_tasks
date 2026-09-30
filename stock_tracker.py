
stock_prices = {
    "AAPL": 180,
    "TSLA": 250,
    "GOOGL": 150,
    "AMZN": 190,
    "MSFT": 420
}

print("===================================")
print("      STOCK PORTFOLIO TRACKER")
print("===================================")

print("\nAvailable stocks:")
for stock in stock_prices:
    print(stock, ":", stock_prices[stock])

total = 0
portfolio = []

while True:
    stock = input("\nEnter stock name (or type 'done' to finish): ").upper()

    if stock == "DONE":
        break

    if stock not in stock_prices:
        print("Stock not available. Please choose from the list.")
        continue

    quantity = int(input("Enter quantity: "))

    price = stock_prices[stock]
    value = price * quantity

    total = total + value

    portfolio.append([stock, quantity, price, value])

print("\n===================================")
print("          PORTFOLIO DETAILS")
print("===================================")

for item in portfolio:
    print("Stock:", item[0])
    print("Quantity:", item[1])
    print("Price:", item[2])
    print("Investment:", item[3])
    print("-----------------------------------")

print("Total Investment:", total)
with open("portfolio.txt", "w") as file:
    file.write("STOCK PORTFOLIO\n")
    file.write("====================\n")

    for item in portfolio:
        file.write("Stock: " + item[0] + "\n")
        file.write("Quantity: " + str(item[1]) + "\n")
        file.write("Price: " + str(item[2]) + "\n")
        file.write("Investment: " + str(item[3]) + "\n")
        file.write("--------------------\n")

    file.write("Total Investment: " + str(total))

print("\nPortfolio has been saved in portfolio.txt")