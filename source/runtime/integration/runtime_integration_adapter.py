"""
RanZiz AI Runtime Integration Adapter
Version 1.0
"""


class RuntimeIntegrationAdapter:


    def __init__(

        self,

        coordinator

    ):

        self.coordinator = coordinator





    def get_runtime(
        self
    ):

        return self.coordinator.get_runtime()


    def process(

        self,

        message,

        context=None

    ):

        return self.coordinator.execute(
            message,
            context
        )


    def run(

        self,

        message,

        context=None

    ):

        return self.process(
            message,
            context
        )



    def start(

        self,

        container

    ):

        return self.coordinator.start(

            container

        )



    def stop(

        self

    ):

        return self.coordinator.stop()