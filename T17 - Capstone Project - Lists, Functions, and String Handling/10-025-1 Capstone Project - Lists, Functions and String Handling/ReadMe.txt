Project Name - Task manager

Project Details:

Description:

The Task Manager Project is a Python program developed for the Hyperion Development 
Software Engineering Bootcamp's level 1 task requirements. This program aids small businesses 
in managing team tasks, incorporating features like task creation, storage, display, and editing, 
all facilitated through text files.

The code comprises six functions, each catering to specific user menu options. These functions 
execute actions based on user input, interacting with lists and dictionaries to store user and task data. 
Upon execution, the program prompts users to log in, verifying their credentials against stored 
information. Incorrect inputs trigger error messages until accurate details are provided.

Following successful login, users access a menu offering options such as user registration, 
task addition, task viewing, user-specific task viewing, report generation, and program exit. 
The 'admin' user has an additional 'display statistics' option. Users navigate through the menu in a 
'while' loop, allowing repeated interactions.

User choices trigger corresponding functions; for instance, registering a new user involves 
executing the 'reg_user()' function, prompting for and storing user information. Task addition 
follows a similar process, with information stored in dictionaries and external text files.

For task viewing options, users can see all tasks or only those assigned to them. Task editing 
is available, and the 'admin' user can display statistics. Report generation, executed by the sixth 
function, creates 'task_overview.txt' and 'user_overview.txt' text files with task and user statistics.

To use the program, clone the repository to a local directory and install Python. Open the Python IDLE, 
load 'taskmanager.py', and run the program. For report viewing, generated text files can be opened with 
a text editor like Notepad.

Ensure Python is installed:

Python Interpreter.

Text editor for viewing files:

Notepad++.

Usage of functions in the project:

login:

	have user enter a username, then enter a password.
		check if username/password combination appears in "user.txt" file
		if both appear in combination continue to menu
		if one or both do not match, print error message

register user:
	
	Only allow admin user to access this option
		use an if statement to check if user is admin upon login
		if result false, display error message if user attempts to add a new user

	prompt user for a new username, password and confirm password
		check that username doesn't exist already, print error message if it does
		check that password and confirmed password match, print error message if not
		write username/password combination to file "user.txt"
	
add task:

	prompt user for username to which the task is assigned
		check that user exists within "user.txt" file
		if not, display error message and prompt again
	
	prompt user for task title
	
	prompt user for task description
	
	prompt user for task due date
	
	Write task to file "tasks.txt", defaulting completed to "No" and date assigned to current date
		import module datetime
		use input today = datetime.date.today()
			for formatting, use today.strftime(%x). output result will formatted to local version
			otherwise, use today.strftime(%d %b %Y) to output as dd mmm yyyy

view all tasks
	
	display each task in an easy to ready format

view my tasks
	
	display only tasks assigned to logged in user in an easy to read format

display statistics
	
	only allow admin user to see and access this option
		use an if statement to check if user is admin upon login
		if result false, display error message if user attempts to display statistics
	
	when selected, option displays total number of tasks and total number of users

Output of the Project:

user.txt output:

Tom;Tom123
James;james123
Lilly;lilly123

tasks.txt output:

Tom;Senior Developer;Add functionality to task manager;2024-03-03;2024-02-28;No
James;Lead;Checking the functionality of task manager;2024-03-05;2024-02-28;No
Lilly;Tester;testing the functionality of task manager;2024-03-07;2024-02-28;No

task_overvew.txt output:

Total number of tasks: 3
Total number of completed tasks: 1
Total number of uncompleted tasks: 2
Total number of tasks overdue: 1
Percentage of tasks incomplete: 83.33%
Percentage of tasks overdue: 16.67%

user_overview.txt output:

Total number of users: 3
Total number of tasks: 3

User: Tom
  Total number of tasks assigned: 1
  Percentage of total tasks assigned: 16.67%
  Percentage of completed tasks: 0.00%
  Percentage of uncompleted tasks: 100.00%
  Percentage of overdue tasks: 0.00%

User: James
  Total number of tasks assigned: 1
  Percentage of total tasks assigned: 16.67%
  Percentage of completed tasks: 100.00%
  Percentage of uncompleted tasks: 0.00%
  Percentage of overdue tasks: 0.00%

User: Lilly
  Total number of tasks assigned: 1
  Percentage of total tasks assigned: 16.67%
  Percentage of completed tasks: 0.00%
  Percentage of uncompleted tasks: 100.00%
  Percentage of overdue tasks: 0.00%

