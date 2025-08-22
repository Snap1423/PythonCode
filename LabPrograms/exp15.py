# Basic list operations and built-in functions

fruits = ["apple", "banana", "cherry"]
a = fruits[0]
b = fruits[-1]
c = fruits[:2]
more_fruits = ["mango", "orange"]
combined = fruits + more_fruits
repeated = fruits * 2
is_banana = "banana" in fruits
length = len(fruits)
fruits.append("grape")
fruits.insert(1, "kiwi")
fruits.extend(["pear", "plum"])
fruits.remove("banana")
popped = fruits.pop()
del fruits[0]
fruits.clear()

numbers = [5, 2, 9, 1]
min_n = min(numbers)
max_n = max(numbers)
sum_n = sum(numbers)
sorted_n = sorted(numbers)

sample = ["a", "b", "a", "c", "a"]
count_a = sample.count("a")
index_c = sample.index("c")

sample2 = [3, 1, 4, 2]
sample2.reverse()
sample2.sort()
