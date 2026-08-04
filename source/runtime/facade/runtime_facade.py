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

        self.inspector = None


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


    def _get_inspector(
        self
    ):

        runtime = None

        if hasattr(
            self.kernel,
            "get_runtime"
        ):
            runtime = self.kernel.get_runtime()

        if (
            runtime is not None
            and hasattr(runtime, "get_runtime")
        ):
            runtime = runtime.get_runtime()

        if runtime is None:

            return None

        if self.inspector is None:

            self.inspector = RuntimeInspector(
                runtime
            )

        return self.inspector


    def inspect(
        self
    ):

        inspector = self._get_inspector()

        if inspector is None:

            return {}

        return inspector.status()


    def status(
        self
    ):

        inspector = self._get_inspector()

        if inspector is None:

            return {
                "status": "NO_RUNTIME"
            }

        return {

            "runtime": inspector.state(),

            "snapshot": inspector.snapshot()

        }


    def __repr__(self):

        return (
            f"RuntimeFacade("
            f"{self.kernel})"
        )
