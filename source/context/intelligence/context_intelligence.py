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
        # Emotion Detection
        # ==============================

        emotion = "neutral"


        if any(
            word in text
            for word in [
                "patah hati",
                "sedih",
                "kecewa",
                "galau",
                "rindu"
            ]
        ):

            emotion = "sad"


        elif any(
            word in text
            for word in [
                "senang",
                "bahagia",
                "semangat",
                "gembira"
            ]
        ):

            emotion = "happy"



        # ==============================
        # Topic Detail Detection
        # ==============================

        topic_detail = None


        if "patah hati" in text:

            topic_detail = "patah hati"



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

            "emotion": emotion,

            "topic_detail": topic_detail,

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