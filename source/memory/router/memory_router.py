"""
RanZiz AI Memory Router
Version 2.0
"""

from source.memory.integration.memory_recall_adapter import MemoryRecallAdapter
from source.memory.intent.memory_intent import MemoryIntent


class MemoryRouter:


    def __init__(self):

        self.intent = MemoryIntent()

        self.recall = MemoryRecallAdapter()



    def route(

        self,

        message

    ):

        intent = self.intent.detect(

            message

        )


        if intent == "identity":

            return self.recall.identity()



        if intent == "recall":

            return self.recall.profile()



        if intent == "profile":

            return self.recall.profile()



        return None



    def __repr__(self):

        return "MemoryRouter()"