"""
RanZiz AI Context Intelligence
Version 1.0
"""


class ContextIntelligence:


    def __init__(self):

        self.context = {}



    def analyze(

        self,

        message

    ):

        text = message.lower()


        # ==============================
        # Topic Detection
        # ==============================

        topic = "general"


        if any(
            word in text
            for word in [
                "lagu",
                "musik",
                "suno",
                "mp3",
                "nyanyi"
            ]
        ):

            topic = "music"


        elif any(
            word in text
            for word in [
                "kode",
                "python",
                "program",
                "aplikasi"
            ]
        ):

            topic = "coding"


        elif any(
            word in text
            for word in [
                "web",
                "website",
                "html"
            ]
        ):

            topic = "web"



        # ==============================
        # Intent Detection
        # ==============================

        intent = "chat"


        if any(
            word in text
            for word in [
                "buat",
                "bikin",
                "buatkan",
                "generate"
            ]
        ):

            intent = "create"


        elif any(
            word in text
            for word in [
                "jelaskan",
                "apa",
                "kenapa"
            ]
        ):

            intent = "question"



        self.context = {

            "topic": topic,

            "intent": intent,

            "last_message": message

        }


        return self.context



    def get(

        self,

        key,

        default=None

    ):

        return self.context.get(

            key,

            default

        )



    def all(self):

        return dict(

            self.context

        )



    def clear(self):

        self.context.clear()



    def __repr__(self):

        return "ContextIntelligence()"