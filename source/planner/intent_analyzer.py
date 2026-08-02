"""
RanZiz AI Intent Analyzer
Version 1.0
"""


class IntentAnalyzer:

    def analyze(self, text):

        text = text.lower().strip()

        if text.startswith("buat"):
            return "CREATE"

        if text.startswith("cari"):
            return "SEARCH"

        if text.startswith("jelaskan"):
            return "ASK"

        return "CHAT"