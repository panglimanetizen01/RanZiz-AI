"""
RanZiz AI Agent Runtime Capability
Version 1.0
"""


class AgentRuntimeCapability:


    def __init__(

        self,

        agent_manager=None

    ):

        self.agent_manager = agent_manager


    def bind(

        self,

        agent_manager

    ):

        self.agent_manager = agent_manager

        return self


    def execute(

        self,

        message,

        context=None

    ):

        if self.agent_manager is None:

            return None


        if hasattr(

            self.agent_manager,

            "execute"

        ):

            return self.agent_manager.execute(

                message,

                context

            )


        return None