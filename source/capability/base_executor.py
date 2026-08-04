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

    def success(
        self,
        data,
        metadata=None
    ):

        return {

            "status": "SUCCESS",

            "capability": self.__class__.__name__,

            "data": data,

            "metadata": metadata or {}

        }


    def failure(
        self,
        error
    ):

        return {

            "status": "FAILED",

            "capability": self.__class__.__name__,

            "error": str(error),

            "metadata": {}

        }

