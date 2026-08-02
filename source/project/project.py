"""
RanZiz AI Project
Version 1.0
"""


class Project:

    def __init__(self, project_id, title):

        self.id = project_id

        self.title = title

        self.status = "CREATED"

        self.tasks = []

        self.assets = []

        self.outputs = []

    def add_task(self, task):

        self.tasks.append(task)

    def add_asset(self, asset):

        self.assets.append(asset)

    def add_output(self, output):

        self.outputs.append(output)

    def complete(self):

        self.status = "COMPLETED"