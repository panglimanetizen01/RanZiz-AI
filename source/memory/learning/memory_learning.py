"""
RanZiz AI Memory Learning
Version 1.0
"""


class MemoryLearning:


    def analyze(

        self,

        message

    ):

        text = message.lower().strip()


        if ":" not in text:

            return None



        parts = message.split(

            ":",

            1

        )


        key = parts[0].strip()

        value = parts[1].strip()



        if not key or not value:

            return None



        return {

            "key": key,

            "value": value,

            "source": "conversation"

        }



    def should_learn(

        self,

        candidate

    ):


        if candidate is None:

            return False



        key = candidate.get(

            "key"

        )


        value = candidate.get(

            "value"

        )


        return not (not key or not value)



    def learn(

        self,

        message

    ):

        candidate = self.analyze(

            message

        )


        if self.should_learn(

            candidate

        ):

            return candidate



        return None



    def __repr__(self):

        return "MemoryLearning()"
