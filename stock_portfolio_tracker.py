# Hardcoded stock prices
stock_prices = {
    "AAPL": 180,
    "TSLA": 250,
    "GOOGL": 140,
    "MSFT": 330,
    "AMZN": 130
}

def get_user_input():
    portfolio = {}
    print("Welcome to the Stock Portfolio Tracker!")
    print("Available stocks and their prices:")
    for stock, price in stock_prices.items():
        print(f"{stock}: ${price}")
    print("\nYou can enter stock symbols and quantities to build your portfolio.")
    print("Type 'done' when you are finished entering stocks.\n")
    # print("Enter stock symbols and quantities (type 'done' to finish):")
    while True:
        stock = input("Stock symbol: ").upper()
        if stock == 'DONE':
            break
        if stock not in stock_prices:
            print("Stock not found in the price list. Try again.")
            continue
        try:
            quantity = int(input(f"Quantity of {stock}: "))
            if stock in portfolio:
                portfolio[stock] += quantity
            else:
                portfolio[stock] = quantity
        except ValueError:
            print("Please enter a valid number.")
    return portfolio

def calculate_total_investment(portfolio):
    total = 0
    for stock, quantity in portfolio.items():
        price = stock_prices[stock]
        total += price * quantity
    return total

def display_summary(portfolio, total):
    print("\n----- Investment Summary -----")
    for stock, quantity in portfolio.items():
        price = stock_prices[stock]
        value = price * quantity
        print(f"{stock}: {quantity} shares x ${price} = ${value}")
    print(f"Total Investment: ${total}")

def save_to_file(portfolio, total, filename="investment_summary.csv"):
    with open(filename, 'w') as f:
        f.write("Stock,Quantity,Price per Share,Total Value\n")
        for stock, quantity in portfolio.items():
            price = stock_prices[stock]
            value = price * quantity
            f.write(f"{stock},{quantity},{price},{value}\n")
        f.write(f"\nTotal Investment,,,{total}\n")
    print(f"\nSaved summary to '{filename}'")

def main():
    portfolio = get_user_input()
    if not portfolio:
        print("No stocks entered. Exiting.")
        return
    total = calculate_total_investment(portfolio)
    display_summary(portfolio, total)
    
    save = input("Would you like to save the summary to a file? (yes/no): ").lower()
    if save == 'yes':
        save_to_file(portfolio, total)

if __name__ == "__main__":
    main()
