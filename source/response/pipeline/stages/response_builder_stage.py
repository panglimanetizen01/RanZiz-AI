"""
RanZiz AI Response Builder Stage
Version 1.0
"""

from source.response.response_builder import ResponseBuilder


class ResponseBuilderStage:


    def __init__(self):

        self.builder = ResponseBuilder()


    def __call__(

        self,

        data

    ):

        return self.builder.build(

            session_id=data["session_id"],

            context=data["context"],

            response=data["response"],

            observability=data.get(
                "observability"
            )

        )