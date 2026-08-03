"""
RanZiz AI Intent Analyzer
Version 2.0
"""


class IntentAnalyzer:

    def analyze(self, text):

        text = text.lower().strip()

        mapping = [

            (
                "CREATE",
                [
                    "buat",
                    "buatkan",
                    "generate",
                    "ciptakan",
                    "tulis"
                ]
            ),

            (
                "EDIT",
                [
                    "edit",
                    "ubah",
                    "perbaiki",
                    "revisi",
                    "rapikan"
                ]
            ),

            (
                "SEARCH",
                [
                    "cari",
                    "temukan",
                    "search",
                    "lookup"
                ]
            ),

            (
                "ANALYZE",
                [
                    "analisis",
                    "analisa",
                    "review",
                    "audit",
                    "cek"
                ]
            ),

            (
                "TRANSLATE",
                [
                    "terjemahkan",
                    "translate"
                ]
            ),

            (
                "SUMMARIZE",
                [
                    "ringkas",
                    "rangkuman",
                    "summary"
                ]
            ),

            (
                "EXPLAIN",
                [
                    "jelaskan",
                    "mengapa",
                    "kenapa",
                    "bagaimana"
                ]
            )

        ]

        for intent, keywords in mapping:

            if any(text.startswith(word) for word in keywords):
                return intent

        return "CHAT"
