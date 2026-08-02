"""
RanZiz AI Decision Result
Version 1.1
"""


class Decision:


    def __init__(

        self,

        intent=None,

        goal=None,

        agent=None,

        workflow=None,

        capabilities=None,

        confidence=0.0,

        reason=None,

        provider=None

    ):


        self.intent = intent

        self.goal = goal

        self.agent = agent

        self.workflow = workflow

        self.capabilities = capabilities or []

        self.confidence = confidence

        self.reason = reason

        self.provider = provider



    def to_dict(self):

        return {

            "intent": self.intent,

            "goal": self.goal,

            "agent": self.agent,

            "workflow": self.workflow,

            "capabilities": self.capabilities,

            "confidence": self.confidence,

            "reason": self.reason,

            "provider": self.provider

        }



    def __repr__(self):

        return str(
            self.to_dict()
        )