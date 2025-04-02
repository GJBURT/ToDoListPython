# Function for deleting a task  
from view_task import view_tasks

def delete_task(tasks):
    if not tasks:
        print("\nNo tasks to delete.")
    else:
        view_tasks(tasks)
        try:
            task_number = int(input("Enter the task number you want to delete: "))
            if 1 <= task_number <= len(tasks):
                removed_task = tasks.pop(task_number - 1)
                print(f"\nTask '{removed_task}' deleted successfully!")
            else:
                print("\nInvalid task number.")
        except ValueError:
            print("\nPlease enter a valid number.")
        except IndexError:
            print("\nTask number out of range.")