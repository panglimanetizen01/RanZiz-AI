"""
RanZiz AI Episodic Memory
Version 1.0
"""

from datetime import UTC, datetime

from source.database.database_manager import DatabaseManager


class EpisodicMemory:


    def __init__(self):

        self.database = DatabaseManager()


    def record(

        self,

        event,

        category="conversation"

    ):

        data = self.database.load()

        episodes = data.setdefault(

            "episodes",

            []

        )

        item = {

            "timestamp": datetime.now(UTC).isoformat(),

            "category": category,

            "event": event

        }

        episodes.append(

            item

        )

        self.database.save(

            data

        )

        return item



    def all(self):

        data = self.database.load()

        return data.get(

            "episodes",

            []

        )



    def latest(

        self,

        limit=5

    ):

        episodes = self.all()

        return episodes[-limit:]



    def search(

        self,

        keyword

    ):

        keyword = keyword.lower()

        results = []

        for episode in self.all():

            event = episode.get(

                "event",

                ""

            ).lower()

            if keyword in event:

                results.append(

                    episode

                )

        return results



    def __repr__(self):

        return "EpisodicMemory()"