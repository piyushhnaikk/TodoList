import tasks as tks
import storage as stor

todo = stor.load_tasks()

print("==========================================================")
print("                   MY PERSONAL ASSISTANT                  ")
print("==========================================================\n")

print("1. Add Task")
print("2. View Task")
print("3. Complete Task")
print("4. Delete Task")
print("5. Exit\n")

command = int(input("Enter choice:  "))

while (command != 5):
    match command:
        case 1:
           tks.add_task(todo) 

        case 2:
            tks.view_tasks(todo)

        case 3:
            tks.complete_task(todo)

        case 4:
            tks.delete_task(todo)

    command = int(input("Enter choice:  "))

stor.save_tasks(todo)
