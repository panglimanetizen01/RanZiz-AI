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


        self.episode.record(

            self.memory,

            message,

            {
                "decision": decision.to_dict()
                if hasattr(decision, "to_dict")
                else decision
            }

        )


        learned = self.memory.learn(

            message

        )


        return learned