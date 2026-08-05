"""
RanZiz AI Agent Router
Version 2.4
"""

from source.events.trace_events import TraceEvents
from source.agents.agent_manager import AgentManager


class AgentRouter:

    def __init__(self, manager=None):

        self.manager = (
            manager
            if manager is not None
            else AgentManager()
        )


    def route(
        self,
        message,
        context=None
    ):

        text = message.lower()

        agent_key = None


        if any(
            word in text
            for word in [
                "kode",
                "program",
                "python",
                "website",
                "aplikasi",
                "software"
            ]
        ):
            agent_key = "coding"


        elif any(
            word in text
            for word in [
                "cari",
                "riset",
                "penelitian",
                "sejarah",
                "informasi"
            ]
        ):
            agent_key = "research"


        if agent_key is None:

            if context is not None:
                context.log(
                    TraceEvents.AGENT_SELECTED,
                    {
                        "agent": None,
                        "found": False
                    }
                )

            return None


        agent_instance = self.manager.get(
            agent_key
        )


        if context is not None:

            context.log(
                TraceEvents.AGENT_SELECTED,
                {
                    "agent": agent_key,
                    "found": agent_instance is not None
                }
            )


        return agent_instance
