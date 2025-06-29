#1
# Predict the output before running
print(type(42)) # int
print(type(3.14159)) # float
print(type(2 + 3j)) #complex
print(True+True) # bool

#What type does Python assign to each number?
#How do Booleans behave in arithmetic operations? 1 - True 0 - False
#2
# Define two numbers
a = 15
b = 2

# Perform calculations
sum_result = a + b
difference = a - b
product = a * b
modulus = a % b
quotient = a / b
floor_division = a // b
power = a ** b

# Print results
print("Sum:", sum_result)
print("Difference:", difference)
print("Product:", product)
print("Quotient:", quotient)
print("Floor Division:", floor_division)
print("Modulus:", modulus)
print("Power:", power)
#What is the difference between / and //?
#What happens if b = 0 when using / or %?

#3
# Convert float to integer
print(int(9.99))

# Convert integer to float
print(float(100))

# Convert boolean to integer
print(int(True), int(False))

# Convert scientific notation to integer
print(int(2e2))

#4
# Absolute value
print(abs(-15))

# Round a floating point number
print(round(3.675))

# Power function
print(3**4)

# Find the max and min in a list
numbers = [4, 7, 2, 9, 1]
print(max(numbers))
print(min(numbers))

def my_function():
    return None

result = my_function()
print(type(None))