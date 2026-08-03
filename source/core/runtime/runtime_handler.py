"""
RanZiz AI Runtime Handler
Version 2.0
"""


class RuntimeHandler:

    def __init__(self, runtime):
        self.runtime = runtime

    def handle(
        self,
        message,
        decision,
        result=None
    ):
        return self.execute(
            decision,
            message,
            result
        )

    def execute(
        self,
        decision,
        message,
        result=None
    ):
        if result is not None:
            return result

        context = None

        if decision is not None:
            context = {
                "provider": getattr(
                    decision,
                    "provider",
                    None
                )
            }

        return self.runtime.process(
            message,
            context
        )
