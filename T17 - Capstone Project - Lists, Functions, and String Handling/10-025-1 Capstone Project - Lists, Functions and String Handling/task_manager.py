# Notes: 
# 1. Use the following username and password to access the admin rights 
# username: admin
# password: password
# 2. Ensure you open the whole folder for this task in VS Code otherwise the 
# program will look in your root directory for the text files.

#=====importing libraries===========
import os
from datetime import datetime, date

# Define the datetime format string used in the code
DATETIME_STRING_FORMAT = "%Y-%m-%d"

# Function to register a new user.
def reg_user(username_password):
    # Input new username
    new_username = input("New Username: ")

      # Check if the username already exists
    if new_username in username_password:
        print("Error: Username already exists. Please try a different username.")
        return False
     
      # Input new password and confirm password
    new_password = input("New Password: ")
    confirm_password = input("Confirm Password: ")
    
    # Check if passwords match
    if new_password == confirm_password:
        print("New user added")
        # Add the new user to the username_password dictionary
        username_password[new_username] = new_password
        
        # Update user.txt file with new user
        with open("user.txt", "a", encoding="utf-8") as out_file:
            out_file.write(f"{new_username};{new_password}\n")
        return True
    else:
        print("Error: Passwords do not match.")
        return False

# Function to add a new task.
def add_task(task_list, username):

     # Input task details
    username = input("Name of person assigned to task: ")
    task_title = input("Title of Task: ")
    task_description = input("Description of Task: ")
    
    # Input and validate due date
    while True:
        try:
            task_due_date = input("Due date of task (YYYY-MM-DD): ")
            due_date_time = datetime.strptime(task_due_date, DATETIME_STRING_FORMAT)
            break
        except ValueError:
            print("Invalid datetime format. Please use the format specified")

    curr_date = date.today()
    
    # Create a new task dictionary
    new_task = {
        "username": username,
        "title": task_title,
        "description": task_description,
        "due_date": due_date_time,
        "assigned_date": curr_date,
        "completed": False
    }
    
    # Add the new task to the task_list
    task_list.append(new_task)

    # Update tasks.txt file with new task
    with open("tasks.txt", "a", encoding="utf-8") as task_file:
        str_attrs = [
            new_task['username'],
            new_task['title'],
            new_task['description'],
            new_task['due_date'].strftime(DATETIME_STRING_FORMAT),
            new_task['assigned_date'].strftime(DATETIME_STRING_FORMAT),
            "Yes" if new_task['completed'] else "No"
        ]
        task_file.write(";".join(str_attrs) + "\n")

    print("Task successfully added.")

# Function to view all tasks.
def view_all(task_list):
    for t in task_list:
        # Display task information
        disp_str = f"Task: \t\t {t['title']}\n"
        disp_str += f"Assigned to: \t {t['username']}\n"
        disp_str += f"Date Assigned: \t {t['assigned_date'].strftime(DATETIME_STRING_FORMAT)}\n"
        disp_str += f"Due Date: \t {t['due_date'].strftime(DATETIME_STRING_FORMAT)}\n"
        disp_str += f"Task Description: \n {t['description']}\n"
        print(disp_str)

# Function to view tasks assigned to the current user
def view_mine(task_list, curr_user, username_password):
    for i, t in enumerate(task_list, 1):
        if t['username'] == curr_user:
            # Display task information
            disp_str = f"Task {i}:\n"
            disp_str += f"  Title: {t['title']}\n"
            disp_str += f"  Assigned to: {t['username']}\n"
            disp_str += f"  Date Assigned: {t['assigned_date'].strftime(DATETIME_STRING_FORMAT)}\n"
            disp_str += f"  Due Date: {t['due_date'].strftime(DATETIME_STRING_FORMAT)}\n"
            disp_str += f"  Task Description: {t['description']}\n"
            disp_str += f"  Completed: {t['completed']}\n"
            print(disp_str)
            
            # Prompt user for task selection
            task_choice = input("Enter the number of the task you want to select, or enter -1 to return to the main menu: ")

            if task_choice.isdigit() and 1 <= int(task_choice) <= len(task_list):
                # Process selected task
                selected_task_index = int(task_choice) - 1
                selected_task = task_list[selected_task_index]

                action_choice = input("Choose an action:\n1. Mark as Complete\n2. Edit Task\nEnter the corresponding number: ")

                if action_choice == '1':
                    selected_task['completed'] = 'Yes'
                    print("Task marked as complete.")
                elif action_choice == '2' and selected_task['completed'] == 'No':
                    # Edit task details
                    new_username = input("Enter the new username (press Enter to keep the current username): ")
                    new_due_date = input("Enter the new due date in the format YYYY-MM-DD (press Enter to keep the current due date): ")

                    if new_username:
                        selected_task['username'] = new_username
                    if new_due_date:
                        selected_task['due_date'] = datetime.strptime(new_due_date, DATETIME_STRING_FORMAT)
                    
                    # Update the task in the tasks.txt file
                    update_task_file(task_list)

                    print("Task edited successfully.")
                elif action_choice == '2' and selected_task['completed'] == 'Yes':
                    print("Error: Completed tasks cannot be edited.")
                else:
                    print("Invalid input. No changes were made.")

