"""
RanZiz AI Brain Request
Version 1.0
"""

from source.events.trace_events import TraceEvents
from source.request.request_context import RequestContext


class BrainRequest:

    def create(

        self,

        sessions,

        session_id,

        message

    ):

        context = RequestContext()

        context.log(

            TraceEvents.REQUEST_CREATED,

            {

                "module": "Brain"

            }

        )

        session = sessions.get_or_create(

            session_id

        )

        session.add_message(

            "user",

            message

        )

        return (

            session,

            context

        )