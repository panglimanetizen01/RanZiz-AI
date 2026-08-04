"""
RanZiz AI Runtime Facade
Version 2.0
"""

from source.runtime.inspector.runtime_inspector import RuntimeInspector


class RuntimeFacade:


    def __init__(
        self,
        kernel
    ):

        self.kernel = kernel

        runtime = getattr(
            kernel,
            "runtime",
            None
        )

        self.inspector = None

        if runtime:

            self.inspector = RuntimeInspector(
                runtime
            )


    def start(
        self,
        container
    ):

        return self.kernel.start(
            container
        )


    def chat(
        self,
        message,
        context=None
    ):

        return self.kernel.process(
            message,
            context
        )


    def stop(
        self
    ):

        return self.kernel.stop()


    def inspect(
        self
    ):

        if self.inspector is None:

            return {}

        return self.inspector.status()


    def status(
        self
    ):

        if self.inspector is None:

            return {
                "status": "NO_RUNTIME"
            }

        return {

            "runtime": self.inspector.state(),

            "snapshot": self.inspector.snapshot()

        }


    def __repr__(self):

        return (
            f"RuntimeFacade("
            f"{self.kernel})"
        )
