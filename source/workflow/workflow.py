"""
RanZiz AI Workflow
Version 1.0
"""


class Workflow:


    def __init__(self, name, tasks=None):

        self.name = name

        self.tasks = tasks or []


    def add_task(self, task):

        self.tasks.append(task)


    def get_tasks(self):

        return self.tasks


    def __repr__(self):

        return (
            f"Workflow("
            f"name={self.name}, "
            f"tasks={len(self.tasks)}"
            f")"
        )