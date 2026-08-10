print("==========================================================\n")
print("                   MY PERSONAL ASSISTANT                  \n")
print("==========================================================\n\n")

print("1. Add Task")
print("2. View Task")
print("3. Complete Task")
print("4. Delete Task")
print("5. Exit\n\n")

command = int(input("Enter choice:  "))
tasks = {}

while (command != 5):
    match command:
        case 1:
            task = input("Enter task: ").lower()
            tasks[task] = False
            print("Task added sucessfully \n\n")

        case 2:
            num = 1
            for i in tasks.keys():
                print(num, ". ",i, end = "" )
                if not tasks[i]:
                    print("[Pending]")
                else:
                    print("[Completed]")
                num += 1


        case 3:
            task = input("Enter task: ").lower()

            if task in tasks:
                tasks[task] = True
                print("Task marked completed\n\n")
            else:
                print("Task not present in list\n\n")

        case 4:
            task = input("Enter task: ").lower()
            if task in tasks:
                del tasks[task] 
                print("Task deleted sucessfully\n\n")
            else:
                print("Task not present in list\n\n")



    command = int(input("Enter choice:  "))
