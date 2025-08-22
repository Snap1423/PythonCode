
# Creating a tuple
colors = ("red", "green", "blue")
print("\nOriginal tuple:", colors)

# Accessing elements
print("First element:", colors[0])
print("Last element:", colors[-1])

# Slicing
print("Sliced tuple (first two):", colors[:2])

# Tuple concatenation
more_colors = ("yellow", "purple")
combined = colors + more_colors
print("After concatenation:", combined)

# Tuple repetition
repeated = colors * 2
print("After repetition:", repeated)

# Checking membership
print("Is 'green' in tuple?", "green" in colors)

# Tuple length
print("Number of elements:", len(colors))

# Built-in tuple functions
numbers = (5, 2, 9, 1)
print("Numbers tuple:", numbers)
print("Min:", min(numbers), "Max:", max(numbers), "Sum:", sum(numbers), "Sorted:", sorted(numbers))

# Counting and index
sample = ("a", "b", "a", "c", "a")
print("Count of 'a':", sample.count("a"))
print("Index of 'c':", sample.index("c"))