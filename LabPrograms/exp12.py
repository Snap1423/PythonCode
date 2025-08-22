# Program to find sum of n natural numbers using for loop
n = int(input("Enter a number: "))
sum = 0

for i in range(1, n + 1):
    sum += i

print(f"Sum of first {n} natural numbers is: {sum}")
