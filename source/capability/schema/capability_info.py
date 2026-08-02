"""
RanZiz AI Capability Info
Version 2.0
"""


class CapabilityInfo:


    def __init__(
        self,
        name,
        category,
        description,
        inputs,
        outputs,
        requires=None,
        priority=100
    ):

        self.name = name

        self.category = category

        self.description = description

        self.inputs = inputs

        self.outputs = outputs

        self.requires = requires or []

        self.priority = priority


    def info(self):

        return {

            "name": self.name,

            "category": self.category,

            "description": self.description,

            "inputs": self.inputs,

            "outputs": self.outputs,

            "requires": self.requires,

            "priority": self.priority

        }