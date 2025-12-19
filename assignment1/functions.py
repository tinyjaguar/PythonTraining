# ----------------------------------------------------
# 1. Function to calculate area with default width = 10
# ----------------------------------------------------
def calculate_area(length, width=10):
    return length * width


# ----------------------------------------------------
# 2. Recursive function for factorial
# ----------------------------------------------------
def factorial(n):
    if n == 0 or n == 1:
        return 1
    return n * factorial(n - 1)


# ----------------------------------------------------
# 3. Function to reverse a string
# ----------------------------------------------------
def reverse_string(text):
    reversed_text = ""
    for ch in text:
        reversed_text = ch + reversed_text
    return reversed_text


# ----------------------------------------------------
# 4. Function to sum all numbers from two lists
# ----------------------------------------------------
def sum_two_lists(list1, list2):
    return sum(list1) + sum(list2)


# ----------------------------------------------------
# 5. Function to return sorted distinct list
# ----------------------------------------------------
def distinct_sorted(my_list):
    return sorted(list(set(my_list)))


# --------------------- Testing the functions ---------------------

# 1. Area test
print("Area:", calculate_area(5))           # width defaults to 10 → 5*10=50
print("Area:", calculate_area(5, 20))       # custom width → 5*20=100

# 2. Factorial
print("Factorial 5:", factorial(5))

# 3. Reverse string
print("Reverse:", reverse_string("python"))

# 4. Sum of two lists
a = [8, 2, 3, 0, 7]
b = [3, -2, 5, 1]
print("Sum of two lists:", sum_two_lists(a, b))

# 5. Distinct + sorted list
a = [4,1,2,3,3,1,3,4,5,1,7]
print("Distinct Sorted:", distinct_sorted(a))
