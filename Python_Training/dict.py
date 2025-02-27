# Filtering with conditions
nums = [1,2,3,4,5,6,7,8,9]
even_squares = {x: x**2 for x in nums if x % 2 == 0}
print(even_squares)

# Transforming Data
employees = {'Alice': 25, 'Bob': 35, 'Charlie': 40, 'David': 28}
above_30 = {name: age for name, age in employees.items() if age > 30}
print(above_30)

# Combining two lists
keys = ['a','b','c']
values = [1,2,3]
combined = {k:v for k,v in zip(keys,values)}
print(combined)

# Nested dictionary comprehension -> used to create multiplication tables
table = {x: {y: x*y for y in range(1,5)} for x in range(1,5)}
print(table)
