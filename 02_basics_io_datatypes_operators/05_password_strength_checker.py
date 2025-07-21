"""
Password Strength Checker
A practical program to check password strength and provide security recommendations.
Demonstrates: String operators, Boolean operations, Comparison operators, Type checking
"""

import re

def main():
    print("=" * 60)
    print("           PASSWORD STRENGTH CHECKER")
    print("=" * 60)
    
    print("Create a strong password with the following criteria:")
    print("• At least 8 characters long")
    print("• Contains uppercase letters (A-Z)")
    print("• Contains lowercase letters (a-z)")
    print("• Contains numbers (0-9)")
    print("• Contains special characters (!@#$%^&*)")
    print("• No common patterns or dictionary words")
    print("-" * 60)
    
    password = input("Enter your password: ")
    
    # Password strength criteria
    length_score = 0
    character_score = 0
    complexity_score = 0
    pattern_score = 0
    
    # Check length
    length = len(password)
    if length >= 12:
        length_score = 4
        length_feedback = "Excellent length"
    elif length >= 8:
        length_score = 3
        length_feedback = "Good length"
    elif length >= 6:
        length_score = 2
        length_feedback = "Fair length"
    else:
        length_score = 1
        length_feedback = "Too short"
    
    # Check character types
    has_uppercase = bool(re.search(r'[A-Z]', password))
    has_lowercase = bool(re.search(r'[a-z]', password))
    has_digits = bool(re.search(r'[0-9]', password))
    has_special = bool(re.search(r'[!@#$%^&*(),.?":{}|<>]', password))
    
    character_types = sum([has_uppercase, has_lowercase, has_digits, has_special])
    character_score = character_types
    
    # Check complexity patterns
    complexity_checks = []
    
    # No repeated characters
    no_repeats = not bool(re.search(r'(.)\1{2,}', password))
    complexity_checks.append(no_repeats)
    
    # No sequential characters
    sequential_patterns = ['123', '234', '345', '456', '567', '678', '789', '890',
                          'abc', 'bcd', 'cde', 'def', 'efg', 'fgh', 'ghi', 'hij']
    no_sequential = not any(pattern in password.lower() for pattern in sequential_patterns)
    complexity_checks.append(no_sequential)
    
    # No common keyboard patterns
    keyboard_patterns = ['qwerty', 'asdf', 'zxcv', '1234', 'abcd']
    no_keyboard = not any(pattern in password.lower() for pattern in keyboard_patterns)
    complexity_checks.append(no_keyboard)
    
    complexity_score = sum(complexity_checks)
    
    # Check against common passwords
    common_passwords = ['password', '123456', 'password123', 'admin', 'welcome',
                       'letmein', 'monkey', 'qwerty', 'dragon', 'master']
    is_common = password.lower() in common_passwords
    pattern_score = 0 if is_common else 3
    
    # Calculate total score
    total_score = length_score + character_score + complexity_score + pattern_score
    max_score = 14
    
    # Determine strength level
    strength_percentage = (total_score / max_score) * 100
    
    if strength_percentage >= 85:
        strength_level = "Very Strong"
        strength_color = "🟢"
        security_rating = "Excellent"
    elif strength_percentage >= 70:
        strength_level = "Strong"
        strength_color = "🟡"
        security_rating = "Good"
    elif strength_percentage >= 50:
        strength_level = "Moderate"
        strength_color = "🟠"
        security_rating = "Fair"
    elif strength_percentage >= 30:
        strength_level = "Weak"
        strength_color = "🔴"
        security_rating = "Poor"
    else:
        strength_level = "Very Weak"
        strength_color = "⚫"
        security_rating = "Very Poor"
    
    # Display results
    print("\n" + "=" * 60)
    print("              PASSWORD ANALYSIS")
    print("=" * 60)
    print(f"Password Length: {length} characters")
    print(f"Strength Level: {strength_color} {strength_level}")
    print(f"Security Rating: {security_rating}")
    print(f"Strength Score: {total_score}/{max_score} ({strength_percentage:.1f}%)")
    print("-" * 60)
    
    # Detailed breakdown
    print("DETAILED ANALYSIS:")
    print(f"📏 Length ({length_score}/4): {length_feedback}")
    print(f"🔤 Character Types ({character_score}/4):")
    print(f"   • Uppercase letters: {'✓' if has_uppercase else '✗'}")
    print(f"   • Lowercase letters: {'✓' if has_lowercase else '✗'}")
    print(f"   • Numbers: {'✓' if has_digits else '✗'}")
    print(f"   • Special characters: {'✓' if has_special else '✗'}")
    
    print(f"🔀 Complexity ({complexity_score}/3):")
    print(f"   • No repeated characters: {'✓' if no_repeats else '✗'}")
    print(f"   • No sequential patterns: {'✓' if no_sequential else '✗'}")
    print(f"   • No keyboard patterns: {'✓' if no_keyboard else '✗'}")
    
    print(f"🛡️  Pattern Security ({pattern_score}/3):")
    print(f"   • Not a common password: {'✓' if not is_common else '✗'}")
    
    # Recommendations
    print("\n" + "=" * 60)
    print("              RECOMMENDATIONS")
    print("=" * 60)
    
    if strength_percentage < 85:
        recommendations = []
        
        if length < 8:
            recommendations.append("• Make your password at least 8 characters long")
        elif length < 12:
            recommendations.append("• Consider making your password longer (12+ characters)")
        
        if not has_uppercase:
            recommendations.append("• Add uppercase letters (A-Z)")
        if not has_lowercase:
            recommendations.append("• Add lowercase letters (a-z)")
        if not has_digits:
            recommendations.append("• Add numbers (0-9)")
        if not has_special:
            recommendations.append("• Add special characters (!@#$%^&*)")
        
        if not no_repeats:
            recommendations.append("• Avoid repeating characters (aaa, 111)")
        if not no_sequential:
            recommendations.append("• Avoid sequential patterns (123, abc)")
        if not no_keyboard:
            recommendations.append("• Avoid keyboard patterns (qwerty, asdf)")
        if is_common:
            recommendations.append("• Avoid common passwords")
        
        if recommendations:
            print("To improve your password strength:")
            for rec in recommendations:
                print(rec)
        else:
            print("Your password meets most security criteria!")
    else:
        print("Excellent! Your password is very strong.")
        print("Remember to:")
        print("• Use unique passwords for different accounts")
        print("• Enable two-factor authentication when possible")
        print("• Change passwords regularly")
    
    print("=" * 60)
    
    # Generate password suggestion
    print("\nWould you like a strong password suggestion? (y/n): ", end="")
    choice = input().lower()
    
    if choice == 'y':
        import random
        import string
        
        # Generate a strong password
        length = 12
        characters = (string.ascii_uppercase + string.ascii_lowercase + 
                     string.digits + "!@#$%^&*")
        
        suggested_password = ''.join(random.choice(characters) for _ in range(length))
        
        print(f"\nSuggested strong password: {suggested_password}")
        print("Note: Make sure to store this password securely!")

if __name__ == "__main__":
    main() 