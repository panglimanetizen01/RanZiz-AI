"""
RanZiz AI Memory Learning Adapter
Version 1.0
"""

from source.memory.learning.learning_pipeline import LearningPipeline
from source.memory.manager.memory_manager import MemoryManager


class MemoryLearningAdapter:


    def __init__(self):

        self.pipeline = LearningPipeline()

        self.manager = MemoryManager()



    def process(

        self,

        message

    ):

        return self.pipeline.process(

            message,

            self.manager

        )



    def learn(

        self,

        message

    ):

        result = self.process(

            message

        )


        if result.get(

            "learned"

        ):

            return (
                f"Saya akan mengingat "
                f"{result['key']} = {result['value']}"
            )


        return None



    def __repr__(self):

        return "MemoryLearningAdapter()"