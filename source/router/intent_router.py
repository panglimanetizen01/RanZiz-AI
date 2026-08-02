"""
RanZiz AI Intent Router
Version 2.0
"""


class IntentRouter:

    def __init__(self):

        self.base_priority = {
            "research": 100,
            "coding": 80,
            "music": 80,
            "project": 70,
            "chat": 10,
        }

        self.keywords = {
            "research": [
                "apa",
                "siapa",
                "mengapa",
                "kenapa",
                "bagaimana",
                "kapan",
                "dimana",
                "di mana",
                "jelaskan",
                "explain",
            ],
            "coding": [
                "python",
                "kode",
                "coding",
                "debug",
                "bug",
                "error",
                "class",
                "function",
            ],
            "music": [
                "lagu",
                "musik",
                "dangdut",
                "pop",
                "rock",
                "rap",
            ],
            "project": [
                "project",
                "proyek",
                "roadmap",
                "struktur",
                "modul",
            ],
            "chat": [
                "halo",
                "hai",
                "hi",
                "apa kabar",
            ],
        }

    def select(self, agents, message):

        text = message.lower()

        best_agent = None
        best_score = -1

        for agent in agents:

            if not agent.can_handle(text):
                continue

            score = self.score(agent, text)

            if score > best_score:
                best_score = score
                best_agent = agent

        return best_agent

    def score(self, agent, text):

        name = agent.name.lower()

        score = self.base_priority.get(name, 0)

        for keyword in self.keywords.get(name, []):

            if keyword in text:
                score += 10

                if text.strip() == keyword:
                    score += 20

        if name == "coding":

            if any(x in text for x in [
                "debug",
                "bug",
                "error",
                "traceback",
                "exception",
            ]):
                score += 40

        elif name == "music":

            if any(x in text for x in [
                "buat lagu",
                "lirik",
                "chorus",
                "verse",
            ]):
                score += 40

        elif name == "project":

            if any(x in text for x in [
                "status project",
                "struktur project",
                "roadmap",
            ]):
                score += 40

        elif name == "research":

            if text.startswith((
                "apa",
                "siapa",
                "mengapa",
                "kenapa",
                "bagaimana",
                "kapan",
                "di mana",
                "dimana",
                "jelaskan",
            )):
                score += 40

        elif (
            name == "chat"
            and text in [
                "halo",
                "hai",
                "hi",
                "apa kabar",
            ]
        ):
            score += 40

        return score
