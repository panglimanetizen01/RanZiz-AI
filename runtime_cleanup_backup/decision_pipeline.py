"""
RanZiz AI Decision Pipeline
Version 1.0
"""


class DecisionPipeline:


    def __init__(

        self,

        intent_analyzer,

        goal_analyzer,

        decision_engine

    ):

        self.intent = intent_analyzer

        self.goal = goal_analyzer

        self.engine = decision_engine



    def execute(

        self,

        message,

        context

    ):

        intent = self.intent.analyze(

            message

        )


        goal = self.goal.analyze(

            message

        )


        decision = self.engine.decide(

            intent,

            goal,

            context

        )


        return {

            "intent": intent,

            "goal": goal,

            "decision": decision

        }