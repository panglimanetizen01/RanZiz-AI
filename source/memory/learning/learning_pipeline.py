"""
RanZiz AI Memory Learning Pipeline
Version 1.0
"""

from source.memory.learning.memory_learning import MemoryLearning


class LearningPipeline:


    def __init__(self):

        self.learning = MemoryLearning()



    def process(

        self,

        message,

        memory_manager

    ):

        candidate = self.learning.learn(

            message

        )


        if candidate is None:

            return {

                "learned": False,

                "message": "Tidak ada memory baru."

            }



        result = memory_manager.save(

            candidate["key"],

            candidate["value"]

        )


        return {

            "learned": True,

            "key": candidate["key"],

            "value": candidate["value"],

            "memory": result

        }



    def __repr__(self):

        return "LearningPipeline()"