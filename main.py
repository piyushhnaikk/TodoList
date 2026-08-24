import tasks as tks
import storage as stor
import ui

todo = stor.load_tasks()

ui.display_options()
command = ui.get_command()

while command != 5:

    match command:
        case 1:
            task = ui.take_input()
            print(tks.add_task(todo, task))

        case 2:
            ui.view_tasks(todo)

        case 3:
            task = ui.take_input()
            print(tks.complete_task(todo, task))

        case 4:
            task = ui.take_input()
            print(tks.delete_task(todo, task))

    ui.display_options()
    command = ui.get_command()

stor.save_tasks(todo)