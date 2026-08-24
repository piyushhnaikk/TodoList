from tasks import add_task, complete_task,delete_task
import unittest

class TestTasks(unittest.TestCase):
    def test_add_task(self):
        tasks = {}

        add_task(tasks, "Learn python")
        self.assertIn("Learn python", tasks)
        self.assertFalse(tasks["Learn python"])

    def test_add_task_duplicate(self):
        tasks = {"Learn python" : True}

        self.assertEqual(add_task(tasks, "Learn python"), "Task already Exists!\n")

    def test_complete_task_IncompleteOne(self):
        tasks = {"learn python" : False}

        complete_task(tasks, "learn python")
        self.assertTrue(tasks["learn python"])

    def test_complete_task_completeOne(self):
        tasks = {"learn git" : True}
        self.assertEqual(complete_task(tasks, "learn git"),"Task already completed!")

    def test_complete_task_non_existing(self):
        tasks = {"learn git" : True}
        self.assertEqual(complete_task(tasks, "learn java"),"Task not present in list\n")

    def test_delete_task_completed(self):
        tasks = {"learn python" : False, "learn git" : True}
        delete_task(tasks, "learn git")
        self.assertNotIn("learn git", tasks)

    def test_delete_task_incomplete(self):
        tasks = {"learn python" : False, "learn git" : True}
        delete_task(tasks, "learn python")
        self.assertNotIn("learn python", tasks)

    def test_delete_task_non_existing(self):
        tasks = {"learn python" : False, "learn git" : True}
        self.assertEqual(delete_task(tasks, "learn java"), "Task not present in list\n")



if __name__ == "__main__":
    unittest.main()