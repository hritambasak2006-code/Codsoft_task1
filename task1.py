tasks = []

while True:

    print("\n===== TO-DO LIST =====")
    print("1. View Tasks")
    print("2. Add Task")
    print("3. Update Task")
    print("4. Delete Task")
    print("5. Exit")

    choice = input("Enter your choice: ")

    # VIEW TASKS
    if choice == "1":

        if len(tasks) == 0:
            print("No tasks available.")

        else:
            print("\nYour Tasks:")

            for i in range(len(tasks)):
                print(i + 1, ".", tasks[i])

    # ADD TASK
    elif choice == "2":

        task = input("Enter new task: ")

        tasks.append(task)

        print("Task added successfully!")

    # UPDATE TASK
    elif choice == "3":

        if len(tasks) == 0:
            print("No tasks to update.")

        else:
            for i in range(len(tasks)):
                print(i + 1, ".", tasks[i])

            num = int(input("Enter task number to update: "))

            new_task = input("Enter new task: ")

            tasks[num - 1] = new_task

            print("Task updated!")

    # DELETE TASK
    elif choice == "4":

        if len(tasks) == 0:
            print("No tasks to delete.")

        else:
            for i in range(len(tasks)):
                print(i + 1, ".", tasks[i])

            num = int(input("Enter task number to delete: "))

            removed = tasks.pop(num - 1)

            print("Deleted task:", removed)

    # EXIT
    elif choice == "5":

        print("Exiting program...")
        break

    else:
        print("Invalid choice!")
