import os
import unittest
from storage import save_tasks, load_tasks

class TestStorage(unittest.TestCase):
    def test_load_task_without_json(self):
        self.assertEqual(load_tasks("non_existing_file"),{})

    def test_save_task(self):
        tasks = {"learn python" : True}
        filename ="test_tasks.json"
        save_tasks(tasks,filename)
        loaded_task = load_tasks(filename)
        self.assertEqual(loaded_task, tasks)

        os.remove(filename)

    