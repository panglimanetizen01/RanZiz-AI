"""
RanZiz AI Memory Migration
Version 1.0
"""

from datetime import UTC, datetime

from source.memory.classifier.memory_classifier import MemoryClassifier
from source.memory.priority.memory_priority import MemoryPriority


class MemoryMigration:


    def __init__(self):

        self.classifier = MemoryClassifier()

        self.priority = MemoryPriority()


    def migrate(

        self,

        memories

    ):

        now = datetime.now(UTC).isoformat()

        migrated = {}

        for key, value in memories.items():

            if isinstance(value, dict):

                migrated[key] = value

                continue

            category = self.classifier.classify(

                key,

                value

            )

            migrated[key] = {

                "value": value,

                "category": category,

                "created_at": now,

                "updated_at": now,

                "priority": self.priority.calculate(
                    category
                )

            }

        return migrated


    def __repr__(self):

        return "MemoryMigration()"