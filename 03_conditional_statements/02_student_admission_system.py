"""
Student Admission System
A practical program for college admission based on multiple criteria.
Demonstrates: Complex conditional statements, logical operators, nested if-else
"""

def main():
    print("=" * 60)
    print("        COLLEGE ADMISSION SYSTEM")
    print("=" * 60)
    
    print("Welcome to Tech University Admission Portal")
    print("Please provide the following information for admission evaluation:")
    print("-" * 60)
    
    # Get student information
    student_name = input("Enter student name: ")
    student_id = input("Enter application ID: ")
    
    # Get academic scores
    print("\nAcademic Information:")
    try:
        tenth_percentage = float(input("10th grade percentage: "))
        twelfth_percentage = float(input("12th grade percentage: "))
        entrance_score = float(input("Entrance exam score (out of 100): "))
        
        # Validate scores
        if not (0 <= tenth_percentage <= 100):
            print("10th grade percentage must be between 0-100")
            return
        if not (0 <= twelfth_percentage <= 100):
            print("12th grade percentage must be between 0-100")
            return
        if not (0 <= entrance_score <= 100):
            print("Entrance exam score must be between 0-100")
            return
            
    except ValueError:
        print("Please enter valid numeric scores!")
        return
    
    # Get course preference
    print("\nAvailable Courses:")
    print("1. Computer Science Engineering")
    print("2. Information Technology")
    print("3. Electronics Engineering")
    print("4. Mechanical Engineering")
    print("5. Civil Engineering")
    
    while True:
        try:
            course_choice = int(input("Select course (1-5): "))
            if 1 <= course_choice <= 5:
                break
            else:
                print("Please select a valid course (1-5)")
        except ValueError:
            print("Please enter a valid number")
    
    courses = {
        1: "Computer Science Engineering",
        2: "Information Technology", 
        3: "Electronics Engineering",
        4: "Mechanical Engineering",
        5: "Civil Engineering"
    }
    selected_course = courses[course_choice]
    
    # Get category information
    print("\nCategory Information:")
    print("1. General")
    print("2. OBC")
    print("3. SC/ST")
    print("4. EWS")
    
    while True:
        try:
            category_choice = int(input("Select category (1-4): "))
            if 1 <= category_choice <= 4:
                break
            else:
                print("Please select a valid category (1-4)")
        except ValueError:
            print("Please enter a valid number")
    
    categories = {1: "General", 2: "OBC", 3: "SC/ST", 4: "EWS"}
    category = categories[category_choice]
    
    # Additional information
    sports_quota = input("Are you applying under sports quota? (y/n): ").lower() == 'y'
    ncc_background = input("Do you have NCC background? (y/n): ").lower() == 'y'
    
    # Define cutoff criteria for different courses and categories
    cutoffs = {
        "Computer Science Engineering": {"General": 85, "OBC": 80, "SC/ST": 75, "EWS": 82},
        "Information Technology": {"General": 82, "OBC": 77, "SC/ST": 72, "EWS": 79},
        "Electronics Engineering": {"General": 80, "OBC": 75, "SC/ST": 70, "EWS": 77},
        "Mechanical Engineering": {"General": 78, "OBC": 73, "SC/ST": 68, "EWS": 75},
        "Civil Engineering": {"General": 75, "OBC": 70, "SC/ST": 65, "EWS": 72}
    }
    
    # Calculate composite score
    composite_score = (tenth_percentage * 0.2) + (twelfth_percentage * 0.3) + (entrance_score * 0.5)
    
    # Add bonus points
    bonus_points = 0
    if sports_quota:
        bonus_points += 5
    if ncc_background:
        bonus_points += 3
    
    final_score = composite_score + bonus_points
    required_cutoff = cutoffs[selected_course][category]
    
    # Determine admission status
    print("\n" + "=" * 60)
    print("              ADMISSION RESULT")
    print("=" * 60)
    print(f"Student Name: {student_name}")
    print(f"Application ID: {student_id}")
    print(f"Course Applied: {selected_course}")
    print(f"Category: {category}")
    print("-" * 60)
    
    print("SCORE BREAKDOWN:")
    print(f"10th Grade (20%): {tenth_percentage:.1f} → {tenth_percentage * 0.2:.1f}")
    print(f"12th Grade (30%): {twelfth_percentage:.1f} → {twelfth_percentage * 0.3:.1f}")
    print(f"Entrance Exam (50%): {entrance_score:.1f} → {entrance_score * 0.5:.1f}")
    print(f"Composite Score: {composite_score:.2f}")
    
    if bonus_points > 0:
        print(f"Bonus Points: +{bonus_points}")
        if sports_quota:
            print("  • Sports Quota: +5")
        if ncc_background:
            print("  • NCC Background: +3")
    
    print(f"Final Score: {final_score:.2f}")
    print(f"Required Cutoff: {required_cutoff}")
    print("-" * 60)
    
    # Admission decision with detailed conditions
    if final_score >= required_cutoff:
        if final_score >= required_cutoff + 10:
            admission_status = "CONFIRMED"
            merit_position = "Merit List - Top 10%"
            scholarship_eligible = True
        elif final_score >= required_cutoff + 5:
            admission_status = "CONFIRMED"
            merit_position = "Merit List - Top 25%"
            scholarship_eligible = True
        else:
            admission_status = "CONFIRMED"
            merit_position = "Merit List"
            scholarship_eligible = False
        
        print("🎉 CONGRATULATIONS! 🎉")
        print(f"Status: {admission_status}")
        print(f"Merit Position: {merit_position}")
        
        if scholarship_eligible:
            print("🏆 You are eligible for merit scholarship!")
            if final_score >= required_cutoff + 10:
                scholarship_amount = 50000
            else:
                scholarship_amount = 25000
            print(f"Scholarship Amount: ₹{scholarship_amount:,} per year")
        
        # Fee structure
        base_fee = 100000
        if category in ["SC/ST"]:
            fee_discount = 0.5
        elif category in ["OBC", "EWS"]:
            fee_discount = 0.3
        else:
            fee_discount = 0.0
        
        discounted_fee = base_fee * (1 - fee_discount)
        if scholarship_eligible:
            final_fee = max(0, discounted_fee - scholarship_amount)
        else:
            final_fee = discounted_fee
        
        print(f"\nFEE STRUCTURE:")
        print(f"Base Fee: ₹{base_fee:,}")
        if fee_discount > 0:
            print(f"Category Discount ({category}): {fee_discount*100}%")
            print(f"After Discount: ₹{discounted_fee:,}")
        if scholarship_eligible:
            print(f"Scholarship: -₹{scholarship_amount:,}")
        print(f"Final Annual Fee: ₹{final_fee:,}")
        
    elif final_score >= required_cutoff - 5:
        print("⏳ WAITLISTED")
        print("Status: You are on the waiting list")
        print("Position: Will be updated after first round of admissions")
        print("Action Required: Wait for further communication")
        
    else:
        print("❌ NOT QUALIFIED")
        print("Status: Did not meet the minimum cutoff")
        print(f"Shortfall: {required_cutoff - final_score:.2f} points")
        
        # Suggest improvements
        print("\nSUGGESTIONS FOR NEXT ATTEMPT:")
        if entrance_score < 70:
            print("• Focus on improving entrance exam score")
        if twelfth_percentage < 80:
            print("• Consider improving 12th grade scores if retaking")
        if not sports_quota and not ncc_background:
            print("• Consider sports or NCC participation for bonus points")
        print("• Apply for courses with lower cutoffs")
    
    # Next steps
    print("\n" + "=" * 60)
    print("              NEXT STEPS")
    print("=" * 60)
    
    if final_score >= required_cutoff:
        print("1. Check your email for admission confirmation")
        print("2. Complete document verification by DD/MM/YYYY")
        print("3. Pay the admission fee to confirm your seat")
        print("4. Attend orientation program")
    elif final_score >= required_cutoff - 5:
        print("1. Monitor the admission portal regularly")
        print("2. Keep all documents ready")
        print("3. Wait for waitlist updates")
    else:
        print("1. Consider other universities/courses")
        print("2. Prepare for next year's entrance exam")
        print("3. Explore alternate career paths")
    
    print("\nFor queries, contact: admissions@techuniversity.edu")
    print("Phone: +91-XXXX-XXXXXX")

if __name__ == "__main__":
    main() 