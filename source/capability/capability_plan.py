"""
RanZiz AI Capability Plan
Version 2.0
"""


class CapabilityPlan:

    def __init__(self):

        self.items = []

    def add(
        self,
        name,
        executor,
        dependencies=None
    ):

        self.items.append({

            "name": name,

            "executor": executor,

            "dependencies": list(
                dependencies or []
            ),

            "status": "PENDING",

            "result": None

        })

    def all(self):

        return list(
            self.items
        )

    def names(self):

        return [

            item["name"]

            for item in self.items

        ]

    def get(
        self,
        name
    ):

        for item in self.items:

            if item["name"] == name:

                return item

        return None

    def set_status(
        self,
        name,
        status
    ):

        item = self.get(name)

        if item:

            item["status"] = status

    def set_result(
        self,
        name,
        result
    ):

        item = self.get(name)

        if item:

            item["result"] = result

    def pending(self):

        return [

            item

            for item in self.items

            if item["status"] == "PENDING"

        ]

    def completed(self):

        return [

            item

            for item in self.items

            if item["status"] == "SUCCESS"

        ]

    def failed(self):

        return [

            item

            for item in self.items

            if item["status"] == "FAILED"

        ]

    def __len__(self):

        return len(
            self.items
        )

    def __iter__(self):

        return iter(
            self.items
        )

    def __repr__(self):

        return (
            f"CapabilityPlan("
            f"{len(self)} items)"
        )
