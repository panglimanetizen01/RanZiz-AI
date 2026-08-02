"""
RanZiz AI Coding Agent
Version 1.0
"""

from pathlib import Path

from source.agents.base_agent import BaseAgent


class CodingAgent(BaseAgent):

    @property
    def name(self):

        return "coding"

    def can_handle(self, message):

        text = message.lower()

        keywords = (
            "python",
            "kode",
            "coding",
            "program",
            "bug",
            "error",
            "debug",
            "refactor",
            "class",
            "function",
            "source",
            ".py"
        )

        return any(keyword in text for keyword in keywords)

    def execute(self, message):

        total_files = 0

        python_files = 0

        for file in Path(".").rglob("*"):

            if file.is_file():

                total_files += 1

                if file.suffix == ".py":

                    python_files += 1

        return (
            "💻 RanZiz Coding Agent\n\n"
            f"Total File : {total_files}\n"
            f"File Python : {python_files}\n\n"
            "Coding Agent aktif dan siap membantu analisis kode."
        )