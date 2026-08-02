"""
RanZiz AI HTTP Server
Version 1.0
"""


from source.api.api_controller import APIController
from source.api.response.response_builder import ResponseBuilder


class HTTPServer:


    def __init__(self):

        self.controller = APIController()

        self.response = ResponseBuilder()



    def chat(

        self,

        payload

    ):

        try:

            result = self.controller.chat(
                payload
            )

            return self.response.success(
                result
            )

        except Exception as error:  # noqa: BLE001
            # Boundary handler: never let unhandled controller errors crash the HTTP API.
            return self.response.error(
                str(error)
            )



    def health(self):

        try:

            return self.response.success(

                self.controller.health()

            )

        except Exception as error:  # noqa: BLE001
            # Boundary handler: never let unhandled controller errors crash the HTTP API.
            return self.response.error(

                str(error)

            )



    def __repr__(self):

        return "HTTPServer()"