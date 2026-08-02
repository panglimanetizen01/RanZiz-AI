"""
RanZiz AI Task Manager Test
Version 1.0
"""

import sys
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent

if str(ROOT) not in sys.path:
    sys.path.insert(0, str(ROOT))

from source.tasks.task import Task
from source.tasks.task_manager import TaskManager


class TaskManagerTest(unittest.TestCase):

    def setUp(self):
        self.manager = TaskManager()

    def test_add_task(self):
        task = Task("Chat", "chat")
        self.manager.add(task)

        info = self.manager.info()

        self.assertEqual(info["total"], 1)
        self.assertEqual(info["pending"], 1)

    def test_running_task(self):
        task = Task("Music", "music")
        self.manager.add(task)
        task.start()

        info = self.manager.info()

        self.assertEqual(info["running"], 1)

    def test_completed_task(self):
        task = Task("Image", "image")
        self.manager.add(task)
        task.start()
        task.finish()

        info = self.manager.info()

        self.assertEqual(info["completed"], 1)


if __name__ == "__main__":
    unittest.main(verbosity=2)