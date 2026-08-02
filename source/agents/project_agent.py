"""
RanZiz AI Project Agent
Version 1.0
"""

from pathlib import Path

from source.agents.base_agent import BaseAgent


class ProjectAgent(BaseAgent):

    @property
    def name(self):

        return "project"

    def can_handle(self, message):

        text = message.lower()

        keywords = (
            "project",
            "proyek",
            "struktur project",
            "struktur proyek",
            "status project",
            "status proyek",
            "roadmap",
            "module",
            "modul"
        )

        return any(keyword in text for keyword in keywords)

    def execute(self, message):

        root = Path(".")

        folders = []

        for item in sorted(root.iterdir()):

            if item.is_dir() and not item.name.startswith("."):

                folders.append(item.name)

        result = (
            "📁 RanZiz Project Agent\n\n"
            "Folder utama:\n"
        )

        for folder in folders:

            result += f"- {folder}\n"

        return result