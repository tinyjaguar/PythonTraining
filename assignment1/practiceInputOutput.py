# 1. Ask the user for their name & greet them
name = input("Enter your name: ")
print(f"Hello, {name}! Welcome!\n")

# 2. Perform arithmetic operations on two numbers
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

# 3. Comma-separated names → list
input_names = input("Enter names separated by commas: ")
name_list = input_names.split(",")
print("Names List:", name_list, "\n")

# 4. Check voting eligibility
age = int(input("Enter your age: "))
if age >= 18:
    print("You are eligible to vote.\n")
else:
    print("You are NOT eligible to vote.\n")

# 5. Print value using f-string up to 2 decimal places
value = 3.14159
print("Value up to 2 decimal places:", f"{value:.2f}")
