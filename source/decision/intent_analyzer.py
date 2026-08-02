"""
RanZiz AI Intent Analyzer
Version 1.0
"""


class IntentAnalyzer:


    def analyze(

        self,

        message

    ):

        text = message.lower()


        create = (

            "buat",

            "bikin",

            "generate",

            "tulis",

            "compose",

            "create"

        )


        ask = (

            "apa",

            "siapa",

            "mengapa",

            "kenapa",

            "kapan",

            "dimana",

            "bagaimana"

        )


        search = (

            "cari",

            "search",

            "temukan",

            "lookup"

        )


        remember = (

            "ingat",

            "remember",

            "simpan"

        )


        if any(

            word in text

            for word in create

        ):

            return "create"


        if any(

            word in text

            for word in ask

        ):

            return "question"


        if any(

            word in text

            for word in search

        ):

            return "search"


        if any(

            word in text

            for word in remember

        ):

            return "memory"


        return "chat"