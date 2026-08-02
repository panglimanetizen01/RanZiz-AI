"""
RanZiz AI API Controller
Version 1.0
"""

from source.api.api_service import APIService


class APIController:


    def __init__(self):

        self.service = APIService()


    def chat(

        self,

        payload

    ):

        if not isinstance(payload, dict):

            raise TypeError(
                "payload harus berupa dict"
            )


        message = payload.get(
            "message",
            ""
        )


        session_id = payload.get(
            "session_id"
        )


        return self.service.chat(

            message,

            session_id

        )


    def health(self):

        return self.service.health()


    def __repr__(self):

        return "APIController()"