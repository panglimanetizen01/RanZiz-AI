"""
RanZiz AI Decision Router
Version 1.0
"""


from source.decision.decision import Decision


class DecisionRouter:


    def route(

        self,

        message,

        context=None

    ):

        text = message.lower()



        intent = "chat"

        goal = "general"

        agent = None

        workflow = None

        capabilities = []

        confidence = 0.5

        reason = "Permintaan umum."



        if any(

            word in text

            for word in [

                "kode",

                "python",

                "program",

                "coding",

                "software"

            ]

        ):

            intent = "create"

            goal = "coding"

            agent = "Coding Agent"

            workflow = "Auto Workflow"

            capabilities = [

                "Code Engine"

            ]

            confidence = 1.0

            reason = "Permintaan terkait pemrograman."



        elif any(

            word in text

            for word in [

                "lagu",

                "musik",

                "dangdut",

                "rock",

                "hiphop"

            ]

        ):

            intent = "create"

            goal = "music"

            agent = "Music Agent"

            workflow = "Music Workflow"

            capabilities = [

                "Music Engine"

            ]

            confidence = 1.0

            reason = "Permintaan terkait musik."



        return Decision(

            intent,

            goal,

            agent,

            workflow,

            capabilities,

            confidence,

            reason

        )