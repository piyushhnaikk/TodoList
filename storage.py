import json


def save_tasks(tasks, filename = "tasks.json"):
    with open(filename, "w") as file:
        json.dump(tasks, file)


def load_tasks(filename = "tasks.json"):
    try:
        with open(filename, "r") as file:
            return json.load(file)
    except FileNotFoundError:
        return {}
    except json.JSONDecodeError:
        return {}