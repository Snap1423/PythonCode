"""
Student Grade Calculator
A practical program to calculate student grades based on marks in different subjects.
Demonstrates: Input/Output, Datatypes, Operators, Type casting
"""

def main():
    print("=" * 50)
    print("          STUDENT GRADE CALCULATOR")
    print("=" * 50)
    
    # Get student information
    student_name = input("Enter student name: ")
    student_id = input("Enter student ID: ")
    
    # Get marks for different subjects
    print("\nEnter marks for 5 subjects (out of 100):")
    
    subjects = ["Mathematics", "Science", "English", "Social Studies", "Computer Science"]
    marks = []
    total_marks = 0
    
    for subject in subjects:
        while True:
            try:
                mark = float(input(f"{subject}: "))
                if 0 <= mark <= 100:
                    marks.append(mark)
                    total_marks += mark
                    break
                else:
                    print("Please enter marks between 0 and 100")
            except ValueError:
                print("Please enter a valid number")
    
    # Calculate percentage and grade
    percentage = total_marks / len(subjects)
    
    # Determine grade using conditional operators
    if percentage >= 90:
        grade = "A+"
        remark = "Excellent"
    elif percentage >= 80:
        grade = "A"
        remark = "Very Good"
    elif percentage >= 70:
        grade = "B+"
        remark = "Good"
    elif percentage >= 60:
        grade = "B"
        remark = "Satisfactory"
    elif percentage >= 50:
        grade = "C"
        remark = "Average"
    else:
        grade = "F"
        remark = "Fail"
    
    # Display results with formatted output
    print("\n" + "=" * 50)
    print("                GRADE REPORT")
    print("=" * 50)
    print(f"Student Name: {student_name}")
    print(f"Student ID: {student_id}")
    print("-" * 50)
    
    for i, subject in enumerate(subjects):
        print(f"{subject:<20}: {marks[i]:>6.1f}")
    
    print("-" * 50)
    print(f"{'Total Marks':<20}: {total_marks:>6.1f}/{len(subjects) * 100}")
    print(f"{'Percentage':<20}: {percentage:>6.2f}%")
    print(f"{'Grade':<20}: {grade:>6}")
    print(f"{'Remark':<20}: {remark:>6}")
    print("=" * 50)

if __name__ == "__main__":
    main() 