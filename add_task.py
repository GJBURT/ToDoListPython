# Function for adding a task
def add_task(tasks):
    task = input("Enter the task you want to add: ")
    tasks.append(task)
    print(f"\nTask '{task}' added successfully!")
