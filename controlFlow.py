# ---------------------------------------------
# FOR LOOP PROGRAMS
# ---------------------------------------------

# 1. Check if a number is even or odd
num = int(input("Enter a number to check even/odd: "))
if num % 2 == 0:
    print(num, "is Even")
else:
    print(num, "is Odd")
print()


# 2. Reverse a string using for loop and check palindrome
s = input("Enter a string to check palindrome: ")
rev = ""

for ch in s:
    rev = ch + rev   # building reverse string

print("Reversed string:", rev)

if rev == s:
    print("It is a palindrome")
else:
    print("It is NOT a palindrome")
print()


# 3. Generate first N Fibonacci numbers
n = int(input("Enter N for Fibonacci sequence: "))
a, b = 0, 1

print("Fibonacci:", end=" ")
for i in range(n):
    print(a, end=" ")
    a, b = b, a + b
print("\n")


# 4. Find two values from list whose sum is 9
nums = [1, 2, 3, 4, 5]
result = []

for i in range(len(nums)):
    for j in range(i + 1, len(nums)):
        if nums[i] + nums[j] == 9:
            result = [nums[i], nums[j]]

print("Two numbers that sum to 9:", result)
print()


# ---------------------------------------------
# WHILE LOOP PROGRAM
# ---------------------------------------------

# Print all even numbers between 1 and 20
print("Even numbers between 1 and 20:")
i = 1
while i <= 20:
    if i % 2 == 0:
        print(i, end=" ")
    i += 1
print("\n")


# ---------------------------------------------
# BREAK STATEMENT
# ---------------------------------------------

numbers = [10, 20, 30, 40, 50]
search_for = 30

for num in numbers:
    if num == search_for:
        print("Found:", num)
        break  # stop searching
print()


# ---------------------------------------------
# CONTINUE STATEMENT
# ---------------------------------------------

print("Odd numbers from 1 to 10:")
for i in range(1, 11):
    if i % 2 == 0:
        continue
    print(i, end=" ")
print("\n")


# ---------------------------------------------
# PASS STATEMENT
# ---------------------------------------------

print("Output of pass example:")
for i in range(5):
    if i == 3:
        pass  
    print(i)
print()


# ---------------------------------------------
# MATCH STATEMENT
# ---------------------------------------------

day = input("Enter day of the week: ").lower()

match day:
    case "monday" | "tuesday" | "wednesday" | "thursday" | "friday":
        print("It's a weekday")
    case "saturday" | "sunday":
        print("It's a weekend")
    case _:
        print("Invalid day entered")
