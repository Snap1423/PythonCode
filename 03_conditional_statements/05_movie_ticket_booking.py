"""
Movie Ticket Booking System
A practical program for booking movie tickets with dynamic pricing and seat selection.
Demonstrates: Complex conditional statements, pricing logic, validation
"""

def main():
    print("=" * 65)
    print("             CINEMAX TICKET BOOKING SYSTEM")
    print("=" * 65)
    
    # Initialize movie data
    movies = {
        1: {
            "title": "Avengers: Endgame",
            "genre": "Action/Sci-Fi",
            "duration": "181 min",
            "rating": "PG-13",
            "language": "English"
        },
        2: {
            "title": "RRR",
            "genre": "Action/Drama",
            "duration": "187 min", 
            "rating": "PG-13",
            "language": "Telugu/Hindi"
        },
        3: {
            "title": "Spider-Man: No Way Home",
            "genre": "Action/Adventure",
            "duration": "148 min",
            "rating": "PG-13",
            "language": "English"
        },
        4: {
            "title": "Dangal",
            "genre": "Biography/Sport",
            "duration": "161 min",
            "rating": "PG",
            "language": "Hindi"
        }
    }
    
    # Show timings and pricing
    showtimes = {
        "Morning": {"time": "10:00 AM", "price_multiplier": 0.8},
        "Matinee": {"time": "1:00 PM", "price_multiplier": 0.9},
        "Evening": {"time": "6:00 PM", "price_multiplier": 1.0},
        "Night": {"time": "9:00 PM", "price_multiplier": 1.2}
    }
    
    # Seat categories
    seat_categories = {
        "Platinum": {"base_price": 400, "rows": ["A", "B"], "total_seats": 20},
        "Gold": {"base_price": 300, "rows": ["C", "D", "E"], "total_seats": 30},
        "Silver": {"base_price": 200, "rows": ["F", "G", "H", "I"], "total_seats": 40}
    }
    
    print("🎬 Welcome to CineMax - Your Ultimate Movie Experience!")
    print("📍 Location: City Mall, Downtown")
    print("-" * 65)
    
    # Customer information
    customer_name = input("Enter your name: ")
    phone = input("Enter your phone number: ")
    
    # Validate phone number
    if not (phone.isdigit() and len(phone) == 10):
        print("Please enter a valid 10-digit phone number")
        return
    
    # Show available movies
    print("\n" + "🎬" * 20)
    print("              MOVIES NOW SHOWING")
    print("🎬" * 20)
    
    for movie_id, movie_info in movies.items():
        print(f"{movie_id}. {movie_info['title']}")
        print(f"   Genre: {movie_info['genre']}")
        print(f"   Duration: {movie_info['duration']}")
        print(f"   Rating: {movie_info['rating']}")
        print(f"   Language: {movie_info['language']}")
        print("-" * 45)
    
    # Movie selection
    while True:
        try:
            movie_choice = int(input("Select movie (1-4): "))
            if movie_choice in movies:
                selected_movie = movies[movie_choice]
                break
            else:
                print("Please select a valid movie (1-4)")
        except ValueError:
            print("Please enter a valid number")
    
    print(f"\n✅ Selected: {selected_movie['title']}")
    
    # Date selection
    print("\nAvailable Dates:")
    print("1. Today")
    print("2. Tomorrow") 
    print("3. Day after tomorrow")
    
    while True:
        try:
            date_choice = int(input("Select date (1-3): "))
            if 1 <= date_choice <= 3:
                dates = ["Today", "Tomorrow", "Day after tomorrow"]
                selected_date = dates[date_choice - 1]
                break
            else:
                print("Please select 1-3")
        except ValueError:
            print("Please enter a valid number")
    
    # Show timing selection
    print(f"\n⏰ Show Timings for {selected_date}:")
    print("-" * 40)
    
    timing_options = list(showtimes.keys())
    for i, timing in enumerate(timing_options):
        price_mult = showtimes[timing]["price_multiplier"]
        time = showtimes[timing]["time"]
        discount_info = ""
        
        if price_mult < 1.0:
            discount = int((1.0 - price_mult) * 100)
            discount_info = f" ({discount}% OFF)"
        elif price_mult > 1.0:
            premium = int((price_mult - 1.0) * 100)
            discount_info = f" (+{premium}% Premium)"
        
        print(f"{i+1}. {timing} Show - {time}{discount_info}")
    
    while True:
        try:
            timing_choice = int(input("Select show timing (1-4): ")) - 1
            if 0 <= timing_choice < len(timing_options):
                selected_timing = timing_options[timing_choice]
                timing_info = showtimes[selected_timing]
                break
            else:
                print("Please select a valid timing")
        except ValueError:
            print("Please enter a valid number")
    
    print(f"✅ Selected: {selected_timing} Show - {timing_info['time']}")
    
    # Seat category selection
    print(f"\n🎟️  SEAT CATEGORIES & PRICING:")
    print("-" * 50)
    
    category_options = list(seat_categories.keys())
    for i, category in enumerate(category_options):
        base_price = seat_categories[category]["base_price"]
        final_price = int(base_price * timing_info["price_multiplier"])
        rows = ", ".join(seat_categories[category]["rows"])
        
        print(f"{i+1}. {category} - ₹{final_price}")
        print(f"   Rows: {rows}")
        print(f"   Features: {'Premium recliner, extra legroom' if category == 'Platinum' else 'Comfortable seating' if category == 'Gold' else 'Standard seating'}")
        print()
    
    while True:
        try:
            category_choice = int(input("Select seat category (1-3): ")) - 1
            if 0 <= category_choice < len(category_options):
                selected_category = category_options[category_choice]
                category_info = seat_categories[selected_category]
                break
            else:
                print("Please select a valid category")
        except ValueError:
            print("Please enter a valid number")
    
    # Calculate base ticket price
    base_price = category_info["base_price"]
    ticket_price = int(base_price * timing_info["price_multiplier"])
    
    print(f"✅ Selected: {selected_category} - ₹{ticket_price} per ticket")
    
    # Number of tickets
    while True:
        try:
            num_tickets = int(input("Number of tickets (1-10): "))
            if 1 <= num_tickets <= 10:
                break
            else:
                print("You can book 1-10 tickets at a time")
        except ValueError:
            print("Please enter a valid number")
    
    # Age group selection for pricing
    age_groups = []
    age_discounts = {
        "Child": 0.5,    # 50% discount
        "Adult": 1.0,    # No discount
        "Senior": 0.7    # 30% discount
    }
    
    print(f"\nAge Group Selection (for {num_tickets} tickets):")
    print("1. Child (2-12 years) - 50% discount")
    print("2. Adult (13-59 years) - Regular price")  
    print("3. Senior (60+ years) - 30% discount")
    
    total_amount = 0
    ticket_details = []
    
    for i in range(num_tickets):
        print(f"\nTicket {i+1}:")
        while True:
            try:
                age_choice = int(input("Select age group (1-3): "))
                if age_choice == 1:
                    age_group = "Child"
                elif age_choice == 2:
                    age_group = "Adult"
                elif age_choice == 3:
                    age_group = "Senior"
                else:
                    print("Please select 1-3")
                    continue
                break
            except ValueError:
                print("Please enter a valid number")
        
        # Calculate ticket price with age discount
        discounted_price = int(ticket_price * age_discounts[age_group])
        total_amount += discounted_price
        
        ticket_details.append({
            "ticket_num": i+1,
            "age_group": age_group,
            "price": discounted_price
        })
        
        print(f"✅ Ticket {i+1}: {age_group} - ₹{discounted_price}")
    
    # Additional charges and discounts
    print(f"\n💰 PRICING BREAKDOWN:")
    print("-" * 40)
    
    subtotal = total_amount
    print(f"Subtotal: ₹{subtotal}")
    
    # Service charges
    service_charge = int(subtotal * 0.02)  # 2% service charge
    print(f"Service Charge (2%): ₹{service_charge}")
    
    # GST
    gst = int((subtotal + service_charge) * 0.18)  # 18% GST
    print(f"GST (18%): ₹{gst}")
    
    # Convenience fee
    convenience_fee = num_tickets * 15  # ₹15 per ticket
    print(f"Convenience Fee: ₹{convenience_fee}")
    
    gross_total = subtotal + service_charge + gst + convenience_fee
    
    # Apply discounts based on conditions
    discount_amount = 0
    applied_discounts = []
    
    # Weekend discount check
    if selected_date == "Today":  # Assuming today is weekend for demo
        if selected_timing in ["Morning", "Matinee"]:
            weekend_discount = int(subtotal * 0.1)  # 10% weekend discount
            discount_amount += weekend_discount
            applied_discounts.append(f"Weekend Morning/Matinee Discount (10%): -₹{weekend_discount}")
    
    # Group booking discount
    if num_tickets >= 5:
        group_discount = int(subtotal * 0.05)  # 5% group discount
        discount_amount += group_discount
        applied_discounts.append(f"Group Booking Discount (5%): -₹{group_discount}")
    
    # First-time customer discount (simulate)
    import random
    if random.choice([True, False]):  # 50% chance
        first_time_discount = 50
        discount_amount += first_time_discount
        applied_discounts.append(f"First Time Customer Discount: -₹{first_time_discount}")
    
    # Student discount option
    student_discount_option = input("\nAre you a student? (y/n): ").lower()
    if student_discount_option == 'y':
        student_id = input("Enter student ID: ")
        if student_id.strip():  # If student ID provided
            student_discount = int(subtotal * 0.15)  # 15% student discount
            discount_amount += student_discount
            applied_discounts.append(f"Student Discount (15%): -₹{student_discount}")
    
    final_total = gross_total - discount_amount
    
    # Show discounts
    if applied_discounts:
        print(f"\n🎉 APPLIED DISCOUNTS:")
        for discount in applied_discounts:
            print(f"   {discount}")
        print(f"Total Discount: -₹{discount_amount}")
    
    print(f"\nGross Total: ₹{gross_total}")
    print(f"Total Savings: -₹{discount_amount}")
    print("=" * 40)
    print(f"FINAL AMOUNT: ₹{final_total}")
    print("=" * 40)
    
    # Payment method selection
    print(f"\n💳 PAYMENT METHODS:")
    print("1. Credit/Debit Card")
    print("2. UPI/Digital Wallet") 
    print("3. Net Banking")
    print("4. Pay at Counter")
    
    payment_methods = {
        1: "Credit/Debit Card",
        2: "UPI/Digital Wallet",
        3: "Net Banking", 
        4: "Pay at Counter"
    }
    
    while True:
        try:
            payment_choice = int(input("Select payment method (1-4): "))
            if payment_choice in payment_methods:
                payment_method = payment_methods[payment_choice]
                break
            else:
                print("Please select a valid payment method")
        except ValueError:
            print("Please enter a valid number")
    
    # Additional payment processing
    processing_fee = 0
    if payment_choice in [1, 2, 3]:  # Online payment methods
        processing_fee = 10  # Online processing fee
        final_total += processing_fee
        print(f"Online Processing Fee: ₹{processing_fee}")
        print(f"Updated Final Amount: ₹{final_total}")
    
    # Confirmation
    print(f"\n" + "=" * 65)
    print("                  BOOKING CONFIRMATION")
    print("=" * 65)
    
    confirmation = input("Confirm booking? (y/n): ").lower()
    
    if confirmation == 'y':
        # Generate booking ID
        import random
        booking_id = f"CMX{random.randint(100000, 999999)}"
        
        print(f"\n🎉 BOOKING SUCCESSFUL!")
        print("=" * 50)
        print(f"Booking ID: {booking_id}")
        print(f"Customer: {customer_name}")
        print(f"Phone: {phone}")
        print("-" * 50)
        print(f"Movie: {selected_movie['title']}")
        print(f"Date: {selected_date}")
        print(f"Show: {selected_timing} - {timing_info['time']}")
        print(f"Seat Category: {selected_category}")
        print(f"Number of Tickets: {num_tickets}")
        print("-" * 50)
        
        print("TICKET DETAILS:")
        for ticket in ticket_details:
            print(f"  Ticket {ticket['ticket_num']}: {ticket['age_group']} - ₹{ticket['price']}")
        
        print("-" * 50)
        print(f"Total Amount Paid: ₹{final_total}")
        print(f"Payment Method: {payment_method}")
        print("=" * 50)
        
        print(f"\n📱 IMPORTANT INFORMATION:")
        print(f"• Arrive 30 minutes before show time")
        print(f"• Carry valid ID proof")
        print(f"• No outside food/drinks allowed")
        print(f"• Mobile tickets will be sent to {phone}")
        
        if payment_choice == 4:
            print(f"• Pay ₹{final_total} at the counter before show time")
        
        print(f"\n🎬 Enjoy your movie!")
        print(f"Thank you for choosing CineMax!")
        
    else:
        print(f"\n❌ Booking cancelled")
        print(f"Thank you for visiting CineMax!")

if __name__ == "__main__":
    main() 