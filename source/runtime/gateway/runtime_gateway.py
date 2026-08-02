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

        return self.adapter.run(

            message,

            context

        )