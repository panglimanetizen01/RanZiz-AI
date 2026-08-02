"""
RanZiz AI Workflow Context
Version 1.0
"""


class WorkflowContext:


    def __init__(self):

        self.data = {}


    def set(
        self,
        key,
        value
    ):

        self.data[key] = value


    def get(
        self,
        key,
        default=None
    ):

        return self.data.get(
            key,
            default
        )


    def all(self):

        return dict(
            self.data
        )


    def clear(self):

        self.data.clear()