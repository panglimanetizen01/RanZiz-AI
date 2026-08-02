"""
RanZiz AI Runtime Core Bridge
Version 1.0
"""


class RuntimeCoreBridge:


    def __init__(

        self,

        gateway

    ):

        self.gateway = gateway



    def start(

        self,

        container

    ):

        return self.gateway.start(

            container

        )



    def process(

        self,

        message,

        context=None

    ):

        return self.gateway.process(

            message,

            context

        )



    def stop(

        self

    ):

        return self.gateway.stop()