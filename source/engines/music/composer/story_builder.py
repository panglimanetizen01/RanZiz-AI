"""
RanZiz AI Story Builder
Version 5.1
"""

from source.knowledge import KnowledgeManager


class StoryBuilder:

    def __init__(self):

        self.knowledge = KnowledgeManager()


    def build(self, request):

        topic = (request.get("topic") or "KEHIDUPAN").upper()

        emotion = (request.get("emotion") or "HAPPY").upper()


        data = self.knowledge.analyze(
            topic,
            emotion
        )


        concepts = data.get(
            "concepts",
            []
        )


        emotion_data = data.get(
            "emotion",
            {
                "tone": emotion
            }
        )


        while len(concepts) < 4:

            concepts.append(
                "harapan"
            )


        title = self.create_title(topic)


        opening = self.create_opening(
            topic,
            concepts
        )


        conflict = self.create_conflict(
            concepts
        )


        climax = self.create_climax(
            emotion_data
        )


        ending = self.create_ending(
            topic
        )


        return {

            "topic": topic,

            "emotion": emotion,

            "title": title,

            "opening": opening,

            "conflict": conflict,

            "climax": climax,

            "ending": ending

        }


    def create_title(self, topic):

        return f"Tentang {topic.title()}"


    def create_opening(self, topic, concepts):

        return (
            f"Kisah tentang {topic.lower()}, "
            f"yang dipenuhi {concepts[0]} dan {concepts[1]}."
        )


    def create_conflict(self, concepts):

        return (
            f"Perjalanan hidup membawa "
            f"{concepts[2]} dan {concepts[3]}."
        )


    def create_climax(self, emotion):

        return (
            f"Semua berpuncak pada suasana "
            f"{emotion.get('tone', 'indah').lower()}."
        )


    def create_ending(self, topic):

        return (
            f"Pada akhirnya, {topic.lower()} menjadi "
            "kenangan yang tak terlupakan."
        )