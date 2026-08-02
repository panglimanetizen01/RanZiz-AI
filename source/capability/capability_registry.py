"""
RanZiz AI Capability Registry
Version 1.0
"""


class CapabilityRegistry:


    def __init__(self):

        self.executors = {}


    def register(
        self,
        name,
        executor
    ):

        self.executors[name] = executor


    def get(
        self,
        name
    ):

        return self.executors.get(name)


    def list(self):

        return list(
            self.executors.keys()
        )
