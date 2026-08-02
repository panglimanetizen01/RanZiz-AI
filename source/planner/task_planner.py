"""
RanZiz AI Task Planner
Version 2.2
"""

from source.capability.selector.capability_selector import CapabilitySelector
from source.planner.goal_analyzer import GoalAnalyzer
from source.planner.intent_analyzer import IntentAnalyzer


class TaskPlanner:

    def __init__(self):

        self.intent = IntentAnalyzer()

        self.goal = GoalAnalyzer()

        self.selector = CapabilitySelector()

    def plan(

        self,

        text,

        context=None

    ):

        if context is None:

            context = {}

        topic = context.get(
            "topic",
            "general"
        )

        detected_intent = context.get(
            "intent"
        )

        if detected_intent is None:

            detected_intent = self.intent.analyze(
                text
            )

        goal = self.goal.analyze(
            text
        )

        capabilities = self.selector.select(
            goal
        )

        task_type = (
            f"{topic}."
            f"{detected_intent}"
        )

        return {

            "message": text,

            "intent": detected_intent,

            "goal": goal,

            "topic": topic,

            "task_type": task_type,

            "capabilities": capabilities,

            "context": dict(context)

        }