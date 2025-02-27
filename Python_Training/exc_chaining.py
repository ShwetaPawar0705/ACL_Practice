try:
    open('nofile.txt')
except OSError:
    raise RuntimeError("Unable to handle error")

# Implicit exception chaining
try:
    x = 1 / 0
except ZeroDivisionError:
    raise ValueError('A value error occured after a ZeroDivisionError')

# Explicit exception chaining
try:
    x = int("abc")
except ValueError as e:
    raise TypeError('A type error occured due to the value error') from e