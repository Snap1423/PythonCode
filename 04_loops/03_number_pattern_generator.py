"""
Number Pattern Generator
A practical program to generate various number patterns using nested loops.
Demonstrates: Nested loops, for loops with range(), pattern logic, mathematical calculations
"""

def main():
    print("=" * 60)
    print("           NUMBER PATTERN GENERATOR")
    print("=" * 60)
    
    print("🎨 Welcome to the Pattern Generator!")
    print("Create beautiful number patterns using different algorithms")
    
    while True:
        print("\n" + "=" * 60)
        print("              PATTERN MENU")
        print("=" * 60)
        print("1. Triangle Patterns")
        print("2. Square Patterns")
        print("3. Diamond Patterns")
        print("4. Special Number Patterns")
        print("5. Pyramid Patterns")
        print("6. Custom Pattern Builder")
        print("7. Exit")
        print("-" * 60)
        
        choice = input("Select pattern type (1-7): ")
        
        if choice == "1":
            # Triangle Patterns
            print("\n🔺 TRIANGLE PATTERNS")
            print("-" * 30)
            print("1. Right Triangle (Numbers)")
            print("2. Right Triangle (Sequential)")
            print("3. Inverted Right Triangle")
            print("4. Pascal's Triangle")
            print("5. Multiplication Table Triangle")
            
            pattern_choice = input("Select triangle pattern (1-5): ")
            
            try:
                size = int(input("Enter size (1-15): "))
                if not (1 <= size <= 15):
                    print("Size must be between 1 and 15")
                    continue
            except ValueError:
                print("Please enter a valid number!")
                continue
            
            print(f"\n🎯 Generating Triangle Pattern (Size: {size})")
            print("-" * 40)
            
            if pattern_choice == "1":
                # Right Triangle with Numbers
                for i in range(1, size + 1):
                    for j in range(1, i + 1):
                        print(f"{j:2}", end=" ")
                    print()
                    
            elif pattern_choice == "2":
                # Right Triangle Sequential
                num = 1
                for i in range(1, size + 1):
                    for j in range(i):
                        print(f"{num:2}", end=" ")
                        num += 1
                    print()
                    
            elif pattern_choice == "3":
                # Inverted Right Triangle
                for i in range(size, 0, -1):
                    for j in range(1, i + 1):
                        print(f"{j:2}", end=" ")
                    print()
                    
            elif pattern_choice == "4":
                # Pascal's Triangle
                for i in range(size):
                    # Print spaces for alignment
                    for j in range(size - i - 1):
                        print("  ", end="")
                    
                    # Calculate and print Pascal's triangle values
                    value = 1
                    for j in range(i + 1):
                        print(f"{value:3}", end=" ")
                        value = value * (i - j) // (j + 1)
                    print()
                    
            elif pattern_choice == "5":
                # Multiplication Table Triangle
                for i in range(1, size + 1):
                    for j in range(1, i + 1):
                        product = i * j
                        print(f"{product:3}", end=" ")
                    print()
            else:
                print("Invalid choice!")
        
        elif choice == "2":
            # Square Patterns
            print("\n⬜ SQUARE PATTERNS")
            print("-" * 30)
            print("1. Hollow Square")
            print("2. Filled Square with Numbers")
            print("3. Diagonal Pattern")
            print("4. Spiral Pattern")
            print("5. Chess Board Pattern")
            
            pattern_choice = input("Select square pattern (1-5): ")
            
            try:
                size = int(input("Enter size (3-12): "))
                if not (3 <= size <= 12):
                    print("Size must be between 3 and 12")
                    continue
            except ValueError:
                print("Please enter a valid number!")
                continue
            
            print(f"\n🎯 Generating Square Pattern (Size: {size})")
            print("-" * 40)
            
            if pattern_choice == "1":
                # Hollow Square
                for i in range(size):
                    for j in range(size):
                        if i == 0 or i == size-1 or j == 0 or j == size-1:
                            print("* ", end="")
                        else:
                            print("  ", end="")
                    print()
                    
            elif pattern_choice == "2":
                # Filled Square with Numbers
                for i in range(size):
                    for j in range(size):
                        print(f"{(i + j) % 10}", end=" ")
                    print()
                    
            elif pattern_choice == "3":
                # Diagonal Pattern
                for i in range(size):
                    for j in range(size):
                        if i == j or i + j == size - 1:
                            print("X ", end="")
                        else:
                            print("O ", end="")
                    print()
                    
            elif pattern_choice == "4":
                # Spiral Pattern (simplified)
                matrix = [[0] * size for _ in range(size)]
                
                # Fill matrix in spiral order
                top, bottom, left, right = 0, size-1, 0, size-1
                num = 1
                
                while top <= bottom and left <= right:
                    # Fill top row
                    for col in range(left, right + 1):
                        matrix[top][col] = num
                        num += 1
                    top += 1
                    
                    # Fill right column
                    for row in range(top, bottom + 1):
                        matrix[row][right] = num
                        num += 1
                    right -= 1
                    
                    # Fill bottom row
                    if top <= bottom:
                        for col in range(right, left - 1, -1):
                            matrix[bottom][col] = num
                            num += 1
                        bottom -= 1
                    
                    # Fill left column
                    if left <= right:
                        for row in range(bottom, top - 1, -1):
                            matrix[row][left] = num
                            num += 1
                        left += 1
                
                # Print the spiral matrix
                for row in matrix:
                    for val in row:
                        print(f"{val:3}", end=" ")
                    print()
                    
            elif pattern_choice == "5":
                # Chess Board Pattern
                for i in range(size):
                    for j in range(size):
                        if (i + j) % 2 == 0:
                            print("█ ", end="")
                        else:
                            print("░ ", end="")
                    print()
            else:
                print("Invalid choice!")
        
        elif choice == "3":
            # Diamond Patterns
            print("\n💎 DIAMOND PATTERNS")
            print("-" * 30)
            print("1. Number Diamond")
            print("2. Hollow Diamond")
            print("3. Diamond with Center")
            print("4. Double Diamond")
            
            pattern_choice = input("Select diamond pattern (1-4): ")
            
            try:
                size = int(input("Enter size (odd number 3-11): "))
                if not (3 <= size <= 11) or size % 2 == 0:
                    print("Size must be an odd number between 3 and 11")
                    continue
            except ValueError:
                print("Please enter a valid number!")
                continue
            
            print(f"\n🎯 Generating Diamond Pattern (Size: {size})")
            print("-" * 40)
            
            mid = size // 2
            
            if pattern_choice == "1":
                # Number Diamond
                # Upper half
                for i in range(mid + 1):
                    # Print spaces
                    for j in range(mid - i):
                        print("  ", end="")
                    # Print numbers
                    for j in range(2 * i + 1):
                        print(f"{(j % 9) + 1} ", end="")
                    print()
                
                # Lower half
                for i in range(mid - 1, -1, -1):
                    # Print spaces
                    for j in range(mid - i):
                        print("  ", end="")
                    # Print numbers
                    for j in range(2 * i + 1):
                        print(f"{(j % 9) + 1} ", end="")
                    print()
                    
            elif pattern_choice == "2":
                # Hollow Diamond
                # Upper half
                for i in range(mid + 1):
                    for j in range(mid - i):
                        print("  ", end="")
                    for j in range(2 * i + 1):
                        if j == 0 or j == 2 * i:
                            print("* ", end="")
                        else:
                            print("  ", end="")
                    print()
                
                # Lower half
                for i in range(mid - 1, -1, -1):
                    for j in range(mid - i):
                        print("  ", end="")
                    for j in range(2 * i + 1):
                        if j == 0 or j == 2 * i:
                            print("* ", end="")
                        else:
                            print("  ", end="")
                    print()
                    
            elif pattern_choice == "3":
                # Diamond with Center
                for i in range(size):
                    for j in range(size):
                        distance = abs(i - mid) + abs(j - mid)
                        if distance == mid:
                            print("* ", end="")
                        elif distance < mid:
                            print(f"{distance + 1} ", end="")
                        else:
                            print("  ", end="")
                    print()
                    
            elif pattern_choice == "4":
                # Double Diamond
                for i in range(size):
                    for j in range(size):
                        if (abs(i - mid) + abs(j - mid) == mid) or \
                           (abs(i - mid) + abs(j - mid) == mid // 2):
                            print("* ", end="")
                        else:
                            print("  ", end="")
                    print()
            else:
                print("Invalid choice!")
        
        elif choice == "4":
            # Special Number Patterns
            print("\n🔢 SPECIAL NUMBER PATTERNS")
            print("-" * 30)
            print("1. Fibonacci Triangle")
            print("2. Prime Number Pattern")
            print("3. Perfect Square Pattern")
            print("4. Factorial Pattern")
            print("5. Sum Pattern")
            
            pattern_choice = input("Select special pattern (1-5): ")
            
            try:
                size = int(input("Enter size (1-10): "))
                if not (1 <= size <= 10):
                    print("Size must be between 1 and 10")
                    continue
            except ValueError:
                print("Please enter a valid number!")
                continue
            
            print(f"\n🎯 Generating Special Pattern (Size: {size})")
            print("-" * 40)
            
            if pattern_choice == "1":
                # Fibonacci Triangle
                def fibonacci(n):
                    if n <= 1:
                        return n
                    return fibonacci(n-1) + fibonacci(n-2)
                
                fib_num = 0
                for i in range(1, size + 1):
                    for j in range(i):
                        print(f"{fibonacci(fib_num):4}", end=" ")
                        fib_num += 1
                    print()
                    
            elif pattern_choice == "2":
                # Prime Number Pattern
                def is_prime(n):
                    if n < 2:
                        return False
                    for i in range(2, int(n**0.5) + 1):
                        if n % i == 0:
                            return False
                    return True
                
                prime_count = 0
                num = 2
                for i in range(1, size + 1):
                    for j in range(i):
                        while not is_prime(num):
                            num += 1
                        print(f"{num:4}", end=" ")
                        num += 1
                        prime_count += 1
                    print()
                    
            elif pattern_choice == "3":
                # Perfect Square Pattern
                square_num = 1
                for i in range(1, size + 1):
                    for j in range(i):
                        print(f"{square_num**2:4}", end=" ")
                        square_num += 1
                    print()
                    
            elif pattern_choice == "4":
                # Factorial Pattern
                def factorial(n):
                    if n <= 1:
                        return 1
                    return n * factorial(n-1)
                
                fact_num = 1
                for i in range(1, size + 1):
                    for j in range(i):
                        print(f"{factorial(fact_num):6}", end=" ")
                        fact_num += 1
                    print()
                    
            elif pattern_choice == "5":
                # Sum Pattern (sum of row and column indices)
                for i in range(1, size + 1):
                    for j in range(1, i + 1):
                        print(f"{i + j:3}", end=" ")
                    print()
            else:
                print("Invalid choice!")
        
        elif choice == "5":
            # Pyramid Patterns
            print("\n🔺 PYRAMID PATTERNS")
            print("-" * 30)
            print("1. Number Pyramid")
            print("2. Inverted Pyramid")
            print("3. Binary Pyramid")
            print("4. Alphabet Pyramid")
            
            pattern_choice = input("Select pyramid pattern (1-4): ")
            
            try:
                size = int(input("Enter size (1-10): "))
                if not (1 <= size <= 10):
                    print("Size must be between 1 and 10")
                    continue
            except ValueError:
                print("Please enter a valid number!")
                continue
            
            print(f"\n🎯 Generating Pyramid Pattern (Size: {size})")
            print("-" * 40)
            
            if pattern_choice == "1":
                # Number Pyramid
                for i in range(1, size + 1):
                    # Print spaces
                    for j in range(size - i):
                        print("  ", end="")
                    # Print ascending numbers
                    for j in range(1, i + 1):
                        print(f"{j:2}", end=" ")
                    # Print descending numbers
                    for j in range(i - 1, 0, -1):
                        print(f"{j:2}", end=" ")
                    print()
                    
            elif pattern_choice == "2":
                # Inverted Pyramid
                for i in range(size, 0, -1):
                    # Print spaces
                    for j in range(size - i):
                        print("  ", end="")
                    # Print numbers
                    for j in range(1, i + 1):
                        print(f"{j:2}", end=" ")
                    for j in range(i - 1, 0, -1):
                        print(f"{j:2}", end=" ")
                    print()
                    
            elif pattern_choice == "3":
                # Binary Pyramid
                for i in range(1, size + 1):
                    # Print spaces
                    for j in range(size - i):
                        print("  ", end="")
                    # Print binary pattern
                    for j in range(i):
                        print(f"{j % 2:2}", end=" ")
                    print()
                    
            elif pattern_choice == "4":
                # Alphabet Pyramid
                for i in range(1, size + 1):
                    # Print spaces
                    for j in range(size - i):
                        print("  ", end="")
                    # Print letters
                    for j in range(i):
                        letter = chr(ord('A') + j)
                        print(f"{letter:2}", end=" ")
                    print()
            else:
                print("Invalid choice!")
        
        elif choice == "6":
            # Custom Pattern Builder
            print("\n🛠️ CUSTOM PATTERN BUILDER")
            print("-" * 30)
            print("Build your own pattern!")
            
            try:
                rows = int(input("Enter number of rows (1-10): "))
                if not (1 <= rows <= 10):
                    print("Rows must be between 1 and 10")
                    continue
                    
                pattern_type = input("Pattern type (number/star/letter): ").lower()
                
                if pattern_type not in ['number', 'star', 'letter']:
                    print("Invalid pattern type!")
                    continue
                    
                shape = input("Shape (triangle/square/custom): ").lower()
                
                print(f"\n🎯 Generating Custom Pattern")
                print("-" * 40)
                
                if shape == "triangle":
                    for i in range(1, rows + 1):
                        for j in range(i):
                            if pattern_type == "number":
                                print(f"{j + 1:2}", end=" ")
                            elif pattern_type == "star":
                                print("* ", end="")
                            elif pattern_type == "letter":
                                letter = chr(ord('A') + j)
                                print(f"{letter} ", end="")
                        print()
                        
                elif shape == "square":
                    for i in range(rows):
                        for j in range(rows):
                            if pattern_type == "number":
                                print(f"{(i + j) % 10}", end=" ")
                            elif pattern_type == "star":
                                print("* ", end="")
                            elif pattern_type == "letter":
                                letter = chr(ord('A') + ((i + j) % 26))
                                print(f"{letter} ", end="")
                        print()
                        
                else:  # custom
                    print("Custom shape - creating alternating pattern")
                    for i in range(rows):
                        elements = (i % 3) + 1  # 1 to 3 elements per row
                        for j in range(elements):
                            if pattern_type == "number":
                                print(f"{(i + j + 1):2}", end=" ")
                            elif pattern_type == "star":
                                print("* ", end="")
                            elif pattern_type == "letter":
                                letter = chr(ord('A') + ((i + j) % 26))
                                print(f"{letter} ", end="")
                        print()
                        
            except ValueError:
                print("Please enter valid numbers!")
        
        elif choice == "7":
            # Exit
            print("\n🎨 PATTERN GENERATOR SUMMARY")
            print("=" * 50)
            print("Thank you for using the Number Pattern Generator!")
            print("You've explored various pattern types:")
            print("• Triangle patterns with different algorithms")
            print("• Square patterns including spirals and chess boards")
            print("• Diamond patterns with hollow and filled designs")
            print("• Special mathematical patterns (Fibonacci, Primes)")
            print("• Pyramid patterns with numbers and letters")
            print("• Custom pattern building capabilities")
            print("\n🚀 Keep experimenting with patterns!")
            print("Try modifying the code to create your own unique designs!")
            break
        
        else:
            print("❌ Invalid choice! Please select 1-7.")

if __name__ == "__main__":
    main() 