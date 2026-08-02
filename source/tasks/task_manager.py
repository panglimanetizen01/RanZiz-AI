"""
RanZiz AI Task Manager
Version 1.0
"""

from source.tasks.task import Task


class TaskManager:

    def __init__(self):

        self.tasks = []

    def add(self, task):

        if isinstance(task, Task):

            self.tasks.append(task)

    def next(self):

        for task in self.tasks:

            if task.status == "pending":

                return task

        return None

    def pending(self):

        return [
            task
            for task in self.tasks
            if task.status == "pending"
        ]

    def running(self):

        return [
            task
            for task in self.tasks
            if task.status == "running"
        ]

    def completed(self):

        return [
            task
            for task in self.tasks
            if task.status == "done"
        ]

    def count(self):

        return len(self.tasks)

    def clear(self):

        self.tasks.clear()

    def info(self):

        return {
            "total": len(self.tasks),
            "pending": len(self.pending()),
            "running": len(self.running()),
            "completed": len(self.completed()),
        }