from celery import Celery

# Create a Celery app
app = Celery('tasks', broker='redis://localhost:6379/0')

# Define a task
@app.task
def add(x, y):
    return x + y