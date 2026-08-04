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



    def get_capability_name(
        self
    ):

        try:

            info = self.metadata()

            if info is not None:

                return info.name

        except Exception:

            pass

        return self.__class__.__name__


    def success(
        self,
        data,
        metadata=None
    ):

        return {

            "status": "SUCCESS",

            "capability": self.get_capability_name(),

            "data": data,

            "metadata": metadata or {}

        }


    def failure(
        self,
        error
    ):

        return {

            "status": "FAILED",

            "capability": self.get_capability_name(),

            "error": str(error),

            "metadata": {}

        }

