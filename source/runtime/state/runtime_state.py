"""
RanZiz AI Runtime State
Version 1.0
"""


class RuntimeState:

    STATES = [
        "CREATED",
        "PLANNING",
        "RUNNING",
        "COMPLETED",
        "FAILED",
        "CANCELLED",
    ]


    def __init__(
        self,
        initial="CREATED"
    ):

        if initial not in self.STATES:
            raise ValueError(
                f"Invalid state: {initial}"
            )

        self.current = initial

        self.history = [
            initial
        ]


    def transition(
        self,
        state
    ):

        if state not in self.STATES:
            raise ValueError(
                f"Invalid state: {state}"
            )

        self.current = state

        self.history.append(
            state
        )

        return self.current


    def is_state(
        self,
        state
    ):

        return self.current == state


    def all(self):

        return list(
            self.history
        )


    def __repr__(self):

        return (
            f"RuntimeState("
            f"{self.current})"
        )
