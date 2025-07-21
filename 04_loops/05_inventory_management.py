"""
Inventory Management System
A practical program for managing store inventory with stock tracking and reporting.
Demonstrates: While loops, for loops, data manipulation, search algorithms, sorting
"""

import datetime
import random

def main():
    print("=" * 60)
    print("          INVENTORY MANAGEMENT SYSTEM")
    print("=" * 60)
    
    # Initialize inventory data
    inventory = {}
    categories = ["Electronics", "Clothing", "Books", "Home & Garden", "Sports", "Automotive"]
    transaction_log = []
    low_stock_threshold = 10
    
    print("📦 Welcome to StoreMax Inventory Management")
    print("Efficiently manage your store's inventory and track stock levels")
    
    # Sample data for demonstration
    sample_products = [
        {"id": "EL001", "name": "Smartphone", "category": "Electronics", "price": 25000, "stock": 15, "min_stock": 5},
        {"id": "CL001", "name": "T-Shirt", "category": "Clothing", "price": 500, "stock": 50, "min_stock": 10},
        {"id": "BK001", "name": "Python Programming Book", "category": "Books", "price": 800, "stock": 8, "min_stock": 5},
        {"id": "HG001", "name": "Garden Hose", "category": "Home & Garden", "price": 1200, "stock": 3, "min_stock": 5},
        {"id": "SP001", "name": "Football", "category": "Sports", "price": 1500, "stock": 20, "min_stock": 8}
    ]
    
    # Load sample data
    for product in sample_products:
        inventory[product["id"]] = product
    
    while True:
        print("\n" + "=" * 60)
        print("             INVENTORY MANAGEMENT MENU")
        print("=" * 60)
        print("1. View All Products")
        print("2. Add New Product")
        print("3. Update Product")
        print("4. Delete Product")
        print("5. Stock Management")
        print("6. Search Products")
        print("7. Reports & Analytics")
        print("8. Low Stock Alerts")
        print("9. Category Management")
        print("10. Exit")
        print("-" * 60)
        
        choice = input("Select an option (1-10): ")
        
        if choice == "1":
            # View All Products
            if not inventory:
                print("\n📋 No products in inventory!")
                continue
            
            print(f"\n📦 ALL PRODUCTS INVENTORY")
            print("=" * 80)
            print(f"{'ID':<8} {'Name':<20} {'Category':<15} {'Price':<10} {'Stock':<8} {'Status'}")
            print("-" * 80)
            
            for product_id, product in inventory.items():
                status = "Low Stock" if product['stock'] <= product['min_stock'] else "In Stock"
                if product['stock'] == 0:
                    status = "Out of Stock"
                
                print(f"{product_id:<8} {product['name'][:19]:<20} {product['category'][:14]:<15} "
                      f"₹{product['price']:<9} {product['stock']:<8} {status}")
            
            total_products = len(inventory)
            total_value = sum(p['price'] * p['stock'] for p in inventory.values())
            out_of_stock = sum(1 for p in inventory.values() if p['stock'] == 0)
            low_stock = sum(1 for p in inventory.values() if 0 < p['stock'] <= p['min_stock'])
            
            print("-" * 80)
            print(f"Total Products: {total_products} | Inventory Value: ₹{total_value:,}")
            print(f"Out of Stock: {out_of_stock} | Low Stock: {low_stock}")
        
        elif choice == "2":
            # Add New Product
            print(f"\n➕ ADD NEW PRODUCT")
            print("-" * 25)
            
            # Generate product ID
            while True:
                product_id = input("Enter product ID (e.g., EL001): ").upper()
                if product_id and product_id not in inventory:
                    break
                elif product_id in inventory:
                    print("Product ID already exists!")
                else:
                    print("Product ID cannot be empty!")
            
            # Get product details
            product_name = input("Enter product name: ")
            while not product_name.strip():
                product_name = input("Product name cannot be empty. Enter product name: ")
            
            # Category selection
            print(f"\nAvailable Categories:")
            for i, category in enumerate(categories, 1):
                print(f"{i}. {category}")
            print(f"{len(categories) + 1}. Add new category")
            
            while True:
                try:
                    cat_choice = int(input(f"Select category (1-{len(categories) + 1}): "))
                    if 1 <= cat_choice <= len(categories):
                        selected_category = categories[cat_choice - 1]
                        break
                    elif cat_choice == len(categories) + 1:
                        new_category = input("Enter new category name: ")
                        if new_category.strip():
                            categories.append(new_category)
                            selected_category = new_category
                            print(f"✅ New category '{new_category}' added!")
                            break
                        else:
                            print("Category name cannot be empty!")
                    else:
                        print(f"Please select 1-{len(categories) + 1}")
                except ValueError:
                    print("Please enter a valid number!")
            
            # Price input
            while True:
                try:
                    price = float(input("Enter product price: ₹"))
                    if price > 0:
                        break
                    else:
                        print("Price must be positive!")
                except ValueError:
                    print("Please enter a valid price!")
            
            # Stock quantity
            while True:
                try:
                    stock = int(input("Enter initial stock quantity: "))
                    if stock >= 0:
                        break
                    else:
                        print("Stock cannot be negative!")
                except ValueError:
                    print("Please enter a valid quantity!")
            
            # Minimum stock level
            while True:
                try:
                    min_stock = int(input("Enter minimum stock level: "))
                    if min_stock >= 0:
                        break
                    else:
                        print("Minimum stock cannot be negative!")
                except ValueError:
                    print("Please enter a valid quantity!")
            
            # Add product to inventory
            inventory[product_id] = {
                "name": product_name,
                "category": selected_category,
                "price": price,
                "stock": stock,
                "min_stock": min_stock,
                "created_date": datetime.datetime.now(),
                "last_updated": datetime.datetime.now()
            }
            
            # Log transaction
            transaction_log.append({
                "date": datetime.datetime.now(),
                "type": "Product Added",
                "product_id": product_id,
                "details": f"Added {product_name} with {stock} units"
            })
            
            print(f"\n✅ Product added successfully!")
            print(f"Product ID: {product_id}")
            print(f"Name: {product_name}")
            print(f"Category: {selected_category}")
            print(f"Price: ₹{price:,.2f}")
            print(f"Stock: {stock} units")
        
        elif choice == "3":
            # Update Product
            if not inventory:
                print("\n📋 No products to update!")
                continue
            
            print(f"\n✏️ UPDATE PRODUCT")
            print("-" * 20)
            
            product_id = input("Enter product ID to update: ").upper()
            
            if product_id not in inventory:
                print("❌ Product not found!")
                continue
            
            product = inventory[product_id]
            print(f"\nCurrent Product Details:")
            print(f"Name: {product['name']}")
            print(f"Category: {product['category']}")
            print(f"Price: ₹{product['price']}")
            print(f"Stock: {product['stock']}")
            print(f"Min Stock: {product['min_stock']}")
            
            print(f"\nWhat would you like to update?")
            print("1. Name")
            print("2. Category")
            print("3. Price")
            print("4. Stock Quantity")
            print("5. Minimum Stock Level")
            print("6. All Details")
            
            update_choice = input("Select option (1-6): ")
            
            if update_choice == "1":
                new_name = input(f"Enter new name (current: {product['name']}): ")
                if new_name.strip():
                    old_name = product['name']
                    product['name'] = new_name
                    print(f"✅ Name updated from '{old_name}' to '{new_name}'")
                    
            elif update_choice == "2":
                print(f"Available Categories:")
                for i, category in enumerate(categories, 1):
                    print(f"{i}. {category}")
                
                try:
                    cat_choice = int(input(f"Select new category (1-{len(categories)}): "))
                    if 1 <= cat_choice <= len(categories):
                        old_category = product['category']
                        product['category'] = categories[cat_choice - 1]
                        print(f"✅ Category updated from '{old_category}' to '{product['category']}'")
                    else:
                        print("Invalid category selection!")
                except ValueError:
                    print("Please enter a valid number!")
                    
            elif update_choice == "3":
                try:
                    new_price = float(input(f"Enter new price (current: ₹{product['price']}): ₹"))
                    if new_price > 0:
                        old_price = product['price']
                        product['price'] = new_price
                        print(f"✅ Price updated from ₹{old_price} to ₹{new_price}")
                    else:
                        print("Price must be positive!")
                except ValueError:
                    print("Please enter a valid price!")
                    
            elif update_choice == "4":
                try:
                    new_stock = int(input(f"Enter new stock quantity (current: {product['stock']}): "))
                    if new_stock >= 0:
                        old_stock = product['stock']
                        product['stock'] = new_stock
                        print(f"✅ Stock updated from {old_stock} to {new_stock}")
                        
                        # Log stock change
                        transaction_log.append({
                            "date": datetime.datetime.now(),
                            "type": "Stock Updated",
                            "product_id": product_id,
                            "details": f"Stock changed from {old_stock} to {new_stock}"
                        })
                    else:
                        print("Stock cannot be negative!")
                except ValueError:
                    print("Please enter a valid quantity!")
                    
            elif update_choice == "5":
                try:
                    new_min_stock = int(input(f"Enter new minimum stock level (current: {product['min_stock']}): "))
                    if new_min_stock >= 0:
                        old_min_stock = product['min_stock']
                        product['min_stock'] = new_min_stock
                        print(f"✅ Minimum stock updated from {old_min_stock} to {new_min_stock}")
                    else:
                        print("Minimum stock cannot be negative!")
                except ValueError:
                    print("Please enter a valid quantity!")
                    
            elif update_choice == "6":
                print("Updating all details...")
                # This would involve updating all fields one by one
                print("💡 Use individual update options for now")
            
            # Update last modified date
            product['last_updated'] = datetime.datetime.now()
        
        elif choice == "4":
            # Delete Product
            if not inventory:
                print("\n📋 No products to delete!")
                continue
            
            print(f"\n🗑️ DELETE PRODUCT")
            print("-" * 20)
            
            product_id = input("Enter product ID to delete: ").upper()
            
            if product_id not in inventory:
                print("❌ Product not found!")
                continue
            
            product = inventory[product_id]
            print(f"\nProduct to delete:")
            print(f"ID: {product_id}")
            print(f"Name: {product['name']}")
            print(f"Stock: {product['stock']} units")
            print(f"Value: ₹{product['price'] * product['stock']:,.2f}")
            
            confirm = input("\nAre you sure you want to delete this product? (yes/no): ")
            if confirm.lower() == "yes":
                # Log deletion
                transaction_log.append({
                    "date": datetime.datetime.now(),
                    "type": "Product Deleted",
                    "product_id": product_id,
                    "details": f"Deleted {product['name']} with {product['stock']} units"
                })
                
                del inventory[product_id]
                print(f"✅ Product {product_id} deleted successfully!")
            else:
                print("❌ Product deletion cancelled!")
        
        elif choice == "5":
            # Stock Management
            if not inventory:
                print("\n📋 No products for stock management!")
                continue
            
            print(f"\n📦 STOCK MANAGEMENT")
            print("-" * 25)
            print("1. Add Stock (Restock)")
            print("2. Remove Stock (Sale/Damage)")
            print("3. Stock Transfer")
            print("4. Bulk Stock Update")
            print("5. Stock Audit")
            
            stock_choice = input("Select stock operation (1-5): ")
            
            if stock_choice == "1":
                # Add Stock
                product_id = input("Enter product ID to restock: ").upper()
                
                if product_id not in inventory:
                    print("❌ Product not found!")
                    continue
                
                product = inventory[product_id]
                print(f"Product: {product['name']}")
                print(f"Current Stock: {product['stock']}")
                
                try:
                    add_quantity = int(input("Enter quantity to add: "))
                    if add_quantity > 0:
                        old_stock = product['stock']
                        product['stock'] += add_quantity
                        
                        # Log transaction
                        transaction_log.append({
                            "date": datetime.datetime.now(),
                            "type": "Stock Added",
                            "product_id": product_id,
                            "details": f"Added {add_quantity} units (from {old_stock} to {product['stock']})"
                        })
                        
                        print(f"✅ Stock updated!")
                        print(f"Previous Stock: {old_stock}")
                        print(f"Added: {add_quantity}")
                        print(f"New Stock: {product['stock']}")
                        
                        # Update last modified
                        product['last_updated'] = datetime.datetime.now()
                    else:
                        print("Quantity must be positive!")
                except ValueError:
                    print("Please enter a valid quantity!")
                    
            elif stock_choice == "2":
                # Remove Stock
                product_id = input("Enter product ID to remove stock: ").upper()
                
                if product_id not in inventory:
                    print("❌ Product not found!")
                    continue
                
                product = inventory[product_id]
                print(f"Product: {product['name']}")
                print(f"Current Stock: {product['stock']}")
                
                try:
                    remove_quantity = int(input("Enter quantity to remove: "))
                    if remove_quantity > 0:
                        if remove_quantity <= product['stock']:
                            old_stock = product['stock']
                            product['stock'] -= remove_quantity
                            
                            # Log transaction
                            reason = input("Reason for removal (sale/damage/other): ")
                            transaction_log.append({
                                "date": datetime.datetime.now(),
                                "type": "Stock Removed",
                                "product_id": product_id,
                                "details": f"Removed {remove_quantity} units ({reason}) - from {old_stock} to {product['stock']}"
                            })
                            
                            print(f"✅ Stock updated!")
                            print(f"Previous Stock: {old_stock}")
                            print(f"Removed: {remove_quantity}")
                            print(f"New Stock: {product['stock']}")
                            
                            if product['stock'] <= product['min_stock']:
                                print(f"⚠️ WARNING: Stock is now at or below minimum level!")
                            
                            # Update last modified
                            product['last_updated'] = datetime.datetime.now()
                        else:
                            print(f"❌ Cannot remove {remove_quantity} units. Only {product['stock']} available!")
                    else:
                        print("Quantity must be positive!")
                except ValueError:
                    print("Please enter a valid quantity!")
                    
            elif stock_choice == "3":
                print("🔄 Stock transfer feature would be implemented for multi-location inventory")
                
            elif stock_choice == "4":
                # Bulk Stock Update
                print(f"\n📊 BULK STOCK UPDATE")
                print("-" * 25)
                print("1. Set all stocks to minimum level")
                print("2. Increase all stocks by percentage")
                print("3. Reset stocks for specific category")
                
                bulk_choice = input("Select bulk operation (1-3): ")
                
                if bulk_choice == "1":
                    confirm = input("Set all products to their minimum stock level? (yes/no): ")
                    if confirm.lower() == "yes":
                        updated_count = 0
                        for product_id, product in inventory.items():
                            if product['stock'] < product['min_stock']:
                                old_stock = product['stock']
                                product['stock'] = product['min_stock']
                                updated_count += 1
                                
                                transaction_log.append({
                                    "date": datetime.datetime.now(),
                                    "type": "Bulk Stock Update",
                                    "product_id": product_id,
                                    "details": f"Set to minimum level: {old_stock} → {product['stock']}"
                                })
                        
                        print(f"✅ Updated {updated_count} products to minimum stock levels!")
                        
                elif bulk_choice == "2":
                    try:
                        percentage = float(input("Enter percentage increase (e.g., 10 for 10%): "))
                        if percentage > 0:
                            updated_count = 0
                            for product_id, product in inventory.items():
                                old_stock = product['stock']
                                increase = int(product['stock'] * (percentage / 100))
                                product['stock'] += increase
                                updated_count += 1
                                
                                transaction_log.append({
                                    "date": datetime.datetime.now(),
                                    "type": "Bulk Stock Increase",
                                    "product_id": product_id,
                                    "details": f"Increased by {percentage}%: {old_stock} → {product['stock']}"
                                })
                            
                            print(f"✅ Increased stock for {updated_count} products by {percentage}%!")
                        else:
                            print("Percentage must be positive!")
                    except ValueError:
                        print("Please enter a valid percentage!")
                        
            elif stock_choice == "5":
                # Stock Audit
                print(f"\n🔍 STOCK AUDIT REPORT")
                print("=" * 40)
                
                total_items = len(inventory)
                out_of_stock_items = [p for p in inventory.values() if p['stock'] == 0]
                low_stock_items = [p for p in inventory.values() if 0 < p['stock'] <= p['min_stock']]
                overstock_items = [p for p in inventory.values() if p['stock'] > p['min_stock'] * 3]
                
                print(f"Total Products: {total_items}")
                print(f"Out of Stock: {len(out_of_stock_items)}")
                print(f"Low Stock: {len(low_stock_items)}")
                print(f"Overstock: {len(overstock_items)}")
                
                if out_of_stock_items:
                    print(f"\n❌ OUT OF STOCK ITEMS:")
                    for item in out_of_stock_items:
                        print(f"  • {item['name']} (ID: {[k for k, v in inventory.items() if v == item][0]})")
                
                if low_stock_items:
                    print(f"\n⚠️ LOW STOCK ITEMS:")
                    for item in low_stock_items:
                        item_id = [k for k, v in inventory.items() if v == item][0]
                        print(f"  • {item['name']} (ID: {item_id}) - {item['stock']}/{item['min_stock']} units")
        
        elif choice == "6":
            # Search Products
            if not inventory:
                print("\n📋 No products to search!")
                continue
            
            print(f"\n🔍 SEARCH PRODUCTS")
            print("-" * 20)
            print("1. Search by Name")
            print("2. Search by Category")
            print("3. Search by Price Range")
            print("4. Search by Stock Level")
            print("5. Advanced Search")
            
            search_choice = input("Select search type (1-5): ")
            
            if search_choice == "1":
                # Search by Name
                search_term = input("Enter product name to search: ").lower()
                found_products = []
                
                for product_id, product in inventory.items():
                    if search_term in product['name'].lower():
                        found_products.append((product_id, product))
                
                if found_products:
                    print(f"\n🔍 Found {len(found_products)} products:")
                    print(f"{'ID':<8} {'Name':<20} {'Category':<15} {'Price':<10} {'Stock'}")
                    print("-" * 65)
                    for product_id, product in found_products:
                        print(f"{product_id:<8} {product['name'][:19]:<20} {product['category'][:14]:<15} "
                              f"₹{product['price']:<9} {product['stock']}")
                else:
                    print("❌ No products found matching the search term!")
                    
            elif search_choice == "2":
                # Search by Category
                print(f"Available Categories:")
                available_categories = list(set(p['category'] for p in inventory.values()))
                for i, category in enumerate(available_categories, 1):
                    print(f"{i}. {category}")
                
                try:
                    cat_choice = int(input(f"Select category (1-{len(available_categories)}): "))
                    if 1 <= cat_choice <= len(available_categories):
                        selected_category = available_categories[cat_choice - 1]
                        found_products = [(pid, p) for pid, p in inventory.items() if p['category'] == selected_category]
                        
                        print(f"\n🔍 Products in '{selected_category}' category:")
                        print(f"{'ID':<8} {'Name':<20} {'Price':<10} {'Stock'}")
                        print("-" * 50)
                        for product_id, product in found_products:
                            print(f"{product_id:<8} {product['name'][:19]:<20} ₹{product['price']:<9} {product['stock']}")
                    else:
                        print("Invalid category selection!")
                except ValueError:
                    print("Please enter a valid number!")
                    
            elif search_choice == "3":
                # Search by Price Range
                try:
                    min_price = float(input("Enter minimum price: ₹"))
                    max_price = float(input("Enter maximum price: ₹"))
                    
                    if min_price <= max_price:
                        found_products = [(pid, p) for pid, p in inventory.items() 
                                        if min_price <= p['price'] <= max_price]
                        
                        if found_products:
                            print(f"\n🔍 Products in price range ₹{min_price} - ₹{max_price}:")
                            print(f"{'ID':<8} {'Name':<20} {'Category':<15} {'Price':<10} {'Stock'}")
                            print("-" * 65)
                            for product_id, product in found_products:
                                print(f"{product_id:<8} {product['name'][:19]:<20} {product['category'][:14]:<15} "
                                      f"₹{product['price']:<9} {product['stock']}")
                        else:
                            print("❌ No products found in this price range!")
                    else:
                        print("Minimum price cannot be greater than maximum price!")
                except ValueError:
                    print("Please enter valid prices!")
                    
            elif search_choice == "4":
                # Search by Stock Level
                print("Stock level filters:")
                print("1. Out of stock (0)")
                print("2. Low stock (below minimum)")
                print("3. In stock (above minimum)")
                print("4. Custom range")
                
                stock_filter = input("Select filter (1-4): ")
                
                if stock_filter == "1":
                    found_products = [(pid, p) for pid, p in inventory.items() if p['stock'] == 0]
                    filter_desc = "out of stock"
                elif stock_filter == "2":
                    found_products = [(pid, p) for pid, p in inventory.items() if 0 < p['stock'] <= p['min_stock']]
                    filter_desc = "low stock"
                elif stock_filter == "3":
                    found_products = [(pid, p) for pid, p in inventory.items() if p['stock'] > p['min_stock']]
                    filter_desc = "in stock"
                elif stock_filter == "4":
                    try:
                        min_stock = int(input("Enter minimum stock: "))
                        max_stock = int(input("Enter maximum stock: "))
                        found_products = [(pid, p) for pid, p in inventory.items() 
                                        if min_stock <= p['stock'] <= max_stock]
                        filter_desc = f"stock between {min_stock} and {max_stock}"
                    except ValueError:
                        print("Please enter valid stock numbers!")
                        continue
                else:
                    print("Invalid filter selection!")
                    continue
                
                if found_products:
                    print(f"\n🔍 Products with {filter_desc}:")
                    print(f"{'ID':<8} {'Name':<20} {'Category':<15} {'Stock':<8} {'Min Stock'}")
                    print("-" * 70)
                    for product_id, product in found_products:
                        print(f"{product_id:<8} {product['name'][:19]:<20} {product['category'][:14]:<15} "
                              f"{product['stock']:<8} {product['min_stock']}")
                else:
                    print(f"❌ No products found with {filter_desc}!")
        
        elif choice == "7":
            # Reports & Analytics
            if not inventory:
                print("\n📊 No data for reports!")
                continue
            
            print(f"\n📊 REPORTS & ANALYTICS")
            print("-" * 30)
            print("1. Inventory Summary")
            print("2. Category Analysis")
            print("3. Stock Value Report")
            print("4. Transaction Log")
            print("5. Top Products by Value")
            
            report_choice = input("Select report (1-5): ")
            
            if report_choice == "1":
                # Inventory Summary
                print(f"\n📋 INVENTORY SUMMARY REPORT")
                print("=" * 50)
                
                total_products = len(inventory)
                total_stock_units = sum(p['stock'] for p in inventory.values())
                total_inventory_value = sum(p['price'] * p['stock'] for p in inventory.values())
                avg_product_price = sum(p['price'] for p in inventory.values()) / total_products
                
                out_of_stock = sum(1 for p in inventory.values() if p['stock'] == 0)
                low_stock = sum(1 for p in inventory.values() if 0 < p['stock'] <= p['min_stock'])
                in_stock = total_products - out_of_stock - low_stock
                
                print(f"Total Products: {total_products}")
                print(f"Total Stock Units: {total_stock_units:,}")
                print(f"Total Inventory Value: ₹{total_inventory_value:,.2f}")
                print(f"Average Product Price: ₹{avg_product_price:,.2f}")
                print(f"\nStock Status:")
                print(f"  In Stock: {in_stock} ({in_stock/total_products*100:.1f}%)")
                print(f"  Low Stock: {low_stock} ({low_stock/total_products*100:.1f}%)")
                print(f"  Out of Stock: {out_of_stock} ({out_of_stock/total_products*100:.1f}%)")
                
            elif report_choice == "2":
                # Category Analysis
                print(f"\n📈 CATEGORY ANALYSIS REPORT")
                print("=" * 50)
                
                category_stats = {}
                for product in inventory.values():
                    category = product['category']
                    if category not in category_stats:
                        category_stats[category] = {
                            'count': 0,
                            'total_stock': 0,
                            'total_value': 0,
                            'avg_price': 0
                        }
                    
                    category_stats[category]['count'] += 1
                    category_stats[category]['total_stock'] += product['stock']
                    category_stats[category]['total_value'] += product['price'] * product['stock']
                
                # Calculate averages
                for category, stats in category_stats.items():
                    category_products = [p for p in inventory.values() if p['category'] == category]
                    stats['avg_price'] = sum(p['price'] for p in category_products) / len(category_products)
                
                print(f"{'Category':<15} {'Products':<10} {'Stock':<10} {'Value':<15} {'Avg Price'}")
                print("-" * 65)
                for category, stats in category_stats.items():
                    print(f"{category[:14]:<15} {stats['count']:<10} {stats['total_stock']:<10} "
                          f"₹{stats['total_value']:<14,.0f} ₹{stats['avg_price']:<10,.0f}")
                
            elif report_choice == "3":
                # Stock Value Report
                print(f"\n💰 STOCK VALUE REPORT")
                print("=" * 60)
                
                # Sort products by total value (price * stock)
                products_by_value = [(pid, p, p['price'] * p['stock']) 
                                   for pid, p in inventory.items()]
                products_by_value.sort(key=lambda x: x[2], reverse=True)
                
                print(f"{'Rank':<5} {'ID':<8} {'Name':<20} {'Stock':<8} {'Unit Price':<12} {'Total Value'}")
                print("-" * 75)
                
                for i, (product_id, product, total_value) in enumerate(products_by_value[:10], 1):
                    print(f"{i:<5} {product_id:<8} {product['name'][:19]:<20} {product['stock']:<8} "
                          f"₹{product['price']:<11,.0f} ₹{total_value:,.0f}")
                
                if len(products_by_value) > 10:
                    print(f"\n... and {len(products_by_value) - 10} more products")
                
            elif report_choice == "4":
                # Transaction Log
                if not transaction_log:
                    print("\n📋 No transactions recorded!")
                    continue
                
                print(f"\n📝 TRANSACTION LOG")
                print("=" * 80)
                
                # Show last 20 transactions
                recent_transactions = transaction_log[-20:]
                
                print(f"{'Date':<12} {'Type':<15} {'Product ID':<10} {'Details'}")
                print("-" * 80)
                
                for transaction in reversed(recent_transactions):
                    date_str = transaction['date'].strftime('%d/%m/%Y')
                    details = transaction['details'][:40] + "..." if len(transaction['details']) > 40 else transaction['details']
                    print(f"{date_str:<12} {transaction['type']:<15} {transaction['product_id']:<10} {details}")
                
                if len(transaction_log) > 20:
                    print(f"\nShowing last 20 transactions. Total transactions: {len(transaction_log)}")
                
            elif report_choice == "5":
                # Top Products by Value
                print(f"\n🏆 TOP PRODUCTS BY VALUE")
                print("=" * 50)
                
                # Sort by total value
                top_products = sorted(
                    [(pid, p) for pid, p in inventory.items()],
                    key=lambda x: x[1]['price'] * x[1]['stock'],
                    reverse=True
                )
                
                print(f"{'Rank':<5} {'Product':<25} {'Total Value':<15} {'Stock'}")
                print("-" * 60)
                
                for i, (product_id, product) in enumerate(top_products[:10], 1):
                    total_value = product['price'] * product['stock']
                    product_name = f"{product['name']} ({product_id})"
                    print(f"{i:<5} {product_name[:24]:<25} ₹{total_value:>14,.0f} {product['stock']:>8}")
        
        elif choice == "8":
            # Low Stock Alerts
            print(f"\n⚠️ LOW STOCK ALERTS")
            print("=" * 40)
            
            # Find products with low stock
            alerts = []
            
            for product_id, product in inventory.items():
                if product['stock'] == 0:
                    alerts.append((product_id, product, "OUT OF STOCK", "🔴"))
                elif product['stock'] <= product['min_stock']:
                    alerts.append((product_id, product, "LOW STOCK", "🟡"))
            
            if not alerts:
                print("✅ All products are adequately stocked!")
                continue
            
            print(f"Found {len(alerts)} products needing attention:")
            print(f"\n{'Status':<6} {'ID':<8} {'Name':<20} {'Current':<8} {'Minimum':<8} {'Action Needed'}")
            print("-" * 70)
            
            for product_id, product, status, icon in alerts:
                action = "RESTOCK IMMEDIATELY" if status == "OUT OF STOCK" else "Restock Soon"
                print(f"{icon:<6} {product_id:<8} {product['name'][:19]:<20} "
                      f"{product['stock']:<8} {product['min_stock']:<8} {action}")
            
            # Restock suggestion
            print(f"\n💡 RESTOCK SUGGESTIONS:")
            for product_id, product, status, icon in alerts:
                if status == "OUT OF STOCK":
                    suggested_qty = product['min_stock'] * 2
                else:
                    suggested_qty = product['min_stock'] * 2 - product['stock']
                
                restock_cost = suggested_qty * product['price']
                print(f"  {product['name']}: Order {suggested_qty} units (Cost: ₹{restock_cost:,.0f})")
        
        elif choice == "9":
            # Category Management
            print(f"\n📂 CATEGORY MANAGEMENT")
            print("-" * 30)
            print("1. View All Categories")
            print("2. Add New Category")
            print("3. Rename Category")
            print("4. Delete Category")
            print("5. Category Statistics")
            
            cat_choice = input("Select option (1-5): ")
            
            if cat_choice == "1":
                # View All Categories
                used_categories = list(set(p['category'] for p in inventory.values()))
                
                print(f"\n📂 ALL CATEGORIES")
                print("-" * 40)
                print(f"Available Categories ({len(categories)}):")
                for i, category in enumerate(categories, 1):
                    status = "✅ Used" if category in used_categories else "❌ Unused"
                    print(f"{i:>2}. {category:<20} {status}")
                
            elif cat_choice == "2":
                # Add New Category
                new_category = input("Enter new category name: ")
                if new_category.strip() and new_category not in categories:
                    categories.append(new_category)
                    print(f"✅ Category '{new_category}' added successfully!")
                elif new_category in categories:
                    print("❌ Category already exists!")
                else:
                    print("❌ Category name cannot be empty!")
                    
            elif cat_choice == "3":
                # Rename Category
                if not categories:
                    print("No categories to rename!")
                    continue
                
                print("Select category to rename:")
                for i, category in enumerate(categories, 1):
                    print(f"{i}. {category}")
                
                try:
                    cat_index = int(input(f"Select category (1-{len(categories)}): ")) - 1
                    if 0 <= cat_index < len(categories):
                        old_name = categories[cat_index]
                        new_name = input(f"Enter new name for '{old_name}': ")
                        
                        if new_name.strip() and new_name not in categories:
                            # Update category in products
                            for product in inventory.values():
                                if product['category'] == old_name:
                                    product['category'] = new_name
                            
                            categories[cat_index] = new_name
                            print(f"✅ Category renamed from '{old_name}' to '{new_name}'!")
                        else:
                            print("❌ Invalid new name!")
                    else:
                        print("Invalid selection!")
                except ValueError:
                    print("Please enter a valid number!")
            
            elif cat_choice == "4":
                # Delete Category
                used_categories = [p['category'] for p in inventory.values()]
                
                print("Categories that can be deleted (not used by any product):")
                deletable = [cat for cat in categories if cat not in used_categories]
                
                if not deletable:
                    print("No categories can be deleted (all are in use)!")
                    continue
                
                for i, category in enumerate(deletable, 1):
                    print(f"{i}. {category}")
                
                try:
                    del_choice = int(input(f"Select category to delete (1-{len(deletable)}): ")) - 1
                    if 0 <= del_choice < len(deletable):
                        category_to_delete = deletable[del_choice]
                        categories.remove(category_to_delete)
                        print(f"✅ Category '{category_to_delete}' deleted!")
                    else:
                        print("Invalid selection!")
                except ValueError:
                    print("Please enter a valid number!")
            
            elif cat_choice == "5":
                # Category Statistics
                print(f"\n📊 CATEGORY STATISTICS")
                print("=" * 50)
                
                category_data = {}
                for product in inventory.values():
                    cat = product['category']
                    if cat not in category_data:
                        category_data[cat] = {
                            'products': 0,
                            'total_stock': 0,
                            'total_value': 0,
                            'out_of_stock': 0,
                            'low_stock': 0
                        }
                    
                    category_data[cat]['products'] += 1
                    category_data[cat]['total_stock'] += product['stock']
                    category_data[cat]['total_value'] += product['price'] * product['stock']
                    
                    if product['stock'] == 0:
                        category_data[cat]['out_of_stock'] += 1
                    elif product['stock'] <= product['min_stock']:
                        category_data[cat]['low_stock'] += 1
                
                print(f"{'Category':<15} {'Products':<10} {'Stock':<8} {'Value':<12} {'Issues'}")
                print("-" * 60)
                
                for category, data in category_data.items():
                    issues = data['out_of_stock'] + data['low_stock']
                    print(f"{category[:14]:<15} {data['products']:<10} {data['total_stock']:<8} "
                          f"₹{data['total_value']:<11,.0f} {issues}")
        
        elif choice == "10":
            # Exit
            print(f"\n📦 INVENTORY MANAGEMENT SUMMARY")
            print("=" * 50)
            print("Thank you for using StoreMax Inventory Management!")
            
            if inventory:
                print(f"\nSession Summary:")
                print(f"• Managed {len(inventory)} products")
                print(f"• Total inventory value: ₹{sum(p['price'] * p['stock'] for p in inventory.values()):,.0f}")
                print(f"• Transactions logged: {len(transaction_log)}")
                print(f"• Categories used: {len(set(p['category'] for p in inventory.values()))}")
                
                # Final alerts
                out_of_stock = sum(1 for p in inventory.values() if p['stock'] == 0)
                low_stock = sum(1 for p in inventory.values() if 0 < p['stock'] <= p['min_stock'])
                
                if out_of_stock > 0:
                    print(f"⚠️ {out_of_stock} products are out of stock!")
                if low_stock > 0:
                    print(f"⚠️ {low_stock} products have low stock!")
            
            print("\n🚀 Keep your inventory organized and profitable!")
            break
        
        else:
            print("❌ Invalid choice! Please select 1-10.")

if __name__ == "__main__":
    main() 