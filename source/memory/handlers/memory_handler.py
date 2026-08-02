"""
RanZiz AI Memory Handler
Version 1.0
"""

from source.events.trace_events import TraceEvents


class MemoryHandler:

    def __init__(
        self,
        memory,
        episode
    ):
        self.memory = memory
        self.episode = episode


    def learn(
        self,
        message,
        decision,
        context
    ):
        self.memory.learn_decision(
            decision
        )

        context.log(
            TraceEvents.DECISION_CREATED,
            decision.to_dict()
        )

        context.set(
            "decision",
            decision
        )

        self.episode.record(
            self.memory,
            message,
            {
                "decision": decision.to_dict()
            }
        )

        return self.memory.learn(
            message
        )


    def fallback(
        self,
        message,
        session,
        context,
        response_builder
    ):
        decision = self.memory.decide(
            message
        )

        if not isinstance(
            decision,
            dict
        ):
            decision = {}

        if decision.get(
            "action"
        ) == "memory":

            result = self.memory.about_user()

            session.add_message(
                "assistant",
                result
            )

            return response_builder(
                session,
                context,
                result
            )


        if decision.get(
            "action"
        ) == "episode":

            episode = self.memory.recall_episode(
                message
            )

            if episode is not None:

                session.add_message(
                    "assistant",
                    episode
                )

                return response_builder(
                    session,
                    context,
                    episode
                )

        return None


    def retrieve(
        self,
        message,
        decision,
        session,
        context,
        response_builder
    ):

        allow_memory = (
            decision.intent != "create"
            and decision.goal == "chat"
        )

        if not allow_memory:
            return None


        retrieved = self.memory.retrieve(
            message
        )

        if retrieved is None:
            return None


        if isinstance(
            retrieved,
            dict
        ):
            value = retrieved.get(
                "value",
                str(retrieved)
            )

        else:
            value = str(
                retrieved
            )


        session.add_message(
            "assistant",
            value
        )


        return response_builder(
            session,
            context,
            value
        )