import os

def stock_portfolio_tracker():
    # 1. Hardcoded stock prices dictionary
    stock_prices = {
        "AAPL": 180.00,
        "TSLA": 250.00,
        "GOOGL": 140.00,
        "MSFT": 400.00,
        "AMZN": 175.00
    }

    portfolio = {}
    total_investment = 0.0

    print("==========================================")
    print("   Welcome to CodeAlpha Stock Tracker")
    print("==========================================")
    print("Available stocks and prices:")
    for stock, price in stock_prices.items():
        print(f"  - {stock}: ${price:.2f}")
    print("==========================================\n")

    # 2. Get user input for stocks and quantities
    while True:
        symbol = input("Enter stock symbol (or type 'done' to finish): ").strip().upper()
        
        if symbol == "DONE":
            break
            
        if symbol not in stock_prices:
            print(f"Error: '{symbol}' is not in the price list. Please pick from available stocks.\n")
            continue

        try:
            quantity = int(input(f"Enter quantity for {symbol}: "))
            if quantity <= 0:
                print("Quantity must be greater than 0.\n")
                continue
        except ValueError:
            print("Invalid input! Please enter a valid whole number for quantity.\n")
            continue

        # Add or update quantity in portfolio
        portfolio[symbol] = portfolio.get(symbol, 0) + quantity
        print(f"Added {quantity} shares of {symbol}.\n")

    # 3. Calculate total investment
    if not portfolio:
        print("\nNo stocks were added to your portfolio.")
        return

    print("\n==========================================")
    print("          PORTFOLIO SUMMARY              ")
    print("==========================================")
    
    summary_lines = []
    summary_lines.append("CodeAlpha Stock Portfolio Tracker Report\n")
    summary_lines.append("------------------------------------------")

    for symbol, qty in portfolio.items():
        price = stock_prices[symbol]
        subtotal = price * qty
        total_investment += subtotal
        line = f"{symbol}: {qty} shares @ ${price:.2f} each = ${subtotal:.2f}"
        print(line)
        summary_lines.append(line)

    summary_lines.append("------------------------------------------")
    summary_lines.append(f"Total Portfolio Value: ${total_investment:.2f}")

    print("------------------------------------------")
    print(f"Total Portfolio Value: ${total_investment:.2f}")
    print("==========================================\n")

    # 4. Optional: Save summary to a .txt file
    save_option = input("Would you like to save this report to a text file? (y/n): ").strip().lower()
    if save_option == 'y':
        filename = "portfolio_summary.txt"
        with open(filename, "w") as file:
            file.write("\n".join(summary_lines))
        print(f"Success! Report saved to '{filename}'.")

if __name__ == "__main__":
    stock_portfolio_tracker()