"""
RanZiz AI Event Manager
Version 1.2
"""

from source.events.event_bus import EventBus
from source.events.subscribers.logger_subscriber import LoggerSubscriber


class EventManager:


    def __init__(self):

        self.bus = EventBus()

        self.register_default()


    def register_default(self):

        logger = LoggerSubscriber()

        events = [

            # Workflow
            "workflow.started",
            "workflow.finished",
            "workflow.failed",

            # Capability
            "capability.started",
            "capability.finished",
            "capability.failed",

            # Session
            "session.created",
            "session.updated",
            "session.closed"

        ]

        for event in events:

            self.bus.subscribe(
                event,
                logger
            )


    def publish(self, event):

        return self.bus.publish(event)


    def subscribe(

        self,

        event_name,

        subscriber

    ):

        self.bus.subscribe(
            event_name,
            subscriber
        )