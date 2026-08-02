"""
RanZiz AI Agent Registry
Version 1.0
"""


class AgentRegistry:


    def __init__(self):

        self.agents = {}


    def register(
        self,
        name,
        agent
    ):

        self.agents[name] = agent


    def get(
        self,
        name
    ):

        return self.agents.get(name)


    def all(self):

        return dict(
            self.agents
        )


    def list(self):

        return sorted(
            self.agents.keys()
        )