"""
RanZiz AI Runtime Snapshot
Version 1.0
"""


class RuntimeSnapshot:

    def __init__(self):

        self.data = {}


    def capture(
        self,
        state,
        plan=None,
        context=None
    ):

        self.data = {

            "state": state,

            "plan": (
                plan.all()
                if plan
                else []
            ),

            "context": (
                context.all()
                if context
                else {}
            )

        }

        return self.data


    def get(self):

        return dict(
            self.data
        )


    def clear(self):

        self.data.clear()


    def __repr__(self):

        return (
            f"RuntimeSnapshot("
            f"{len(self.data)} fields)"
        )
