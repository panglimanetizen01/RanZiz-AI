"""
RanZiz AI Agent Manager
Version 3.2
"""


from source.agents.agent_loader import AgentLoader
from source.agents.registry.agent_registry import AgentRegistry
from source.agents.router.agent_router import AgentRouter


class AgentManager:



    def __init__(self):

        self.loader = AgentLoader()

        self.registry = AgentRegistry()


        self.router = AgentRouter(
            self
        )


        self.load()



    def load(self):

        agents = self.loader.load()


        for name, agent in agents.items():

            self.registry.register(
                name,
                agent
            )



    def execute(

        self,

        message,

        context=None

    ):


        agent_name = self.router.route(

            message,

            context

        )


        agent = self.registry.get(
            agent_name
        )


        if agent:


            try:

                return agent.execute(
                    message,
                    context
                )


            except TypeError:

                return agent.execute(
                    message
                )


        return None



    def list(self):

        return self.registry.list()



    def get(self, name):

        return self.registry.get(
            name
        )