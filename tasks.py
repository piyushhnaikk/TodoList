def add_task(tasks: dict, task: str):
    if task in tasks:
        return "Task already Exists!\n"
    
    tasks[task] = False
    return "Task added Successfully! \n"


def complete_task(tasks: dict, task: str):
    if task in tasks:
        if not tasks[task]:
            tasks[task] = True
            return "Task marked completed\n"
        else:
            return "Task already completed!"
    else:
        return "Task not present in list\n"


def delete_task(tasks: dict, task: str):
    if task in tasks:
        del tasks[task]
        return "Task deleted successfully\n"
    else:
        return "Task not present in list\n"