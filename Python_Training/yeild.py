# def count(max_value):
#     count =1
#     while count <= max_value:
#         yield count
#         count += 1

# # Create a generator
# counter = count(5)

# print(next(counter))
# print(next(counter))
# print(next(counter))
# print(next(counter))
# print(next(counter))

# Using loop
# def odd_num(max_value):
#     for n in range(max_value + 10):
#         if n % 2 != 0:
#             yield n

# for number in odd_num(10):
#     print(number)  

# cube generator
def cube_generator(n):
    for i in range(n, n+1):
        yield i ** 3

n = int(input("Enter a number:"))

# Create a generator object
cubes = cube_generator(n)

# Iterate over the cubes and print the result
print("cubes of numbers from 1 to", n)
for num in cubes:
    print(num)