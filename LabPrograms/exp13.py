# Program to demonstrate basic operations and built-in functions of a set

# Creating a set
fruits = {"apple", "banana", "cherry"}
print("Original set:", fruits)

# Adding an element
fruits.add("orange")
print("After adding 'orange':", fruits)

# Removing an element
fruits.remove("banana")
print("After removing 'banana':", fruits)

# Checking membership
print("Is 'apple' in set?", "apple" in fruits)

# Set length
print("Number of elements:", len(fruits))

# Built-in set functions
more_fruits = {"cherry", "mango", "apple"}
print("Union:", fruits.union(more_fruits))
print("Intersection:", fruits.intersection(more_fruits))
print("Difference:", fruits.difference(more_fruits))

# Clearing the set
fruits.clear()
print("After clearing:", fruits)
print("Min:", min(more_fruits), "Max:", max(more_fruits), "Sum (not possible for strings):", "N/A", "Sorted:", sorted(more_fruits))
# Program to demonstrate basic operations and built-in functions of a tuple
