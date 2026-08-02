"""
RanZiz AI Runtime Service
Version 1.2
"""


class RuntimeService:


    def __init__(

        self,

        manager

    ):

        self.manager = manager



    def execute(

        self,

        message,

        context=None

    ):

        return self.manager.execute(

            message,

            context

        )