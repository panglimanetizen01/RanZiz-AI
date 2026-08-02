"""
RanZiz AI API Service
Version 1.0
"""


from source.core.brain import Brain


class APIService:


    def __init__(self):

        self.brain = Brain()



    def chat(

        self,

        message,

        session_id=None

    ):

        return self.brain.process(

            message,

            session_id

        )



    def health(self):

        return {

            "status": "OK",

            "service": "RanZiz AI",

            "version": self.brain.version

        }



    def __repr__(self):

        return "APIService()"