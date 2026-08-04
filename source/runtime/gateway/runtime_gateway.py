"""
RanZiz AI Runtime Gateway
Version 1.0
"""


class RuntimeGateway:


    def __init__(

        self,

        adapter

    ):

        self.adapter = adapter





    def get_runtime(
        self
    ):

        return self.adapter.get_runtime()


    def start(

        self,

        container

    ):

        return self.adapter.start(

            container

        )



    def stop(

        self

    ):

        return self.adapter.stop()



    def process(

        self,

        message,

        context=None

    ):

        if hasattr(
            self.adapter,
            "process"
        ):

            return self.adapter.process(
                message,
                context
            )

        return self.adapter.run(
            message,
            context
        )