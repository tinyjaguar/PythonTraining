# ---------------------------------------------------------
# 1. Convert list of numeric strings to integers
# ---------------------------------------------------------
strings = ["1", "2", "3", "4", "5"]
int_list = [int(x) for x in strings]
print(int_list)


# ---------------------------------------------------------
# 2. Extract integers greater than 10
# ---------------------------------------------------------
numbers = [1, 5, 13, 4, 16, 7]
greater_than_10 = [x for x in numbers if x > 10]
print(greater_than_10)


# ---------------------------------------------------------
# 3. List of squares for numbers 1 to 5
# ---------------------------------------------------------
squares = [x * x for x in range(1, 6)]
print(squares)


# ---------------------------------------------------------
# 4. Convert 2D list to 1D list
# ---------------------------------------------------------
matrix = [[1, 3, 4], [23, 32, 56, 74], [-2, -6, -9]]
flattened = [num for row in matrix for num in row]
print(flattened)


# ---------------------------------------------------------
# 5. Create dictionary using keys & values
# ---------------------------------------------------------
keys = ['a', 'b', 'c']
values = [1, 2, 3]
my_dict = {keys[i]: values[i] for i in range(len(keys))}
print(my_dict)


# ---------------------------------------------------------
# 6. Dictionary of students scoring above 80
# ---------------------------------------------------------
scores = {'Alice': 85, 'Bob': 70, 'Charlie': 90}
above_80 = {name: score for name, score in scores.items() if score > 80}
print(above_80)
