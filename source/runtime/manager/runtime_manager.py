"""
RanZiz AI Runtime Manager
Version 1.2
"""


class RuntimeManager:


    def __init__(

        self

    ):

        self.container = None


    def register(

        self,

        container

    ):

        self.container = container


    def get_container(

        self

    ):

        return self.container


    def ready(

        self

    ):

        return self.container is not None


    def clear(

        self

    ):

        self.container = None


    def execute(

        self,

        message,

        context=None

    ):

        if self.container is None:

            return None


        runtime = self.container.get_brain_runtime()


        if runtime is not None and hasattr(

            runtime,

            "process"

        ):

            return runtime.process(

                message,

                context

            )


        adapter = self.container.get_runtime_adapter()


        if adapter is not None and hasattr(

            adapter,

            "process"

        ):

            return adapter.process(

                message,

                context

            )


        return {
            "status": "ok",
            "message": message,
            "context": context
        }