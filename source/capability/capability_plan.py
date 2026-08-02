"""
RanZiz AI Capability Plan
Version 1.0
"""


class CapabilityPlan:


    def __init__(self):

        self.items = []


    def add(
        self,
        name,
        executor
    ):

        self.items.append({

            "name": name,

            "executor": executor

        })


    def all(self):

        return list(self.items)


    def names(self):

        return [

            item["name"]

            for item in self.items

        ]


    def __len__(self):

        return len(self.items)


    def __iter__(self):

        return iter(self.items)