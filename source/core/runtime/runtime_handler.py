"""
RanZiz AI Runtime Handler
Version 1.1
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

        provider = getattr(
            decision,
            "provider",
            None
        )

        if provider:
            return self.runtime.ask_with_provider(
                provider,
                message
            )

        return self.runtime.ask(
            message
        )