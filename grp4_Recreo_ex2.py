# Filename: grp4_Recreo_ex2.py

# Task #1: Arithmetic Operations on Different Data Types

# Integer variables
int_num1 = 10
int_num2 = 5

# Float variables
float_num1 = 10.5
float_num2 = 5.2

# Complex variables
complex_num1 = 2 + 3j
complex_num2 = 1 + 4j

# Operations for int
print("Integer Operations:")
print(f"Addition: {int_num1 + int_num2}")
print(f"Subtraction: {int_num1 - int_num2}")
print(f"Multiplication: {int_num1 * int_num2}")
print(f"Division: {int_num1 / int_num2}")
print(f"Modulus: {int_num1 % int_num2}")
print(f"Exponent: {int_num1 ** int_num2}\n")

# Operations for float
print("Float Operations:")
print(f"Addition: {float_num1 + float_num2}")
print(f"Subtraction: {float_num1 - float_num2}")
print(f"Multiplication: {float_num1 * float_num2}")
print(f"Division: {float_num1 / float_num2}")
print(f"Modulus: {float_num1 % float_num2}")
print(f"Exponent: {float_num1 ** float_num2}\n")

# Operations for complex
print("Complex Operations:")
print(f"Addition: {complex_num1 + complex_num2}")
print(f"Subtraction: {complex_num1 - complex_num2}")
print(f"Multiplication: {complex_num1 * complex_num2}")
print(f"Division: {complex_num1 / complex_num2}")

print()

# Task #2: Creating Two Integer Variables with and without Underscores
num1 = 25_000_000  # Integer with underscores
num2 = 25000000    # Integer without underscores

# Print both variables
print("num1:", num1)
print("num2:", num2)
print()

# Task #3: Creating and Checking Variable Types
int_var = 42           # Integer
float_var = 3.14       # Float
complex_var = 1 + 2j  # Complex number

# Checking and printing the type of each variable
print("Type of int_var:", type(int_var))
print("Type of float_var:", type(float_var))
print("Type of complex_var:", type(complex_var))