"""
RanZiz AI Agent Manager
Version 2.0
"""

from source.agents.registry.agent_registry import AgentRegistry


class AgentManager:


    def __init__(
        self,
        registry=None
    ):

        self.registry = registry or AgentRegistry()

        self.agents = {}

        self.load()



    def load(self):

        """
        Agent loader placeholder.
        Agent capability integration menggunakan registry.
        """

        return self.agents



    def register(
        self,
        name,
        agent
    ):

        self.agents[name] = agent

        self.registry.register(
            name,
            agent
        )



    def get(
        self,
        name
    ):

        return self.agents.get(
            name
        )



    def execute(
        self,
        message,
        context=None
    ):

        for name, agent in self.agents.items():

            try:

                if not agent.can_handle(
                    message
                ):
                    continue


                try:

                    return agent.execute(
                        message,
                        context
                    )

                except TypeError:

                    return agent.execute(
                        message
                    )

            except AttributeError:

                continue

        return None


    def list(self):

        return list(
            self.agents.keys()
        )



    def count(self):

        return len(
            self.agents
        )



    def __repr__(self):

        return (
            f"AgentManager("
            f"{self.count()} agents)"
        )
