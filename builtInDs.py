# -----------------------------------------
# 1. Ask the user for their name & greet
# -----------------------------------------
name = input("Enter your name: ")
print(f"Hello, {name}! Welcome!\n")

# -----------------------------------------
# 2. Arithmetic operations
# -----------------------------------------
num1 = float(input("Enter first number: "))
num2 = float(input("Enter second number: "))

print("\n--- Arithmetic Results ---")
print("Sum:", num1 + num2)
print("Multiplication:", num1 * num2)

if num2 != 0:
    print("Division:", num1 / num2)
else:
    print("Division: Cannot divide by zero")
print()

# -----------------------------------------
# 3. Comma-separated names → list
# -----------------------------------------
input_names = input("Enter names separated by commas: ")
name_list = input_names.split(",")
print("Names List:", name_list, "\n")

# -----------------------------------------
# 4. Voting eligibility
# -----------------------------------------
age = int(input("Enter your age: "))
if age >= 18:
    print("You are eligible to vote.\n")
else:
    print("You are NOT eligible to vote.\n")

# -----------------------------------------
# 5. Print value with 2 decimal points
# -----------------------------------------
value = 3.14159
print("Value up to 2 decimal places:", f"{value:.2f}\n")

# -----------------------------------------
# 6. Maximum and minimum from a list
# -----------------------------------------
nums = [1, 2, 3, 4, 5]
print("List:", nums)
print("Maximum:", max(nums))
print("Minimum:", min(nums), "\n")

# -----------------------------------------
# 7. Merge two lists
# -----------------------------------------
a = [1, 2, 3, 4]
b = [5, 6, 7, 8]
merged_list = a + b
print("Merged List:", merged_list, "\n")

# -----------------------------------------
# 8. Count occurrences of value 3
# -----------------------------------------
a = [1, 3, 4, 5, 2, 1, 3, 9, 3]
print("Count of 3:", a.count(3), "\n")

# -----------------------------------------
# 9. Sort list
# -----------------------------------------
a_sorted = sorted(a)
print("Sorted List:", a_sorted, "\n")

# -----------------------------------------
# 10. Add element to a set
# -----------------------------------------
numbers = {1, 2, 3, 4, 5}
numbers.add(6)
print("Set after adding 6:", numbers, "\n")

# -----------------------------------------
# 11. Remove element 3 from set
# -----------------------------------------
numbers = {1, 2, 3, 4, 5}
numbers.remove(3)
print("Set after removing 3:", numbers, "\n")

# -----------------------------------------
# 12. Intersection of two sets
# -----------------------------------------
set1 = {1, 2, 3}
set2 = {3, 4, 5}
print("Intersection:", set1.intersection(set2), "\n")

# -----------------------------------------
# 13. Count occurrences in tuple
# -----------------------------------------
fruits = ('apple', 'banana', 'apple', 'cherry')
print("Number of 'apple':", fruits.count('apple'), "\n")

# -----------------------------------------
# 14. Concatenate two tuples
# -----------------------------------------
tuple1 = (1, 2, 3)
tuple2 = (4, 5, 6)
print("Concatenated Tuple:", tuple1 + tuple2, "\n")

# -----------------------------------------
# 15. Access dictionary value
# -----------------------------------------
person = {"name": "Alice", "age": 30, "city": "New York"}
print("Age:", person["age"], "\n")

# -----------------------------------------
# 16. Add new key to dictionary
# -----------------------------------------
person["gender"] = "M"
print("After adding gender:", person, "\n")

# -----------------------------------------
# 17. Remove key from dictionary
# -----------------------------------------
person.pop("city")
print("After removing city:", person, "\n")

# -----------------------------------------
# 18. Merge two dictionaries
# -----------------------------------------
dict1 = {"a": 1, "b": 2}
dict2 = {"c": 3, "d": 4}
merged_dict = {**dict1, **dict2}
print("Merged Dictionary:", merged_dict)
