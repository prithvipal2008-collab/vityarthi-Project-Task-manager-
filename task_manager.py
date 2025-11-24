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
