def display_options():
    print("==========================================================")
    print("                   MY PERSONAL ASSISTANT                  ")
    print("==========================================================\n")

    print("1. Add Task")
    print("2. View Task")
    print("3. Complete Task")
    print("4. Delete Task")
    print("5. Exit\n")


def get_command():
    isValid = False

    while not isValid:
        command = input("Enter choice:  ")

        try:
            command = int(command)

            if command in [1, 2, 3, 4, 5]:
                isValid = True
            else:
                print("Invalid option! please choose a number between 1 and 5")

        except ValueError:
            print("Invalid option! please choose a number between 1 and 5")

    return command


def take_input():
    task = input("Enter task: ").lower()
    return task


def view_tasks(tasks):
    if tasks == {}:
        print("No tasks found!\n")
        return
    
    num = 1

    for i in tasks.keys():
        print(f"{num}. {i}", end="   ")

        if not tasks[i]:
            print("[Pending]")
        else:
            print("[Completed]")

        num += 1

    print("\n\n")