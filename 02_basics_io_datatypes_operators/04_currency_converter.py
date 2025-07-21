"""
Currency Converter
A practical program to convert between different currencies.
Demonstrates: Arithmetic operators, Dictionaries as data storage, Formatted output
"""

def main():
    print("=" * 60)
    print("              CURRENCY CONVERTER")
    print("=" * 60)
    
    # Exchange rates (as of a sample date - in real application, fetch from API)
    exchange_rates = {
        'USD': {'INR': 83.25, 'EUR': 0.92, 'GBP': 0.79, 'JPY': 149.50, 'CAD': 1.36},
        'INR': {'USD': 0.012, 'EUR': 0.011, 'GBP': 0.0095, 'JPY': 1.80, 'CAD': 0.016},
        'EUR': {'USD': 1.09, 'INR': 90.50, 'GBP': 0.86, 'JPY': 163.20, 'CAD': 1.48},
        'GBP': {'USD': 1.27, 'INR': 105.30, 'EUR': 1.16, 'JPY': 189.80, 'CAD': 1.72},
        'JPY': {'USD': 0.0067, 'INR': 0.56, 'EUR': 0.0061, 'GBP': 0.0053, 'CAD': 0.0091},
        'CAD': {'USD': 0.74, 'INR': 61.20, 'EUR': 0.68, 'GBP': 0.58, 'JPY': 110.40}
    }
    
    currencies = {
        'USD': 'US Dollar',
        'INR': 'Indian Rupee',
        'EUR': 'Euro',
        'GBP': 'British Pound',
        'JPY': 'Japanese Yen',
        'CAD': 'Canadian Dollar'
    }
    
    print("Available Currencies:")
    print("-" * 40)
    for code, name in currencies.items():
        print(f"{code} - {name}")
    print("-" * 40)
    
    # Get user input
    while True:
        from_currency = input("Enter source currency code: ").upper()
        if from_currency in currencies:
            break
        print("Invalid currency code. Please try again.")
    
    while True:
        to_currency = input("Enter target currency code: ").upper()
        if to_currency in currencies:
            break
        print("Invalid currency code. Please try again.")
    
    if from_currency == to_currency:
        print("Source and target currencies are the same!")
        return
    
    while True:
        try:
            amount = float(input(f"Enter amount in {from_currency}: "))
            if amount >= 0:
                break
            else:
                print("Amount cannot be negative!")
        except ValueError:
            print("Please enter a valid number!")
    
    # Perform conversion
    if to_currency in exchange_rates[from_currency]:
        rate = exchange_rates[from_currency][to_currency]
        converted_amount = amount * rate
    else:
        print("Exchange rate not available for this currency pair.")
        return
    
    # Calculate fees (example: 2% conversion fee)
    conversion_fee_rate = 0.02
    fee = converted_amount * conversion_fee_rate
    final_amount = converted_amount - fee
    
    # Display results
    print("\n" + "=" * 60)
    print("              CONVERSION RESULT")
    print("=" * 60)
    print(f"From: {currencies[from_currency]} ({from_currency})")
    print(f"To: {currencies[to_currency]} ({to_currency})")
    print(f"Exchange Rate: 1 {from_currency} = {rate:.4f} {to_currency}")
    print("-" * 60)
    print(f"Original Amount: {amount:,.2f} {from_currency}")
    print(f"Converted Amount: {converted_amount:,.2f} {to_currency}")
    print(f"Conversion Fee (2%): {fee:,.2f} {to_currency}")
    print(f"Final Amount: {final_amount:,.2f} {to_currency}")
    print("=" * 60)
    
    # Additional calculations
    print("\nAdditional Information:")
    print(f"• You are converting {amount:,.2f} {currencies[from_currency]}")
    print(f"• Exchange rate used: {rate:.4f}")
    print(f"• Fee percentage: {conversion_fee_rate * 100}%")
    
    # Reverse conversion for reference
    reverse_rate = 1 / rate
    print(f"• Reverse rate: 1 {to_currency} = {reverse_rate:.4f} {from_currency}")
    
    # Show conversion for common amounts
    print(f"\nQuick Reference:")
    common_amounts = [1, 10, 100, 1000]
    for amt in common_amounts:
        converted = amt * rate
        print(f"• {amt} {from_currency} = {converted:.2f} {to_currency}")
    
    print("\nNote: Exchange rates are indicative and may vary.")
    print("Actual rates may differ based on your bank or exchange service.")

if __name__ == "__main__":
    main() 