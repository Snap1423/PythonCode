"""
ATM Machine Simulator
A practical program simulating ATM operations with conditional statements.
Demonstrates: If-else statements, nested conditions, multiway branching
"""

def main():
    print("=" * 50)
    print("          ATM MACHINE SIMULATOR")
    print("=" * 50)
    
    # Initial account setup
    account_balance = 10000.0
    pin = "1234"
    max_attempts = 3
    daily_limit = 25000.0
    withdrawn_today = 0.0
    
    print("Welcome to PyBank ATM")
    print("Please insert your card...")
    
    # PIN verification
    attempts = 0
    while attempts < max_attempts:
        entered_pin = input(f"Enter your 4-digit PIN (Attempt {attempts + 1}/{max_attempts}): ")
        
        if entered_pin == pin:
            print("PIN verified successfully!")
            break
        else:
            attempts += 1
            if attempts == max_attempts:
                print("Maximum attempts exceeded. Card blocked!")
                print("Please contact your bank.")
                return
            else:
                print(f"Incorrect PIN. {max_attempts - attempts} attempts remaining.")
    
    # Main ATM menu
    while True:
        print("\n" + "=" * 50)
        print("              ATM MAIN MENU")
        print("=" * 50)
        print("1. Check Balance")
        print("2. Withdraw Cash")
        print("3. Deposit Cash")
        print("4. Mini Statement")
        print("5. Change PIN")
        print("6. Exit")
        print("-" * 50)
        
        choice = input("Select an option (1-6): ")
        
        if choice == "1":
            # Check Balance
            print("\n" + "-" * 30)
            print("        BALANCE INQUIRY")
            print("-" * 30)
            print(f"Available Balance: ₹{account_balance:,.2f}")
            print(f"Today's Withdrawal: ₹{withdrawn_today:,.2f}")
            print(f"Remaining Daily Limit: ₹{daily_limit - withdrawn_today:,.2f}")
            
        elif choice == "2":
            # Withdraw Cash
            print("\n" + "-" * 30)
            print("        CASH WITHDRAWAL")
            print("-" * 30)
            print("Select amount or enter custom amount:")
            print("1. ₹500    2. ₹1000    3. ₹2000")
            print("4. ₹5000   5. ₹10000   6. Custom")
            
            withdraw_choice = input("Enter choice (1-6): ")
            
            if withdraw_choice == "1":
                amount = 500
            elif withdraw_choice == "2":
                amount = 1000
            elif withdraw_choice == "3":
                amount = 2000
            elif withdraw_choice == "4":
                amount = 5000
            elif withdraw_choice == "5":
                amount = 10000
            elif withdraw_choice == "6":
                try:
                    amount = float(input("Enter amount: ₹"))
                except ValueError:
                    print("Invalid amount entered!")
                    continue
            else:
                print("Invalid choice!")
                continue
            
            # Validate withdrawal
            if amount <= 0:
                print("Amount must be positive!")
            elif amount % 100 != 0:
                print("Amount must be in multiples of ₹100!")
            elif amount > account_balance:
                print("Insufficient balance!")
                print(f"Available balance: ₹{account_balance:,.2f}")
            elif (withdrawn_today + amount) > daily_limit:
                print("Daily withdrawal limit exceeded!")
                print(f"Remaining limit: ₹{daily_limit - withdrawn_today:,.2f}")
            elif amount > 20000:
                print("Single transaction limit is ₹20,000")
            else:
                # Process withdrawal
                account_balance -= amount
                withdrawn_today += amount
                print("\n" + "✓" * 30)
                print("Transaction Successful!")
                print(f"Amount Withdrawn: ₹{amount:,.2f}")
                print(f"Remaining Balance: ₹{account_balance:,.2f}")
                print("Please collect your cash")
                print("✓" * 30)
        
        elif choice == "3":
            # Deposit Cash
            print("\n" + "-" * 30)
            print("        CASH DEPOSIT")
            print("-" * 30)
            
            try:
                amount = float(input("Enter deposit amount: ₹"))
                
                if amount <= 0:
                    print("Amount must be positive!")
                elif amount > 50000:
                    print("Single deposit limit is ₹50,000")
                    print("For larger deposits, please visit the branch")
                else:
                    # Process deposit
                    account_balance += amount
                    print("\n" + "✓" * 30)
                    print("Deposit Successful!")
                    print(f"Amount Deposited: ₹{amount:,.2f}")
                    print(f"New Balance: ₹{account_balance:,.2f}")
                    print("✓" * 30)
                    
            except ValueError:
                print("Invalid amount entered!")
        
        elif choice == "4":
            # Mini Statement
            print("\n" + "-" * 40)
            print("           MINI STATEMENT")
            print("-" * 40)
            print("Account Summary:")
            print(f"Current Balance: ₹{account_balance:,.2f}")
            print(f"Today's Withdrawals: ₹{withdrawn_today:,.2f}")
            print(f"Available Daily Limit: ₹{daily_limit - withdrawn_today:,.2f}")
            print("-" * 40)
            print("Recent Transactions:")
            print("• Balance inquiry - Today")
            if withdrawn_today > 0:
                print(f"• Cash withdrawal ₹{withdrawn_today:,.2f} - Today")
            print("• Account opened - Last month")
            print("-" * 40)
        
        elif choice == "5":
            # Change PIN
            print("\n" + "-" * 30)
            print("         CHANGE PIN")
            print("-" * 30)
            
            current_pin = input("Enter current PIN: ")
            if current_pin != pin:
                print("Incorrect current PIN!")
                continue
            
            new_pin = input("Enter new 4-digit PIN: ")
            if len(new_pin) != 4 or not new_pin.isdigit():
                print("PIN must be exactly 4 digits!")
                continue
            
            confirm_pin = input("Confirm new PIN: ")
            if new_pin != confirm_pin:
                print("PINs do not match!")
                continue
            
            # Additional PIN validation
            if new_pin == "0000" or new_pin == "1234":
                print("Please choose a more secure PIN!")
                continue
            
            # Check for sequential or repeated digits
            if (new_pin == "1234" or new_pin == "4321" or 
                len(set(new_pin)) == 1):
                print("PIN should not have sequential or repeated digits!")
                continue
            
            pin = new_pin
            print("\n" + "✓" * 30)
            print("PIN changed successfully!")
            print("Please remember your new PIN")
            print("✓" * 30)
        
        elif choice == "6":
            # Exit
            print("\n" + "=" * 50)
            print("Thank you for using PyBank ATM!")
            print("Please collect your card")
            print("Have a great day!")
            print("=" * 50)
            break
        
        else:
            print("Invalid choice! Please select 1-6.")
        
        # Ask if user wants to continue
        if choice != "6":
            continue_choice = input("\nDo you want to perform another transaction? (y/n): ")
            if continue_choice.lower() != 'y':
                print("\n" + "=" * 50)
                print("Thank you for using PyBank ATM!")
                print("Please collect your card")
                print("=" * 50)
                break

if __name__ == "__main__":
    main() 