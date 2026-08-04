"""
RanZiz AI Runtime Event Bus
Version 1.0
"""

from source.runtime.events.runtime_event import RuntimeEvent


class RuntimeEventBus:

    def __init__(self):

        self.events = []

    def emit(
        self,
        event,
        capability=None,
        payload=None
    ):

        runtime_event = RuntimeEvent(
            event,
            capability,
            payload
        )

        self.events.append(
            runtime_event
        )

        return runtime_event

    def all(self):

        return [
            event.to_dict()
            for event in self.events
        ]

    def clear(self):

        self.events.clear()

    def count(self):

        return len(
            self.events
        )

    def last(self):

        if not self.events:
            return None

        return self.events[-1]

    def __len__(self):

        return len(
            self.events
        )

    def __iter__(self):

        return iter(
            self.events
        )

    def __repr__(self):

        return (
            f"RuntimeEventBus("
            f"{len(self)} events)"
        )
