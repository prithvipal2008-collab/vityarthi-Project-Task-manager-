📝 Python Console Task Manager   
🚀 Overview of the Project
This project is a simple command-line interface (CLI) Task Manager implemented in Python. It allows users to efficiently manage their daily tasks using a basic list structure. The program initializes with a user-specified number of tasks and then presents a menu to perform various operations until the user chooses to exit. It's a foundational script ideal for learning basic Python input/output, list manipulation, and control flow structures like while loops and if/elif/else statements.

✨ Features
The Task Manager provides the following functionalities through its interactive menu:

Add a task: Appends a new task string to the list.

Update a task: Allows the user to replace an existing task with a new one (updates by task content).

Delete a task: Removes a specified task from the list (removes by task content).

View all tasks: Prints the entire list of current tasks.

Exit: Terminates the program loop.

Input Validation: Includes basic error handling to ensure the menu choice is a number.

🛠️ Technologies/Tools Used
Programming Language: Python 3.x

⚙️ Steps to Install & Run the Project
Since this is a single, self-contained Python script, installation is straightforward.

1. Save the Code
Save the Python code provided in your prompt into a file named task_manager.py.
def task():
        tasks = []
        print("--- TASK MANAGER ---")
        n = int(input("How many tasks do you want to add today ? "))

        for i in range(n):

            t = input(f"Enter task {i+1}: ")

            tasks.append(t)
        print("Your tasks for today is :")
        print(tasks)
        while True :
            print("\n Choose an option:")
            print("1 Add a task")
            print("2 Update a task")
            print("3 Delete a task")
            print("4 View all tasks")
            print("5 Exit")
            try:

                choice = int(input("Enter your choice : "))

            except:

                print("Enter a number.")

                continue

            if choice == 1:

                new_task = input("Enter your new task: ")

                tasks.append(new_task)

                print("Your new task has been add ")

            elif choice == 2:
                old = input("Which task do you want to update? ")
                if old in tasks:
                    new = input("Enter your new task: ")
                    idx = tasks.index(old)
                    tasks[idx] = new
                    print("Task had been Updated.")

                else:
                    print("Task not found.")
            elif choice == 3:
                d = input("Which task do you want to delete ? ")
                if d in tasks:
                    tasks.remove(d)
                    print("Task Deleted.")
                else:
                    print("Task not found.")
            elif choice == 4:
                print("Current tasks:", tasks)
            elif choice == 5:
                print("Exiting....")
                break
            else:
                print("Invalid choice. enter 1-5.")
task()
   
3. Run the Script
Open your terminal or command prompt, navigate to the directory where you saved task_manager.py, and run the file using the Python interpreter:
python task_manager.py
🧪 Instructions for Testing
When you run the script, follow these steps to test all functionalities:

1. Initial Setup: The program will first ask you: How many tasks do you want to add today ?. Enter a number (e.g., 2) and input the tasks (e.g., Buy groceries, Finish report).

2. Test Option 1 (Add a task):

Enter 1.

Input a new task (e.g., Call mom).

Verify the output: Your new task has been added.

3. Test Option 2 (Update a task):

Enter 2.

Input an existing task to change (e.g., Buy groceries).

Input the new task (e.g., Buy organic groceries).

Verify the output: Task has been Updated.

4. Test Option 3 (Delete a task):

Enter 3.

Input a task to delete (e.g., Finish report).

Verify the output: Task Deleted.

5. Test Option 4 (View all tasks):

Enter 4.

Check that the output list reflects the additions, updates, and deletions (['Buy organic groceries', 'Call mom'] in this example).

6. Test Option 5 (Exit):

Enter 5.

Verify the output: Exiting.... and the program terminates.

7. Error Handling Test: Try to enter a letter or a number outside of 1-5 for the menu choice and verify the appropriate error message is shown, and the menu reappears.
