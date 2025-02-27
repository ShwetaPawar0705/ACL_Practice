# main.py
from tasks import add

# Calling the task
result = add.delay(4, 5)  # This will run in the background
print("Task submitted!")
