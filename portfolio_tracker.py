import os

def load_stock_prices():
    """
    Hardcoded dictionary defining current stock prices.
    These are the baseline numbers used to calculate your investment.
    """
    return {
        "AAPL": 180.00,
        "TSLA": 250.00,
        "GOOGL": 175.00,
        "AMZN": 185.00,
        "MSFT": 420.00
    }

def display_available_stocks(prices):
    print("\n--- Available Stocks & Prices ---")
    for symbol, price in prices.items():
        print(f"{symbol}: ${price:.2f}")
    print("---------------------------------")

def save_portfolio_to_file(portfolio, total_val, filename="portfolio_summary.txt"):
    try:
        with open(filename, "w") as file:
            file.write("=== CODEALPHA STOCK PORTFOLIO SUMMARY ===\n\n")
            file.write(f"{'Stock':<10}{'Quantity':<10}{'Price':<12}{'Total Value':<12}\n")
            file.write("-" * 45 + "\n")
            
            for symbol, details in portfolio.items():
                file.write(
                    f"{symbol:<10}"
                    f"{details['quantity']:<10}"
                    f"${details['price']:<11.2f}"
                    f"${details['total_value']:<11.2f}\n"
                )
            
            file.write("-" * 45 + "\n")
            file.write(f"Total Portfolio Investment: ${total_val:.2f}\n")
        print(f"\n💾 Portfolio successfully saved to '{filename}'!")
    except IOError:
        print("\n❌ Error: Could not save portfolio to file.")

def main():
    stock_prices = load_stock_prices()
    portfolio = {}
    total_portfolio_value = 0.0

    print("Welcome to the CodeAlpha Stock Portfolio Tracker!")
    display_available_stocks(stock_prices)

    while True:
        # Get stock symbol input from the user
        symbol = input("\nEnter the stock symbol you own (or type 'done' to calculate): ").upper().strip()
        
        if symbol == "DONE":
            break
            
        if symbol not in stock_prices:
            print("❌ Invalid stock symbol. Please choose from the available list (AAPL, TSLA, GOOGL, AMZN, MSFT).")
            continue

        # Get quantity input with basic input validation
        try:
            quantity = int(input(f"Enter the quantity of shares for {symbol}: "))
            if quantity <= 0:
                print("❌ Quantity must be greater than 0.")
                continue
        except ValueError:
            print("❌ Invalid quantity. Please enter a valid whole number.")
            continue

        # Add tracking data to our portfolio dictionary
        price = stock_prices[symbol]
        if symbol in portfolio:
            portfolio[symbol]['quantity'] += quantity
            portfolio[symbol]['total_value'] = portfolio[symbol]['quantity'] * price
        else:
            portfolio[symbol] = {
                "quantity": quantity,
                "price": price,
                "total_value": quantity * price
            }
        print(f"✅ Added {quantity} shares of {symbol} to your tracker.")

    # Calculate results if the user entered data
    if not portfolio:
        print("\n👋 No stocks entered. Exiting program.")
        return

    print("\n=========================================")
    print("        YOUR PORTFOLIO INVESTMENT        ")
    print("=========================================")
    print(f"{'Stock':<10}{'Quantity':<10}{'Unit Price':<12}{'Total Value':<12}")
    print("-" * 46)

    for symbol, details in portfolio.items():
        print(
            f"{symbol:<10}"
            f"{details['quantity']:<10}"
            f"${details['price']:<11.2f}"
            f"${details['total_value']:<11.2f}"
        )
        total_portfolio_value += details['total_value']

    print("-" * 46)
    print(f"Total Portfolio Value: ${total_portfolio_value:.2f}")
    print("=========================================")

    # Ask user if they wish to save the text file
    save_choice = input("\nDo you want to save this summary to a text file? (yes/no): ").lower().strip()
    if save_choice in ['yes', 'y']:
        save_portfolio_to_file(portfolio, total_portfolio_value)
    
    print("\nThank you for using CodeAlpha Stock Portfolio Tracker!")

if __name__ == "__main__":
    main()