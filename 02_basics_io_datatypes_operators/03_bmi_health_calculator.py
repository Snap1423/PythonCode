"""
BMI Health Calculator
A practical program to calculate Body Mass Index and provide health recommendations.
Demonstrates: Mathematical operators, Type casting, Boolean operations, Formatted output
"""

import math

def main():
    print("=" * 55)
    print("            BMI HEALTH CALCULATOR")
    print("=" * 55)
    
    # Get user information
    name = input("Enter your name: ")
    age = int(input("Enter your age: "))
    gender = input("Enter your gender (M/F): ").upper()
    
    # Get measurements
    print("\nChoose measurement system:")
    print("1. Metric (kg, cm)")
    print("2. Imperial (lbs, inches)")
    
    choice = input("Enter choice (1 or 2): ")
    
    if choice == "1":
        weight = float(input("Enter your weight in kg: "))
        height_cm = float(input("Enter your height in cm: "))
        height_m = height_cm / 100
    else:
        weight_lbs = float(input("Enter your weight in lbs: "))
        height_inches = float(input("Enter your height in inches: "))
        # Convert to metric
        weight = weight_lbs * 0.453592
        height_m = height_inches * 0.0254
    
    # Calculate BMI
    bmi = weight / (height_m ** 2)
    
    # Determine BMI category
    if bmi < 18.5:
        category = "Underweight"
        color_code = "🔵"
        health_risk = "Low"
    elif 18.5 <= bmi < 25:
        category = "Normal weight"
        color_code = "🟢"
        health_risk = "Low"
    elif 25 <= bmi < 30:
        category = "Overweight"
        color_code = "🟡"
        health_risk = "Moderate"
    elif 30 <= bmi < 35:
        category = "Obesity Class I"
        color_code = "🟠"
        health_risk = "High"
    elif 35 <= bmi < 40:
        category = "Obesity Class II"
        color_code = "🔴"
        health_risk = "Very High"
    else:
        category = "Obesity Class III"
        color_code = "⚫"
        health_risk = "Extremely High"
    
    # Calculate ideal weight range
    ideal_bmi_min = 18.5
    ideal_bmi_max = 24.9
    ideal_weight_min = ideal_bmi_min * (height_m ** 2)
    ideal_weight_max = ideal_bmi_max * (height_m ** 2)
    
    # Calculate calories needed (basic estimation)
    if gender == "M":
        bmr = 88.362 + (13.397 * weight) + (4.799 * height_cm) - (5.677 * age)
    else:
        bmr = 447.593 + (9.247 * weight) + (3.098 * height_cm) - (4.330 * age)
    
    calories_sedentary = bmr * 1.2
    calories_moderate = bmr * 1.55
    calories_active = bmr * 1.9
    
    # Display results
    print("\n" + "=" * 55)
    print("                 HEALTH REPORT")
    print("=" * 55)
    print(f"Name: {name}")
    print(f"Age: {age} years")
    print(f"Gender: {'Male' if gender == 'M' else 'Female'}")
    print(f"Weight: {weight:.1f} kg")
    print(f"Height: {height_m:.2f} m")
    print("-" * 55)
    print(f"BMI: {bmi:.2f}")
    print(f"Category: {color_code} {category}")
    print(f"Health Risk: {health_risk}")
    print("-" * 55)
    print(f"Ideal Weight Range: {ideal_weight_min:.1f} - {ideal_weight_max:.1f} kg")
    
    weight_difference = weight - ((ideal_weight_min + ideal_weight_max) / 2)
    if weight_difference > 0:
        print(f"Weight to lose: {weight_difference:.1f} kg")
    elif weight_difference < 0:
        print(f"Weight to gain: {abs(weight_difference):.1f} kg")
    else:
        print("You are at ideal weight!")
    
    print("-" * 55)
    print("DAILY CALORIE NEEDS:")
    print(f"Sedentary (little/no exercise): {calories_sedentary:.0f} calories")
    print(f"Moderate (3-5 days/week): {calories_moderate:.0f} calories")
    print(f"Active (6-7 days/week): {calories_active:.0f} calories")
    
    # Health recommendations
    print("\n" + "=" * 55)
    print("              RECOMMENDATIONS")
    print("=" * 55)
    
    if bmi < 18.5:
        print("• Increase caloric intake with healthy foods")
        print("• Include protein-rich foods in your diet")
        print("• Consider strength training exercises")
        print("• Consult with a nutritionist")
    elif 18.5 <= bmi < 25:
        print("• Maintain your current healthy lifestyle")
        print("• Continue regular exercise")
        print("• Eat a balanced diet")
        print("• Stay hydrated")
    else:
        print("• Create a caloric deficit through diet and exercise")
        print("• Increase physical activity gradually")
        print("• Focus on whole foods and reduce processed foods")
        print("• Consider consulting with a healthcare provider")
    
    print("=" * 55)

if __name__ == "__main__":
    main() 