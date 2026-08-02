"""
RanZiz AI Event Subscriber
Version 1.0
"""


class EventSubscriber:


    def __init__(

        self,

        name,

        callback

    ):

        self.name = name

        self.callback = callback


    def notify(

        self,

        event

    ):

        return self.callback(
            event
        )


    def __repr__(self):

        return (
            f"EventSubscriber({self.name})"
        )