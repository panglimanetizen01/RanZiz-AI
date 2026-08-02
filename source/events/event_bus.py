"""
RanZiz AI Event Bus
Version 1.0
"""

from source.events.event_subscriber import EventSubscriber


class EventBus:


    def __init__(self):

        self.subscribers = {}


    def subscribe(

        self,

        event_name,

        subscriber

    ):

        if not isinstance(
            subscriber,
            EventSubscriber
        ):

            raise TypeError(
                "subscriber harus EventSubscriber"
            )


        self.subscribers.setdefault(
            event_name,
            []
        ).append(
            subscriber
        )


    def publish(

        self,

        event

    ):

        results = []

        listeners = self.subscribers.get(
            event.name,
            []
        )


        for subscriber in listeners:

            results.append(

                subscriber.notify(
                    event
                )

            )


        return results


    def listeners(

        self,

        event_name

    ):

        return self.subscribers.get(
            event_name,
            []
        )


    def clear(self):

        self.subscribers.clear()