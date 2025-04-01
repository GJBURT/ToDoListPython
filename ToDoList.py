# Creating a to do list application
# User Interface must have a simple Command Line Interface (CLI) that welcomes users and displays a menu with options to add, view, delete
#  tasks, or quit the application.
# Tasks will be stored in a python list
# Core Features: Add Task, View Task, Delete Task, Quit Application
# User interaction will use input()
# Implement error handling using try, except, else, and finally blocks to catch errors
# Alert the user if they provide invalid input
# Alert the user if there are no tasks to view
# Alert the user if they try to delete a task that doesn't exist
# Alert the user if they select an option on the main menu that doesn't exist

# Function for the Display Menu
def displayMenu():
    print("\nWelcome to the To Do List Application!")
    print("Please choose an option:")
    print("1. Add Task")
    print("2. View Tasks")
    print("3. Delete Task")
    print("4. Quit Application")

# Function for adding a task
def addTask(tasks):
    task = input("Enter the task you want to add: ")
    tasks.append(task)
    print(f"\nTask '{task}' added successfully!")

# Function for viewing tasks
def viewTasks(tasks):
    if not tasks:
        print("\nNo tasks to view.")
    else:
        print("\nYour tasks:")
        for index, task in enumerate(tasks, start=1):
            print(f"{index}. {task}")
        
# Function for deleting a task  
def deleteTask(tasks):
    if not tasks:
        print("\nNo tasks to delete.")
    else:
        viewTasks(tasks)
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

# Main function to run the application    
def main():
    tasks = []
    while True:
        displayMenu()
        # Sets choice to value of None fixing bug where the program would crash if the user entered a non-integer value
        choice = None
        try:
            choice = int(input("Enter your choice: "))
            if choice == 1:
                addTask(tasks)
            elif choice == 2:
                viewTasks(tasks)
            elif choice == 3:
                deleteTask(tasks)
            # Uses the break feature to shut down the application for the Qudit Application option
            elif choice == 4:
                print("Thank you for using the To Do List Application!")
                break
            else:
                print("\nInvalid option. Please try again.")
        except ValueError:
            print("\nPlease enter a valid number.")
        except Exception as e:
            print(f"\nAn unexpected error occurred: {e}")
        finally:
            # Will NOT print if user chose option 4 to quit the application
            if choice != 4:
                print("Returning to main menu...\n")

# The if statement below is in place to ensure that the main function is only called when this script is run directly, not when it is imported as a module.
# This is important to ensure that code is not run unintentionally when importing the module elsewhere.
if __name__ == "__main__":
    main()
