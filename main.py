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

from display_menu import display_menu
from add_task import add_task
from view_task import view_tasks
from delete_task import delete_task
        


# Main function to run the application    
def main():
    tasks = []
    while True:
        display_menu()
        # Sets choice to value of None fixing bug where the program would crash if the user entered a non-integer value
        choice = None
        try:
            choice = int(input("Enter your choice: "))
            if choice == 1:
                add_task(tasks)
            elif choice == 2:
                view_tasks(tasks)
            elif choice == 3:
                delete_task(tasks)
            # Uses the break feature to shut down the application for the Quit Application option
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
