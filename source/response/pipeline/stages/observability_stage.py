"""
RanZiz AI Observability Stage
Version 1.0
"""

from source.observability.observability_service import ObservabilityService


class ObservabilityStage:


    def __init__(self):

        self.service = (
            ObservabilityService()
        )


    def __call__(

        self,

        data

    ):

        data["observability"] = (

            self.service.process(

                data["context"]

            )

        )

        return data