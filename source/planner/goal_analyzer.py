"""
RanZiz AI Goal Analyzer
Version 2.1
"""


class GoalAnalyzer:

    def analyze(self, text):

        text = text.lower()

        if any(
            word in text
            for word in [
                "lagu",
                "musik",
                "dangdut",
                "pop",
                "rock",
                "lirik"
            ]
        ):
            return "MUSIC"

        if any(
            word in text
            for word in [
                "video",
                "film",
                "animasi"
            ]
        ):
            return "VIDEO"

        if any(
            word in text
            for word in [
                "gambar",
                "foto",
                "logo",
                "ikon",
                "icon",
                "poster",
                "banner",
                "desain",
                "design",
                "image"
            ]
        ):
            return "IMAGE"

        if any(
            word in text
            for word in [
                "website",
                "web",
                "html",
                "css",
                "javascript",
                "js"
            ]
        ):
            return "WEBSITE"

        if any(
            word in text
            for word in [
                "aplikasi",
                "program",
                "python",
                "java",
                "kotlin",
                "coding",
                "kode"
            ]
        ):
            return "APPLICATION"

        if any(
            word in text
            for word in [
                "cari",
                "riset",
                "penelitian",
                "sejarah",
                "informasi",
                "analisis",
                "research"
            ]
        ):
            return "RESEARCH"


        if any(
            word in text
            for word in [
                "iklan",
                "promosi",
                "produk",
                "jualan",
                "marketing",
                "advertisement",
                "copywriting"
            ]
        ):
            return "MARKETING"

        return "GENERAL"
