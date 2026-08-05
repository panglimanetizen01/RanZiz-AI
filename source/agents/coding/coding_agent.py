"""
RanZiz AI Coding Agent
Version 2.0
"""


class CodingAgent:


    def __init__(self):

        self.name = "coding"


    def can_handle(
        self,
        message
    ):

        text = message.lower()

        keywords = [
            "kode",
            "coding",
            "program",
            "python",
            "website",
            "aplikasi",
            "software"
        ]

        return any(
            word in text
            for word in keywords
        )


    def create_task(
        self,
        message,
        context=None
    ):

        return {
            "capability": "Code Engine",
            "message": message,
            "context": context or {}
        }


    def info(self):

        return {
            "name": self.name,
            "display_name": "Coding Agent",
            "category": "Coding",
            "description": "Agent khusus pemrograman dan pengembangan software"
        }
