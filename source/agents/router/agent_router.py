"""
RanZiz AI Agent Router
Version 2.1
"""


from source.events.trace_events import TraceEvents


class AgentRouter:



    def __init__(

        self,

        manager=None

    ):

        self.manager = manager



    def route(

        self,

        message,

        context=None

    ):

        text = message.lower()


        agent = None


        if any(

            word in text

            for word in [

                "lagu",
                "musik",
                "lirik",
                "dangdut",
                "pop"
            ]

        ):

            agent = "Music Agent"



        elif any(

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

            agent = "Coding Agent"



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

            agent = "Research Agent"



        else:

            agent = "chat"



        if context is not None:

            context.log(

                TraceEvents.AGENT_SELECTED,

                {
                    "agent": agent
                }

            )


        return agent