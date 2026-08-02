"""
RanZiz AI Knowledge Manager
Version 2.0
"""

from source.knowledge.concept_engine import ConceptEngine
from source.knowledge.emotion_engine import EmotionEngine
from source.knowledge.topic_engine import TopicEngine


class KnowledgeManager:

    def __init__(self):

        self.topic = TopicEngine()

        self.concept = ConceptEngine()

        self.emotion = EmotionEngine()

    def analyze(self, topic, emotion):

        topic_data = self.topic.get(topic)

        keywords = topic_data["keywords"]

        concepts = self.concept.expand(
            keywords
        )

        emotion_data = self.emotion.get(
            emotion
        )

        return {

            "topic": topic,

            "keywords": keywords,

            "concepts": concepts,

            "emotion": emotion_data

        }