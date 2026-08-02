"""
RanZiz AI Capability Catalog
Version 1.0
"""


class CapabilityCatalog:


    def __init__(self):

        self.capabilities = {}


    def register(
        self,
        capability
    ):

        info = capability.metadata()

        data = info.info()

        self.capabilities[
            data["name"]
        ] = data


    def add_many(
        self,
        executors
    ):

        for executor in executors:

            self.register(
                executor
            )


    def get(
        self,
        name
    ):

        return self.capabilities.get(
            name
        )


    def list(
        self
    ):

        return list(
            self.capabilities.values()
        )


    def search(
        self,
        keyword
    ):

        keyword = keyword.lower()

        results = []

        for item in self.capabilities.values():

            if keyword in str(item).lower():

                results.append(item)


        return results