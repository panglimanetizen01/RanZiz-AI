"""
RanZiz AI Brain Runtime
Version 2.0
"""

from source.events.trace_events import TraceEvents
from source.request.request_context import RequestContext


class BrainRuntime:


    def __init__(

        self,

        orchestrator

    ):

        self.orchestrator = orchestrator



    def process(

        self,

        message,

        context=None,

        plan=None

    ):

        if context is None:

            context = RequestContext()

            context.log(

                TraceEvents.REQUEST_CREATED,

                {

                    "module": "BrainRuntime"

                }

            )


        return self.orchestrator.execute(

            message,

            context,

            plan

        )