# Function to update the tasks.txt file
def update_task_file(task_list):
    with open("tasks.txt", "w", encoding="utf-8") as task_file:
        for t in task_list:
            str_attrs = [
                t['username'],
                t['title'],
                t['description'],
                t['due_date'].strftime(DATETIME_STRING_FORMAT),
                t['assigned_date'].strftime(DATETIME_STRING_FORMAT),
                "Yes" if t['completed'] else "No"
            ]
            task_file.write(";".join(str_attrs) + "\n")

# Function to generate reports.
def generate_reports(task_list, username_password):
    total_tasks = len(task_list)
    completed_tasks = sum(task['completed'] == 'Yes' for task in task_list)
    uncompleted_tasks = total_tasks - completed_tasks
    overdue_tasks = sum(1 for task in task_list if not task['completed'] and task['due_date'].date() < datetime.now().date())
    percentage_incomplete = (uncompleted_tasks / total_tasks) * 100
    percentage_overdue = (overdue_tasks / total_tasks) * 100
    
    # Write task overview to task_overview.txt
    with open("task_overview.txt", "w", encoding="utf-8") as task_overview_file:
        task_overview_file.write(f"Total number of tasks: {total_tasks}\n")
        task_overview_file.write(f"Total number of completed tasks: {completed_tasks}\n")
        task_overview_file.write(f"Total number of uncompleted tasks: {uncompleted_tasks}\n")
        task_overview_file.write(f"Total number of tasks overdue: {overdue_tasks}\n")
        task_overview_file.write(f"Percentage of tasks incomplete: {percentage_incomplete:.2f}%\n")
        task_overview_file.write(f"Percentage of tasks overdue: {percentage_overdue:.2f}%\n")

    total_users = len(username_password.keys())
    
    # Write user overview to user_overview.txt
    with open("user_overview.txt", "w", encoding="utf-8") as user_overview_file:
        user_overview_file.write(f"Total number of users: {total_users}\n")
        user_overview_file.write(f"Total number of tasks: {total_tasks}\n")

        for user in username_password.keys():
            user_tasks = [task for task in task_list if task['username'] == user]
            total_user_tasks = len(user_tasks)
            completed_user_tasks = sum(task['completed'] == 'Yes' for task in user_tasks)
            uncompleted_user_tasks = total_user_tasks - completed_user_tasks
            overdue_user_tasks = sum(1 for task in user_tasks if not task['completed'] and task['due_date'].date() < datetime.now().date())
            
            # Calculate percentages
            if total_tasks != 0:
                percentage_user_tasks = (total_user_tasks / total_tasks) * 100
            else:
                percentage_user_tasks = 0

            percentage_completed_user_tasks = (completed_user_tasks / total_user_tasks) * 100
            percentage_uncompleted_user_tasks = (uncompleted_user_tasks / total_user_tasks) * 100
            percentage_overdue_user_tasks = (overdue_user_tasks / total_user_tasks) * 100
            
            # Write user-specific information to user_overview.txt
            user_overview_file.write(f"\nUser: {user}\n")
            user_overview_file.write(f"  Total number of tasks assigned: {total_user_tasks}\n")
            user_overview_file.write(f"  Percentage of total tasks assigned: {percentage_user_tasks:.2f}%\n")
            user_overview_file.write(f"  Percentage of completed tasks: {percentage_completed_user_tasks:.2f}%\n")
            user_overview_file.write(f"  Percentage of uncompleted tasks: {percentage_uncompleted_user_tasks:.2f}%\n")
            user_overview_file.write(f"  Percentage of overdue tasks: {percentage_overdue_user_tasks:.2f}%\n")

