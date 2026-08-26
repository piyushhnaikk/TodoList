import os
import unittest
from storage import save_tasks, load_tasks

class TestStorage(unittest.TestCase):
    def setUp(self):
        self.filename = "test_tasks.json"
        
    def test_load_task_without_json(self):
        self.assertEqual(load_tasks("non_existing_file"), {})

    def test_save_task(self):
        tasks = {"learn python" : True}
        save_tasks(tasks,self.filename)
        loaded_task = load_tasks(self.filename)
        self.assertEqual(loaded_task, tasks)

    def test_load_corrupted_json(self):
        with open(self.filename, "w") as file:
            file.write("This is not valid JSON")

        self.assertEqual(load_tasks(self.filename), {})

    def tearDown(self):
        if os.path.exists(self.filename):
            os.remove(self.filename)
