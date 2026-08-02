"""
RanZiz AI Decision Engine
Version 1.2
"""


from source.decision.decision import Decision


class DecisionEngine:


    def decide(
        self,
        intent,
        goal,
        context=None
    ):


        decision = Decision(

            intent=intent,

            goal=goal,

            workflow="Auto Workflow",

            confidence=1.0

        )


        if goal == "coding":

            decision.agent = "Coding Agent"

            decision.capabilities = [
                "Code Engine"
            ]

            decision.provider = "deepseek"

            decision.reason = (
                "Permintaan terkait pemrograman."
            )



        elif goal == "music":

            decision.agent = "Music Agent"

            decision.capabilities = [

                "Lyric Engine",

                "Composer",

                "Audio Engine"

            ]

            decision.provider = "gemini"

            decision.reason = (
                "Permintaan terkait musik."
            )



        elif goal == "research":

            decision.agent = "Research Agent"

            decision.provider = "claude"

            decision.reason = (
                "Permintaan terkait riset."
            )



        else:

            decision.agent = "Chat Agent"

            decision.provider = "local"

            decision.reason = (
                "Percakapan umum."
            )



        return decision