"""
Banking Transaction System
A practical program for managing bank accounts with transaction history using loops.
Demonstrates: While loops, for loops, data processing, transaction management
"""

import datetime
import random

def main():
    print("=" * 60)
    print("           BANKING TRANSACTION SYSTEM")
    print("=" * 60)
    
    # Initialize bank data
    accounts = {}
    transaction_id_counter = 1000
    
    print("🏦 Welcome to PyBank - Advanced Banking System")
    print("Manage multiple accounts with complete transaction history")
    
    while True:
        print("\n" + "=" * 60)
        print("               MAIN BANKING MENU")
        print("=" * 60)
        print("1. Create New Account")
        print("2. Account Login")
        print("3. Admin Panel")
        print("4. Bank Statistics")
        print("5. Exit")
        print("-" * 60)
        
        choice = input("Select an option (1-5): ")
        
        if choice == "1":
            # Create New Account
            print("\n📝 CREATE NEW ACCOUNT")
            print("-" * 30)
            
            # Get account details with validation
            while True:
                account_number = input("Enter account number (6 digits): ")
                if len(account_number) == 6 and account_number.isdigit():
                    if account_number not in accounts:
                        break
                    else:
                        print("Account number already exists!")
                else:
                    print("Please enter exactly 6 digits!")
            
            customer_name = input("Enter customer name: ")
            while not customer_name.strip():
                customer_name = input("Name cannot be empty. Enter customer name: ")
            
            # Initial deposit with validation
            while True:
                try:
                    initial_deposit = float(input("Enter initial deposit (minimum ₹500): "))
                    if initial_deposit >= 500:
                        break
                    else:
                        print("Minimum initial deposit is ₹500!")
                except ValueError:
                    print("Please enter a valid amount!")
            
            # Account type selection
            print("\nSelect Account Type:")
            print("1. Savings Account (3% interest)")
            print("2. Current Account (No interest)")
            print("3. Fixed Deposit (5% interest)")
            
            while True:
                try:
                    acc_type_choice = int(input("Choose account type (1-3): "))
                    if acc_type_choice in [1, 2, 3]:
                        account_types = {1: "Savings", 2: "Current", 3: "Fixed Deposit"}
                        account_type = account_types[acc_type_choice]
                        break
                    else:
                        print("Please choose 1, 2, or 3!")
                except ValueError:
                    print("Please enter a valid number!")
            
            # Create account
            accounts[account_number] = {
                "name": customer_name,
                "balance": initial_deposit,
                "account_type": account_type,
                "created_date": datetime.datetime.now(),
                "transactions": [],
                "is_active": True
            }
            
            # Add initial deposit transaction
            transaction = {
                "id": transaction_id_counter,
                "type": "Deposit",
                "amount": initial_deposit,
                "balance_after": initial_deposit,
                "date": datetime.datetime.now(),
                "description": "Initial deposit - Account opening"
            }
            accounts[account_number]["transactions"].append(transaction)
            transaction_id_counter += 1
            
            print(f"\n✅ Account created successfully!")
            print(f"Account Number: {account_number}")
            print(f"Account Holder: {customer_name}")
            print(f"Account Type: {account_type}")
            print(f"Initial Balance: ₹{initial_deposit:,.2f}")
        
        elif choice == "2":
            # Account Login
            if not accounts:
                print("\n❌ No accounts exist. Please create an account first!")
                continue
            
            print("\n🔐 ACCOUNT LOGIN")
            print("-" * 25)
            
            account_number = input("Enter account number: ")
            
            if account_number not in accounts:
                print("❌ Account not found!")
                continue
            
            if not accounts[account_number]["is_active"]:
                print("❌ Account is deactivated!")
                continue
            
            account = accounts[account_number]
            print(f"\n✅ Welcome, {account['name']}!")
            
            # Account operations loop
            while True:
                print(f"\n" + "=" * 50)
                print(f"         ACCOUNT OPERATIONS")
                print(f"Account: {account_number} | Balance: ₹{account['balance']:,.2f}")
                print("=" * 50)
                print("1. Check Balance")
                print("2. Deposit Money")
                print("3. Withdraw Money")
                print("4. Transfer Money")
                print("5. Transaction History")
                print("6. Account Statement")
                print("7. Calculate Interest")
                print("8. Logout")
                print("-" * 50)
                
                operation = input("Select operation (1-8): ")
                
                if operation == "1":
                    # Check Balance
                    print(f"\n💰 CURRENT BALANCE")
                    print("-" * 25)
                    print(f"Account Number: {account_number}")
                    print(f"Account Holder: {account['name']}")
                    print(f"Account Type: {account['account_type']}")
                    print(f"Current Balance: ₹{account['balance']:,.2f}")
                    print(f"Last Transaction: {account['transactions'][-1]['date'].strftime('%d/%m/%Y %H:%M') if account['transactions'] else 'None'}")
                
                elif operation == "2":
                    # Deposit Money
                    print(f"\n💵 DEPOSIT MONEY")
                    print("-" * 20)
                    
                    try:
                        amount = float(input("Enter deposit amount: ₹"))
                        if amount <= 0:
                            print("Amount must be positive!")
                            continue
                        if amount > 100000:
                            print("Single deposit limit is ₹1,00,000!")
                            continue
                        
                        # Process deposit
                        old_balance = account['balance']
                        account['balance'] += amount
                        
                        # Add transaction record
                        transaction = {
                            "id": transaction_id_counter,
                            "type": "Deposit",
                            "amount": amount,
                            "balance_after": account['balance'],
                            "date": datetime.datetime.now(),
                            "description": "Cash deposit"
                        }
                        account['transactions'].append(transaction)
                        transaction_id_counter += 1
                        
                        print(f"\n✅ Deposit Successful!")
                        print(f"Amount Deposited: ₹{amount:,.2f}")
                        print(f"Previous Balance: ₹{old_balance:,.2f}")
                        print(f"New Balance: ₹{account['balance']:,.2f}")
                        print(f"Transaction ID: {transaction['id']}")
                        
                    except ValueError:
                        print("Please enter a valid amount!")
                
                elif operation == "3":
                    # Withdraw Money
                    print(f"\n💸 WITHDRAW MONEY")
                    print("-" * 20)
                    
                    try:
                        amount = float(input("Enter withdrawal amount: ₹"))
                        if amount <= 0:
                            print("Amount must be positive!")
                            continue
                        if amount > account['balance']:
                            print(f"Insufficient balance! Available: ₹{account['balance']:,.2f}")
                            continue
                        if amount > 25000:
                            print("Single withdrawal limit is ₹25,000!")
                            continue
                        
                        # Check minimum balance for savings account
                        if account['account_type'] == "Savings":
                            if (account['balance'] - amount) < 1000:
                                print("Cannot withdraw! Minimum balance of ₹1,000 required for savings account.")
                                continue
                        
                        # Process withdrawal
                        old_balance = account['balance']
                        account['balance'] -= amount
                        
                        # Add transaction record
                        transaction = {
                            "id": transaction_id_counter,
                            "type": "Withdrawal",
                            "amount": amount,
                            "balance_after": account['balance'],
                            "date": datetime.datetime.now(),
                            "description": "Cash withdrawal"
                        }
                        account['transactions'].append(transaction)
                        transaction_id_counter += 1
                        
                        print(f"\n✅ Withdrawal Successful!")
                        print(f"Amount Withdrawn: ₹{amount:,.2f}")
                        print(f"Previous Balance: ₹{old_balance:,.2f}")
                        print(f"New Balance: ₹{account['balance']:,.2f}")
                        print(f"Transaction ID: {transaction['id']}")
                        
                    except ValueError:
                        print("Please enter a valid amount!")
                
                elif operation == "4":
                    # Transfer Money
                    print(f"\n🔄 TRANSFER MONEY")
                    print("-" * 20)
                    
                    target_account = input("Enter target account number: ")
                    
                    if target_account not in accounts:
                        print("❌ Target account not found!")
                        continue
                    
                    if target_account == account_number:
                        print("❌ Cannot transfer to the same account!")
                        continue
                    
                    if not accounts[target_account]["is_active"]:
                        print("❌ Target account is deactivated!")
                        continue
                    
                    try:
                        amount = float(input("Enter transfer amount: ₹"))
                        if amount <= 0:
                            print("Amount must be positive!")
                            continue
                        if amount > account['balance']:
                            print(f"Insufficient balance! Available: ₹{account['balance']:,.2f}")
                            continue
                        if amount > 50000:
                            print("Single transfer limit is ₹50,000!")
                            continue
                        
                        # Check minimum balance
                        if account['account_type'] == "Savings":
                            if (account['balance'] - amount) < 1000:
                                print("Cannot transfer! Minimum balance of ₹1,000 required.")
                                continue
                        
                        # Get transfer description
                        description = input("Enter transfer description (optional): ")
                        if not description.strip():
                            description = f"Transfer to {target_account}"
                        
                        # Process transfer
                        old_balance_sender = account['balance']
                        old_balance_receiver = accounts[target_account]['balance']
                        
                        account['balance'] -= amount
                        accounts[target_account]['balance'] += amount
                        
                        # Add transaction records for sender
                        transaction_sender = {
                            "id": transaction_id_counter,
                            "type": "Transfer Out",
                            "amount": amount,
                            "balance_after": account['balance'],
                            "date": datetime.datetime.now(),
                            "description": f"Transfer to {target_account} - {description}",
                            "target_account": target_account
                        }
                        account['transactions'].append(transaction_sender)
                        transaction_id_counter += 1
                        
                        # Add transaction records for receiver
                        transaction_receiver = {
                            "id": transaction_id_counter,
                            "type": "Transfer In",
                            "amount": amount,
                            "balance_after": accounts[target_account]['balance'],
                            "date": datetime.datetime.now(),
                            "description": f"Transfer from {account_number} - {description}",
                            "source_account": account_number
                        }
                        accounts[target_account]['transactions'].append(transaction_receiver)
                        transaction_id_counter += 1
                        
                        print(f"\n✅ Transfer Successful!")
                        print(f"Amount Transferred: ₹{amount:,.2f}")
                        print(f"To Account: {target_account} ({accounts[target_account]['name']})")
                        print(f"Your New Balance: ₹{account['balance']:,.2f}")
                        print(f"Transaction ID: {transaction_sender['id']}")
                        
                    except ValueError:
                        print("Please enter a valid amount!")
                
                elif operation == "5":
                    # Transaction History
                    print(f"\n📋 TRANSACTION HISTORY")
                    print("-" * 40)
                    
                    if not account['transactions']:
                        print("No transactions found!")
                        continue
                    
                    # Show options for filtering
                    print("1. Show all transactions")
                    print("2. Show last 10 transactions")
                    print("3. Show transactions by type")
                    print("4. Show transactions by date range")
                    
                    filter_choice = input("Choose filter option (1-4): ")
                    
                    transactions_to_show = account['transactions']
                    
                    if filter_choice == "2":
                        transactions_to_show = account['transactions'][-10:]
                    elif filter_choice == "3":
                        print("Transaction types: Deposit, Withdrawal, Transfer In, Transfer Out")
                        filter_type = input("Enter transaction type: ")
                        transactions_to_show = [t for t in account['transactions'] if t['type'].lower() == filter_type.lower()]
                    elif filter_choice == "4":
                        print("Date filtering (simplified - last N days)")
                        try:
                            days = int(input("Show transactions from last N days: "))
                            cutoff_date = datetime.datetime.now() - datetime.timedelta(days=days)
                            transactions_to_show = [t for t in account['transactions'] if t['date'] >= cutoff_date]
                        except ValueError:
                            print("Invalid input, showing all transactions")
                    
                    # Display transactions
                    if not transactions_to_show:
                        print("No transactions match the filter criteria!")
                        continue
                    
                    print(f"\n{'ID':<6} {'Type':<12} {'Amount':<12} {'Balance':<12} {'Date':<12} {'Description'}")
                    print("-" * 80)
                    
                    for transaction in transactions_to_show:
                        amount_str = f"₹{transaction['amount']:,.2f}"
                        balance_str = f"₹{transaction['balance_after']:,.2f}"
                        date_str = transaction['date'].strftime('%d/%m/%Y')
                        desc = transaction['description'][:20] + "..." if len(transaction['description']) > 20 else transaction['description']
                        
                        print(f"{transaction['id']:<6} {transaction['type']:<12} {amount_str:<12} {balance_str:<12} {date_str:<12} {desc}")
                
                elif operation == "6":
                    # Account Statement
                    print(f"\n📄 ACCOUNT STATEMENT")
                    print("=" * 50)
                    print(f"Account Number: {account_number}")
                    print(f"Account Holder: {account['name']}")
                    print(f"Account Type: {account['account_type']}")
                    print(f"Account Opened: {account['created_date'].strftime('%d/%m/%Y')}")
                    print(f"Current Balance: ₹{account['balance']:,.2f}")
                    print(f"Total Transactions: {len(account['transactions'])}")
                    
                    if account['transactions']:
                        # Calculate statistics
                        total_deposits = sum(t['amount'] for t in account['transactions'] if t['type'] in ['Deposit', 'Transfer In'])
                        total_withdrawals = sum(t['amount'] for t in account['transactions'] if t['type'] in ['Withdrawal', 'Transfer Out'])
                        
                        print(f"Total Deposits: ₹{total_deposits:,.2f}")
                        print(f"Total Withdrawals: ₹{total_withdrawals:,.2f}")
                        print(f"Net Flow: ₹{total_deposits - total_withdrawals:,.2f}")
                        
                        # Recent activity
                        print(f"\nRecent Activity (Last 5 transactions):")
                        print("-" * 50)
                        recent_transactions = account['transactions'][-5:]
                        for transaction in recent_transactions:
                            date_str = transaction['date'].strftime('%d/%m/%Y %H:%M')
                            print(f"{date_str} | {transaction['type']} | ₹{transaction['amount']:,.2f}")
                
                elif operation == "7":
                    # Calculate Interest
                    print(f"\n📈 INTEREST CALCULATION")
                    print("-" * 30)
                    
                    if account['account_type'] == "Current":
                        print("Current accounts do not earn interest.")
                        continue
                    
                    interest_rates = {
                        "Savings": 0.03,  # 3%
                        "Fixed Deposit": 0.05  # 5%
                    }
                    
                    rate = interest_rates.get(account['account_type'], 0)
                    
                    print(f"Account Type: {account['account_type']}")
                    print(f"Interest Rate: {rate * 100}% per annum")
                    print(f"Current Balance: ₹{account['balance']:,.2f}")
                    
                    # Calculate interest for different periods
                    monthly_interest = (account['balance'] * rate) / 12
                    quarterly_interest = (account['balance'] * rate) / 4
                    annual_interest = account['balance'] * rate
                    
                    print(f"\nInterest Projections:")
                    print(f"Monthly Interest: ₹{monthly_interest:,.2f}")
                    print(f"Quarterly Interest: ₹{quarterly_interest:,.2f}")
                    print(f"Annual Interest: ₹{annual_interest:,.2f}")
                    
                    # Option to add interest
                    if account['account_type'] in ["Savings", "Fixed Deposit"]:
                        add_interest = input("\nAdd monthly interest to account? (y/n): ").lower()
                        if add_interest == 'y':
                            old_balance = account['balance']
                            account['balance'] += monthly_interest
                            
                            # Add interest transaction
                            transaction = {
                                "id": transaction_id_counter,
                                "type": "Interest Credit",
                                "amount": monthly_interest,
                                "balance_after": account['balance'],
                                "date": datetime.datetime.now(),
                                "description": f"Monthly interest @ {rate * 100}% p.a."
                            }
                            account['transactions'].append(transaction)
                            transaction_id_counter += 1
                            
                            print(f"✅ Interest credited successfully!")
                            print(f"Interest Amount: ₹{monthly_interest:,.2f}")
                            print(f"New Balance: ₹{account['balance']:,.2f}")
                
                elif operation == "8":
                    # Logout
                    print(f"\n👋 Thank you, {account['name']}!")
                    print("You have been logged out successfully.")
                    break
                
                else:
                    print("❌ Invalid choice! Please select 1-8.")
        
        elif choice == "3":
            # Admin Panel
            print("\n🔧 ADMIN PANEL")
            print("-" * 20)
            
            admin_password = input("Enter admin password: ")
            if admin_password != "admin123":
                print("❌ Invalid admin password!")
                continue
            
            while True:
                print(f"\n" + "=" * 40)
                print("         ADMIN OPERATIONS")
                print("=" * 40)
                print("1. View All Accounts")
                print("2. Deactivate Account")
                print("3. Activate Account")
                print("4. Delete Account")
                print("5. Reset Account Password")
                print("6. Back to Main Menu")
                print("-" * 40)
                
                admin_choice = input("Select operation (1-6): ")
                
                if admin_choice == "1":
                    # View All Accounts
                    if not accounts:
                        print("No accounts found!")
                        continue
                    
                    print(f"\n📊 ALL ACCOUNTS OVERVIEW")
                    print("-" * 70)
                    print(f"{'Account':<8} {'Name':<15} {'Type':<12} {'Balance':<12} {'Status':<8} {'Transactions'}")
                    print("-" * 70)
                    
                    for acc_num, acc_data in accounts.items():
                        status = "Active" if acc_data['is_active'] else "Inactive"
                        print(f"{acc_num:<8} {acc_data['name'][:14]:<15} {acc_data['account_type']:<12} ₹{acc_data['balance']:<11,.0f} {status:<8} {len(acc_data['transactions'])}")
                
                elif admin_choice == "2":
                    # Deactivate Account
                    acc_num = input("Enter account number to deactivate: ")
                    if acc_num in accounts:
                        accounts[acc_num]['is_active'] = False
                        print(f"✅ Account {acc_num} deactivated successfully!")
                    else:
                        print("❌ Account not found!")
                
                elif admin_choice == "3":
                    # Activate Account
                    acc_num = input("Enter account number to activate: ")
                    if acc_num in accounts:
                        accounts[acc_num]['is_active'] = True
                        print(f"✅ Account {acc_num} activated successfully!")
                    else:
                        print("❌ Account not found!")
                
                elif admin_choice == "4":
                    # Delete Account
                    acc_num = input("Enter account number to delete: ")
                    if acc_num in accounts:
                        confirm = input(f"Are you sure you want to delete account {acc_num}? (yes/no): ")
                        if confirm.lower() == "yes":
                            del accounts[acc_num]
                            print(f"✅ Account {acc_num} deleted successfully!")
                        else:
                            print("❌ Account deletion cancelled!")
                    else:
                        print("❌ Account not found!")
                
                elif admin_choice == "5":
                    # Reset Password (placeholder)
                    print("🔒 Password reset functionality would be implemented here")
                    print("This feature requires secure authentication mechanisms")
                
                elif admin_choice == "6":
                    break
                
                else:
                    print("❌ Invalid choice!")
        
        elif choice == "4":
            # Bank Statistics
            if not accounts:
                print("\n📊 No accounts exist yet!")
                continue
            
            print(f"\n📊 BANK STATISTICS")
            print("=" * 40)
            
            total_accounts = len(accounts)
            active_accounts = sum(1 for acc in accounts.values() if acc['is_active'])
            total_balance = sum(acc['balance'] for acc in accounts.values())
            total_transactions = sum(len(acc['transactions']) for acc in accounts.values())
            
            # Account type breakdown
            account_types = {}
            for acc in accounts.values():
                acc_type = acc['account_type']
                if acc_type not in account_types:
                    account_types[acc_type] = {'count': 0, 'balance': 0}
                account_types[acc_type]['count'] += 1
                account_types[acc_type]['balance'] += acc['balance']
            
            print(f"Total Accounts: {total_accounts}")
            print(f"Active Accounts: {active_accounts}")
            print(f"Total Bank Balance: ₹{total_balance:,.2f}")
            print(f"Total Transactions: {total_transactions}")
            print(f"Average Balance per Account: ₹{total_balance/total_accounts:,.2f}" if total_accounts > 0 else "N/A")
            
            print(f"\n📈 Account Type Breakdown:")
            print("-" * 40)
            for acc_type, data in account_types.items():
                avg_balance = data['balance'] / data['count'] if data['count'] > 0 else 0
                print(f"{acc_type}: {data['count']} accounts, ₹{data['balance']:,.2f} total, ₹{avg_balance:,.2f} avg")
            
            # Find largest account
            if accounts:
                largest_account = max(accounts.items(), key=lambda x: x[1]['balance'])
                print(f"\n💰 Largest Account: {largest_account[0]} with ₹{largest_account[1]['balance']:,.2f}")
        
        elif choice == "5":
            # Exit
            print(f"\n🏦 BANKING SYSTEM SUMMARY")
            print("=" * 50)
            print("Thank you for using PyBank!")
            
            if accounts:
                print(f"Session Summary:")
                print(f"• Managed {len(accounts)} accounts")
                print(f"• Total bank balance: ₹{sum(acc['balance'] for acc in accounts.values()):,.2f}")
                print(f"• Total transactions processed: {sum(len(acc['transactions']) for acc in accounts.values())}")
            
            print("Have a great day! 💳")
            break
        
        else:
            print("❌ Invalid choice! Please select 1-5.")

if __name__ == "__main__":
    main() 