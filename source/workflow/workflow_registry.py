"""
RanZiz AI Workflow Registry
Version 1.0
"""


class WorkflowRegistry:


    def __init__(self):

        self.workflows = {}


    def register(self, workflow):

        self.workflows[workflow.name] = workflow

        return True


    def unregister(self, name):

        if name in self.workflows:

            del self.workflows[name]

            return True

        return False


    def get(self, name):

        return self.workflows.get(name)


    def list_workflows(self):

        return list(self.workflows.keys())