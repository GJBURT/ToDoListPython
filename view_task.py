# Function for viewing tasks
def view_tasks(tasks):
    if not tasks:
        print("\nNo tasks to view.")
    else:
        print("\nYour tasks:")
        for index, task in enumerate(tasks, start=1):
            print(f"{index}. {task}")