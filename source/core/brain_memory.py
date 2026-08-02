"""
RanZiz AI Brain Memory
Version 1.0
"""

class BrainMemory:


    def __init__(

        self,

        memory,

        episode

    ):

        self.memory = memory

        self.episode = episode


    def process(

        self,

        message,

        ai_decision

    ):

        self.memory.learn_decision(

            ai_decision

        )

        self.episode.record(

            self.memory,

            message,

            {

                "decision": ai_decision.to_dict()

            }

        )

        learned = self.memory.learn(

            message

        )

        if learned is not None:

            return learned

        decision = self.memory.decide(

            message

        )

        if decision.get(

            "action"

        ) == "memory":

            return self.memory.about_user()

        if decision.get(

            "action"

        ) == "episode":

            episode = self.memory.recall_episode(

                message

            )

            if episode is not None:

                return episode

        retrieved = self.memory.retrieve(

            message

        )

        if retrieved is None:

            return None

        if isinstance(

            retrieved,

            dict

        ):

            return retrieved.get(

                "value",

                str(retrieved)

            )

        return str(

            retrieved

        )