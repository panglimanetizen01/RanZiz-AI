"""
RanZiz AI Router Handler
Version 1.1
"""


class RouterHandler:

    def __init__(
        self,
        router
    ):
        self.router = router


    def handle(
        self,
        message,
        session,
        context,
        response_builder
    ):

        result = self.router.execute(
            message,
            context
        )

        if result is None:
            return None


        return response_builder(
            session,
            context,
            result
        )
