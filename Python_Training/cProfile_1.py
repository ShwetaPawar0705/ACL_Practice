import cProfile

# Define a recursive factorial function
def recursive_factorial(n):
    if n <= 1:
        return 1
    return n * recursive_factorial(n - 1)

# Define an iterative factorial function
def iterative_factorial(n):
    result = 1
    for i in range(1, n + 1):
        result *= i
    return result

# Main function to profile
def main():
    print("Calculating recursive factorial of 20:")
    recursive_result = recursive_factorial(20)
    print("Result:", recursive_result)

    print("Calculating iterative factorial of 20:")
    iterative_result = iterative_factorial(20)
    print("Result:", iterative_result)

# Run the profiler on the main function
cProfile.run('main()')

