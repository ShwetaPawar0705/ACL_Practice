# Syntax:

# lambda arguments: expression

# Using regular function
# def add(x,y):
#     return x + y

# Using lambda function
lambda_add = lambda x, y: x + y

# Use lambda function
num1 = int(input("Enter first number: "))
num2 = int(input("Enter second number: "))
result = lambda_add(num1, num2)
print(result)

# Lambda with map
# map() - applies function to each element in iterable fashion
nums = [1,2,3,4,5,6]

doubled = map(lambda x: x * 3, nums)

print(list(doubled))

# Lambda with filter
num = [1,2,3,4,5]

odd = filter(lambda x: x % 2 != 0, num)

print(list(odd))