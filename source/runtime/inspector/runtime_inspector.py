"""
RanZiz AI Runtime Inspector
Version 1.0
"""


class RuntimeInspector:

    def __init__(
        self,
        runtime
    ):

        self.runtime = runtime


    def state(self):

        return self.runtime.state.current


    def events(self):

        return self.runtime.events.all()


    def last_event(self):

        event = self.runtime.events.last()

        if event is None:
            return None

        return event.to_dict()


    def trace(self):

        return self.runtime.trace.all()


    def snapshot(self):

        return self.runtime.snapshot.get()


    def status(self):

        return {

            "state": self.state(),

            "events": self.events(),

            "trace": self.trace(),

            "snapshot": self.snapshot()

        }


    def __repr__(self):

        return (
            f"RuntimeInspector("
            f"{self.state()})"
        )
