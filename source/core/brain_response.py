"""
RanZiz AI Brain Response
Version 1.0
"""

from source.response.pipeline.pipeline_manager import PipelineManager


class BrainResponse:


    def __init__(self):

        self.pipeline = PipelineManager()


    def build(

        self,

        session,

        context,

        response

    ):

        return self.pipeline.process(

            session.id,

            context,

            response

        )


    def reply(

        self,

        session,

        context,

        response

    ):

        session.add_message(

            "assistant",

            str(response)

        )

        return self.build(

            session,

            context,

            response

        )