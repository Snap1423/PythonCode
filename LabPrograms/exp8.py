# Program to check voting eligibility and gender using nested if
age = int(input("Enter your age: "))
gender = input("Enter your gender (M/F): ")

if age >= 18:
    if gender.upper() == 'M':
        print("You are eligible to vote and you are Male")
    elif gender.upper() == 'F':
        print("You are eligible to vote and you are Female") 
    else:
        print("Invalid gender entered")
else:
    if gender.upper() == 'M':
        print("You are not eligible to vote and you are Male")
    elif gender.upper() == 'F':
        print("You are not eligible to vote and you are Female")
    else:
        print("Invalid gender entered")
