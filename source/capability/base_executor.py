"""
RanZiz AI Base Capability Executor
Version 1.0
"""


class BaseCapabilityExecutor:


    def execute(self, payload):

        raise NotImplementedError(
            "Executor harus memiliki method execute()"
        )


    def metadata(self):

        raise NotImplementedError(
            "Executor harus memiliki method metadata()"
        )