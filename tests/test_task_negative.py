"""
RanZiz AI Negative Task Test
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


class TaskNegativeTest(unittest.TestCase):

    def test_empty_manager(self):

        manager = TaskManager()

        info = manager.info()

        self.assertEqual(info["total"], 0)
        self.assertEqual(info["pending"], 0)
        self.assertEqual(info["running"], 0)
        self.assertEqual(info["completed"], 0)

    def test_finish_without_start(self):

        task = Task("Chat", "chat")

        task.finish()

        self.assertEqual(task.status, "done")

    def test_fail_task(self):

        task = Task("Chat", "chat")

        task.fail()

        self.assertEqual(task.status, "failed")


if __name__ == "__main__":
    unittest.main(verbosity=2)