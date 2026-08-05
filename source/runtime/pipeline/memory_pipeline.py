"""
RanZiz AI Memory Pipeline
Version 1.0
"""


class MemoryPipeline:


    def __init__(

        self,

        memory_gateway,

        episode_recorder

    ):

        self.memory = memory_gateway

        self.episode = episode_recorder



    def execute(

        self,

        message,

        decision

    ):

        self.memory.learn_decision(

            decision

        )


        metadata = {
            "decision": (
                decision.to_dict()
                if hasattr(decision, "to_dict")
                else decision
            )
        }

        import json

        try:
            json.dumps(metadata)
        except TypeError:
            metadata = {
                "decision": str(decision)
            }

        self.episode.record(
            self.memory,
            message,
            metadata
        )


        learned = self.memory.learn(

            message

        )


        return learned