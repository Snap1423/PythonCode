"""
Shopping Bill Calculator
A practical program to calculate shopping bills with discounts and taxes.
Demonstrates: Arithmetic operators, Input/Output, Type casting, Formatted output
"""

def main():
    print("=" * 60)
    print("             SHOPPING BILL CALCULATOR")
    print("=" * 60)
    
    # Store information
    store_name = "Tech Mart"
    print(f"Welcome to {store_name}!")
    
    # Get customer information
    customer_name = input("Enter customer name: ")
    
    items = []
    total_amount = 0.0
    
    print("\nEnter item details (Enter 'done' as item name to finish):")
    
    while True:
        item_name = input("Item name: ")
        if item_name.lower() == 'done':
            break
            
        try:
            quantity = int(input("Quantity: "))
            price_per_unit = float(input("Price per unit: ₹"))
            
            item_total = quantity * price_per_unit
            items.append({
                'name': item_name,
                'quantity': quantity,
                'price': price_per_unit,
                'total': item_total
            })
            
            total_amount += item_total
            print(f"Added: {item_name} x {quantity} = ₹{item_total:.2f}\n")
            
        except ValueError:
            print("Please enter valid numbers for quantity and price!\n")
    
    if not items:
        print("No items purchased!")
        return
    
    # Calculate discounts and taxes
    discount_rate = 0.0
    if total_amount > 5000:
        discount_rate = 0.15  # 15% discount for purchases above ₹5000
    elif total_amount > 2000:
        discount_rate = 0.10  # 10% discount for purchases above ₹2000
    elif total_amount > 1000:
        discount_rate = 0.05  # 5% discount for purchases above ₹1000
    
    discount_amount = total_amount * discount_rate
    amount_after_discount = total_amount - discount_amount
    
    # Tax calculation (GST)
    tax_rate = 0.18  # 18% GST
    tax_amount = amount_after_discount * tax_rate
    final_amount = amount_after_discount + tax_amount
    
    # Print detailed bill
    print("\n" + "=" * 60)
    print(f"                    {store_name.upper()}")
    print("                   TAX INVOICE")
    print("=" * 60)
    print(f"Customer: {customer_name}")
    print(f"Date: {__import__('datetime').datetime.now().strftime('%d/%m/%Y %H:%M')}")
    print("-" * 60)
    print(f"{'Item':<20} {'Qty':<5} {'Rate':<10} {'Amount':<10}")
    print("-" * 60)
    
    for item in items:
        print(f"{item['name']:<20} {item['quantity']:<5} "
              f"₹{item['price']:<9.2f} ₹{item['total']:<9.2f}")
    
    print("-" * 60)
    print(f"{'Subtotal:':<45} ₹{total_amount:>10.2f}")
    
    if discount_rate > 0:
        print(f"{'Discount (' + str(int(discount_rate * 100)) + '%):':<45} -₹{discount_amount:>9.2f}")
        print(f"{'Amount after discount:':<45} ₹{amount_after_discount:>10.2f}")
    
    print(f"{'GST (' + str(int(tax_rate * 100)) + '%):':<45} ₹{tax_amount:>10.2f}")
    print("=" * 60)
    print(f"{'TOTAL AMOUNT:':<45} ₹{final_amount:>10.2f}")
    print("=" * 60)
    
    # Payment information
    print(f"\nItems purchased: {len(items)}")
    print(f"You saved: ₹{discount_amount:.2f}")
    print("Thank you for shopping with us!")

if __name__ == "__main__":
    main() 