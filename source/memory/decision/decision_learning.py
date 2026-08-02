"""
RanZiz AI Decision Learning
Version 2.0
"""

from source.database.database_manager import DatabaseManager


class DecisionLearning:


    def __init__(self):

        self.database = DatabaseManager()



    def learn(

        self,

        decision

    ):

        if not decision:

            return None



        if hasattr(

            decision,

            "to_dict"

        ):

            data = decision.to_dict()



        elif isinstance(

            decision,

            dict

        ):

            data = decision



        else:

            return None



        intent = data.get(

            "goal",

            data.get(

                "intent",

                "unknown"

            )

        )


        agent = data.get(

            "agent",

            "unknown"

        )


        key = f"{intent}:{agent}"



        storage = self.database.load()


        patterns = storage.setdefault(

            "decision_patterns",

            {}

        )


        patterns[key] = patterns.get(

            key,

            0

        ) + 1



        self.database.save(

            storage

        )


        return {

            "pattern": key,

            "count": patterns[key]

        }



    def patterns(self):

        storage = self.database.load()


        return storage.get(

            "decision_patterns",

            {}

        )



    def best(self):

        patterns = self.patterns()


        if not patterns:

            return None



        return max(

            patterns,

            key=patterns.get

        )



    def clear(self):

        storage = self.database.load()


        storage["decision_patterns"] = {}


        self.database.save(

            storage

        )



    def __repr__(self):

        return "DecisionLearning(v2.0)"