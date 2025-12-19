from functools import reduce

# 1. Double each element using map()
a = [1, 2, 3, 4]
double_elements = list(map(lambda x: x * 2, a))
print("1. Doubled elements:", double_elements)

# 2. Extract all even numbers using filter() and lambda
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
even_numbers = list(filter(lambda x: x % 2 == 0, numbers))
print("2. Even numbers:", even_numbers)

# 3. Find the longest word using reduce() and lambda
words = ["apple", "banana", "cherry", "date"]
longest_word = reduce(lambda a, b: a if len(a) > len(b) else b, words)
print("3. Longest word:", longest_word)

# 4. Square each number and round to one decimal using map()
my_floats = [4.35, 6.09, 3.25, 9.77, 2.16, 8.88, 4.59]
squared_rounded = list(map(lambda x: round(x ** 2, 1), my_floats))
print("4. Squared and rounded:", squared_rounded)

# 5. Select names with 7 or fewer characters using filter()
my_names = ["olumide", "akinremi", "josiah", "temidayo", "omoseun"]
short_names = list(filter(lambda name: len(name) <= 7, my_names))
print("5. Names with 7 or fewer characters:", short_names)

# 6. Calculate the sum of all numbers using reduce()
nums = [1, 2, 3, 4, 5]
total_sum = reduce(lambda a, b: a + b, nums)
print("6. Sum of numbers:", total_sum)
