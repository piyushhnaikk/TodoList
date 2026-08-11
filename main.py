import tasks as tks
import storage as stor
import ui

todo = stor.load_tasks()

ui.display_options()

command = ui.get_command()

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
    
    ui.display_options()
    command = ui.get_command()

stor.save_tasks(todo)
