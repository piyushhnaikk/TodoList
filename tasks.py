def add_task(tasks):
    task = input("Enter Task: ").lower()
    tasks[task] = False
    print("Task added Successfully! \n\n ")

def view_tasks(tasks):
    num = 1
    for i in tasks.keys():
        print(num, ". ",i, end = "" )
        if not tasks[i]:
            print("[Pending]")
        else:
            print("[Completed]")
        num += 1
        print("\n\n")
        
def complete_task(tasks):
    task = input("Enter task: ").lower()

    if task in tasks:
        tasks[task] = True
        print("Task marked completed\n\n")
    else:
        print("Task not present in list\n\n")

def delete_task(tasks):
    task = input("Enter task: ").lower()
    if task in tasks:
        del tasks[task] 
        print("Task deleted successfully\n\n")
    else:
        print("Task not present in list\n\n")                                           