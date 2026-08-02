"""
RanZiz AI Pipeline Manager
Version 1.1
"""


from source.response.pipeline.response_pipeline import ResponsePipeline
from source.response.pipeline.stages.observability_stage import ObservabilityStage
from source.response.pipeline.stages.response_builder_stage import ResponseBuilderStage


class PipelineManager:


    def __init__(self):

        self.pipeline = ResponsePipeline()


        self.pipeline.add_stage(
            ObservabilityStage()
        )


        self.pipeline.add_stage(
            ResponseBuilderStage()
        )



    def process(
        self,
        session_id,
        context,
        response
    ):


        data = {

            "session_id": session_id,

            "context": context,

            "response": response

        }


        result = self.pipeline.process(
            data
        )


        if isinstance(
            result,
            dict
        ):

            if "response" in result:

                return result["response"]


            if "output" in result:

                return result["output"]


        return result



    def stage_count(self):

        return self.pipeline.count()