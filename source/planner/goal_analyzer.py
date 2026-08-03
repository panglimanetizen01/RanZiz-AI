"""
RanZiz AI Goal Analyzer
Version 2.2
"""


class GoalAnalyzer:

    def analyze(self, text):

        text = text.lower()

        groups = [

            (
                "MUSIC",
                [
                    "lagu",
                    "musik",
                    "dangdut",
                    "pop",
                    "rock",
                    "lirik"
                ]
            ),

            (
                "VIDEO",
                [
                    "video",
                    "film",
                    "animasi"
                ]
            ),

            (
                "IMAGE",
                [
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
            ),

            (
                "WEBSITE",
                [
                    "website",
                    "web",
                    "html",
                    "css",
                    "javascript",
                    "js"
                ]
            ),

            (
                "APPLICATION",
                [
                    "aplikasi",
                    "program",
                    "python",
                    "java",
                    "kotlin",
                    "coding",
                    "kode"
                ]
            ),

            (
                "DOCUMENT",
                [
                    "dokumen",
                    "document",
                    "pdf",
                    "docx",
                    "word",
                    "laporan",
                    "proposal",
                    "presentasi",
                    "ppt",
                    "excel",
                    "xlsx"
                ]
            ),

            (
                "VISION",
                [
                    "analisis gambar",
                    "deteksi gambar",
                    "vision",
                    "ocr",
                    "scan gambar",
                    "baca gambar"
                ]
            ),

            (
                "VOICE",
                [
                    "suara",
                    "voice",
                    "tts",
                    "text to speech",
                    "pidato",
                    "narasi"
                ]
            ),

            (
                "RESEARCH",
                [
                    "cari",
                    "riset",
                    "penelitian",
                    "sejarah",
                    "informasi",
                    "analisis",
                    "research"
                ]
            ),

            (
                "MARKETING",
                [
                    "iklan",
                    "promosi",
                    "produk",
                    "jualan",
                    "marketing",
                    "advertisement",
                    "copywriting"
                ]
            )

        ]

        for goal, keywords in groups:

            if any(word in text for word in keywords):
                return goal

        return "GENERAL"
