"""
RanZiz AI Context Gateway
Version 2.0
"""


from source.context.context_manager import ContextManager
from source.context.intelligence.context_intelligence import ContextIntelligence
from source.memory.context.context_builder import ContextBuilder


class ContextGateway:


    def __init__(self):

        self.manager = ContextManager()

        self.builder = ContextBuilder()

        self.intelligence = ContextIntelligence()



    def set(

        self,

        key,

        value

    ):

        return self.manager.set(

            key,

            value

        )



    def get(

        self,

        key,

        default=None

    ):

        return self.manager.get(

            key,

            default

        )



    def analyze(

        self,

        message

    ):

        result = self.intelligence.analyze(

            message

        )


        for key, value in result.items():

            self.manager.set(

                key,

                value

            )


        return result



    def build_memory_context(

        self,

        key

    ):

        return self.builder.build(

            key

        )



    def get_id(self):

        return self.manager.get(
            "request_id",
            None
        )



    def log(

        self,

        event,

        data=None

    ):

        self.manager.set(

            "last_event",

            {
                "event": str(event),
                "data": data
            }

        )

        return True



    def get_trace(self):

        return self.manager.get(
            "trace",
            []
        )



    def all(self):

        return self.manager.all()



    def clear(self):

        self.intelligence.clear()

        return self.manager.clear()



    def __repr__(self):

        return "ContextGateway(v2.0)"