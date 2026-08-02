"""
RanZiz AI Memory Intent Detector
Version 1.0
"""


class MemoryIntent:


    def detect(

        self,

        message

    ):

        text = message.lower()


        if any(

            word in text

            for word in [

                "siapa nama saya",

                "nama saya siapa",

                "identitas saya"

            ]

        ):

            return "identity"



        if any(

            word in text

            for word in [

                "apa yang kamu ingat",

                "ingat tentang saya",

                "yang kamu tahu tentang saya"

            ]

        ):

            return "recall"



        if any(

            word in text

            for word in [

                "profil saya",

                "ceritakan tentang saya",

                "tentang saya"

            ]

        ):

            return "profile"



        return None



    def __repr__(self):

        return "MemoryIntent()"