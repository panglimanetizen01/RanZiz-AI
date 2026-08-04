"""
RanZiz AI Chat API
Version 1.0
"""


class ChatAPI:

    def __init__(
        self,
        gateway
    ):

        self.gateway = gateway


    def chat(
        self,
        message,
        context=None
    ):

        if not isinstance(
            message,
            str
        ):

            return {
                "error": "message harus berupa text"
            }


        result = self.gateway.process(
            message,
            context or {}
        )


        return {
            "response": result
        }
