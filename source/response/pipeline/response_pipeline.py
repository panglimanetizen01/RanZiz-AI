"""
RanZiz AI Response Pipeline
Version 1.0
"""


class ResponsePipeline:


    def __init__(self):

        self.stages = []


    def add_stage(

        self,

        stage

    ):

        self.stages.append(
            stage
        )


    def process(

        self,

        data

    ):

        result = data

        for stage in self.stages:

            result = stage(
                result
            )

        return result


    def count(self):

        return len(
            self.stages
        )


    def clear(self):

        self.stages.clear()