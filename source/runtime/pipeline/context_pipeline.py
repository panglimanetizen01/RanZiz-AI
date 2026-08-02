"""
RanZiz AI Context Pipeline
Version 1.0
"""


class ContextPipeline:


    def __init__(

        self,

        context_gateway

    ):

        self.gateway = context_gateway


    def execute(

        self,

        request_context,

        message

    ):

        active_context = self.gateway.analyze(

            message

        )

        request_context.log(

            "REQUEST_CONTEXT",

            {

                "context": active_context

            }

        )

        return active_context