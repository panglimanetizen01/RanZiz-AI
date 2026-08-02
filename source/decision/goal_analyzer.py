"""
RanZiz AI Goal Analyzer
Version 1.1
"""


class GoalAnalyzer:


    def analyze(

        self,

        message

    ):

        text = message.lower()


        coding = (

            "python",

            "kode",

            "coding",

            "program",

            ".py",

            "software",

            "website",

            "web",

            "html",

            "css",

            "javascript",

            "react",

            "vue",

            "laravel",

            "django",

            "flask",

            "api",

            "backend",

            "frontend",

            "aplikasi",

            "android"

        )


        music = (

            "lagu",

            "musik",

            "dangdut",

            "lirik",

            "melodi",

            "suno",

            "audio"

        )


        research = (

            "riset",

            "research",

            "penelitian",

            "analisa"

        )


        project = (

            "project",

            "proyek",

            "ranziz"

        )


        if any(

            word in text

            for word in coding

        ):

            return "coding"



        if any(

            word in text

            for word in music

        ):

            return "music"



        if any(

            word in text

            for word in research

        ):

            return "research"



        if any(

            word in text

            for word in project

        ):

            return "project"



        return "chat"