# Function to display statistics.
def display_statistics(task_list, username_password):
    total_tasks = len(task_list)
    completed_tasks = sum(1 for task in task_list if task['completed'] == 'Yes')
    uncompleted_tasks = total_tasks - completed_tasks
    overdue_tasks = sum(1 for task in task_list if not task['completed'] and task['due_date'].date() < datetime.now().date())
    percentage_incomplete = (uncompleted_tasks / total_tasks) * 100
    percentage_overdue = (overdue_tasks / total_tasks) * 100
    
    # Print statistics to console
    print(f"Total number of tasks: {total_tasks}")
    print(f"Total number of completed tasks: {completed_tasks}")
    print(f"Total number of uncompleted tasks: {uncompleted_tasks}")
    print(f"Total number of tasks overdue: {overdue_tasks}")
    print(f"Percentage of tasks incomplete: {percentage_incomplete:.2f}%")
    print(f"Percentage of tasks overdue: {percentage_overdue:.2f}%")
    
    # Write statistics to task_overview.txt
    with open("task_overview.txt", "w", encoding="utf-8") as task_overview_file:
        task_overview_file.write(f"Total number of tasks: {total_tasks}\n")
        task_overview_file.write(f"Total number of completed tasks: {completed_tasks}\n")
        task_overview_file.write(f"Total number of uncompleted tasks: {uncompleted_tasks}\n")
        task_overview_file.write(f"Total number of tasks overdue: {overdue_tasks}\n")
        task_overview_file.write(f"Percentage of tasks incomplete: {percentage_incomplete:.2f}%\n")
        task_overview_file.write(f"Percentage of tasks overdue: {percentage_overdue:.2f}%\n")

    total_users = len(username_password.keys())
    
    # Write user statistics to user_overview.txt
    with open("user_overview.txt", "w", encoding="utf-8") as user_overview_file:
        user_overview_file.write(f"Total number of users: {total_users}\n")
        user_overview_file.write(f"Total number of tasks: {total_tasks}\n")

        for user in username_password.keys():
            user_tasks = [task for task in task_list if task['username'] == user]
            total_user_tasks = len(user_tasks)
            completed_user_tasks = sum(task['completed'] == 'Yes' for task in user_tasks)
            uncompleted_user_tasks = total_user_tasks - completed_user_tasks
            overdue_user_tasks = sum(1 for task in user_tasks if not task['completed'] and task['due_date'].date() < datetime.now().date())
            
            # Calculate percentages
            if total_tasks != 0:
                percentage_user_tasks = (total_user_tasks / total_tasks) * 100
            else:
                percentage_user_tasks = 0

            percentage_completed_user_tasks = (completed_user_tasks / total_user_tasks) * 100
            percentage_uncompleted_user_tasks = (uncompleted_user_tasks / total_user_tasks) * 100
            percentage_overdue_user_tasks = (overdue_user_tasks / total_user_tasks) * 100
            
            # Write user-specific information to user_overview.txt
            user_overview_file.write(f"\nUser: {user}\n")
            user_overview_file.write(f"  Total number of tasks assigned: {total_user_tasks}\n")
            user_overview_file.write(f"  Percentage of total tasks assigned: {percentage_user_tasks:.2f}%\n")
            user_overview_file.write(f"  Percentage of completed tasks: {percentage_completed_user_tasks:.2f}%\n")
            user_overview_file.write(f"  Percentage of uncompleted tasks: {percentage_uncompleted_user_tasks:.2f}%\n")
            user_overview_file.write(f"  Percentage of overdue tasks: {percentage_overdue_user_tasks:.2f}%\n")

# Main function
def main():
    logged_in = False
    curr_user = ""
    username_password = {}

    # Load existing usernames from user.txt
    try:
        with open("user.txt", "r", encoding="utf-8") as in_file:
            for line in in_file:
                user_info = line.strip().split(';')
                if len(user_info) == 2:
                    user, password = user_info
                    username_password[user] = password
                else:
                    print(f"Warning: Ignoring invalid line in user.txt: {line}")
    except FileNotFoundError:
        # If the file does not exist, proceed with an empty dictionary
        pass

    # Read existing task data from tasks.txt
    task_list = []
    with open("tasks.txt", 'r', encoding="utf-8") as task_file:
        task_data = task_file.read().split("\n")
        task_data = [t for t in task_data if t != ""]

    # Parse existing tasks and populate task_list
    task_list = []
    for t_str in task_data:
        curr_t = {}

        # Split by semicolon and manually add each component
        task_components = t_str.split(";")
        # Check if task_components has enough elements
        if len(task_components) >= 6:
            curr_t['username'] = task_components[0]
            curr_t['title'] = task_components[1]
            curr_t['description'] = task_components[2]
            curr_t['due_date'] = datetime.strptime(task_components[3], DATETIME_STRING_FORMAT)
            curr_t['assigned_date'] = datetime.strptime(task_components[4], DATETIME_STRING_FORMAT)
            curr_t['completed'] = True if task_components[5] == "Yes" else False

            task_list.append(curr_t)
        else:
            print(f"Warning: Ignoring invalid line in tasks.txt: {t_str}")
    
    # User login
    while not logged_in:
        print("LOGIN")
        curr_user = input("Username: ")
        curr_pass = input("Password: ")
        if curr_user not in username_password.keys():
            print("User does not exist")
            continue
        elif username_password[curr_user] != curr_pass:
            print("Wrong password")
            continue
        else:
            print("Login Successful!")
            logged_in = True
    
    # Main menu
    while True:
        print()
        menu = input('''Select one of the following Options below:
    r - Registering a user
    a - Adding a task
    va - View all tasks
    vm - View my task
    gr - Generate reports
    ds - Display statistics
    e - Exit
    : ''').lower()

        if menu == 'r':
            # Register a new user
            reg_user(username_password)

        elif menu == 'a':
            # Add a new task
            add_task(task_list, curr_user)

        elif menu == 'va':
            # View all tasks
            view_all(task_list)

        elif menu == 'vm':
            # View tasks assigned to the current user
            view_mine(task_list, curr_user, username_password)

        elif menu == 'gr':
            # Generate reports
            generate_reports(task_list, username_password)

        elif menu == 'ds' and curr_user == 'admin':
            # Display statistics (only accessible to admin)
            display_statistics(task_list, username_password)

        elif menu == 'e':
            print('Goodbye!!!')
            exit()

        else:
            print("You have made a wrong choice, Please Try again")

if __name__ == "__main__":
    main()
