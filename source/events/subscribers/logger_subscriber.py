"""
RanZiz AI Logger Subscriber
Version 1.0
"""

from source.events.event_subscriber import EventSubscriber
from source.logger.logger import Logger


class LoggerSubscriber(EventSubscriber):


    def __init__(self):

        self.logger = Logger()

        super().__init__(

            "Logger",

            self.handle

        )


    def handle(

        self,

        event

    ):

        self.logger.info(  # noqa: PLE1205
            "Event",
            event.name,
            event.payload,
        )

        return True
