"""
RanZiz AI Natural Learning Pipeline
Version 1.0
"""

from source.memory.extractor.memory_extractor import MemoryExtractor
from source.memory.manager.memory_manager import MemoryManager


class NaturalLearningPipeline:


    def __init__(self):

        self.extractor = MemoryExtractor()

        self.manager = MemoryManager()



    def process(

        self,

        message

    ):

        result = self.extractor.extract(

            message

        )


        if result is None:

            return {

                "learned": False,

                "message": "Tidak ada memory yang ditemukan."

            }


        saved = self.manager.save(

            result["key"],

            result["value"]

        )


        return {

            "learned": True,

            "key": result["key"],

            "value": result["value"],

            "memory": saved

        }



    def __repr__(self):

        return "NaturalLearningPipeline()"