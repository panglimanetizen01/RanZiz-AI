from typing import ClassVar

"""
RanZiz AI Memory Repository
Version 3.0
"""

from datetime import UTC, datetime

from source.database.database_manager import DatabaseManager
from source.memory.classifier.memory_classifier import MemoryClassifier
from source.memory.priority.memory_priority import MemoryPriority


class MemoryRepository:


    MAX_KEY_LENGTH = 200
    MAX_VALUE_LENGTH = 10000

    BLOCKED_KEYS: ClassVar = {
        "system",
        "system_prompt",
        "developer",
        "admin",
        "root",
        "password",
        "secret",
        "api_key"
    }


    def __init__(self):

        self.database = DatabaseManager()

        self.classifier = MemoryClassifier()

        self.priority = MemoryPriority()



    def sanitize_key(self, key):

        key = str(key).strip()

        if len(key) > self.MAX_KEY_LENGTH:

            key = key[:self.MAX_KEY_LENGTH]


        lowered = key.lower()

        for blocked in self.BLOCKED_KEYS:

            if blocked in lowered:

                raise ValueError(
                    "Memory key tidak diperbolehkan"
                )

        return key



    def sanitize_value(self, value):

        if value is None:

            raise ValueError(
                "Memory value kosong"
            )


        value = str(value).strip()


        if len(value) > self.MAX_VALUE_LENGTH:

            value = value[:self.MAX_VALUE_LENGTH]


        return value



    def save(

        self,

        key,

        value

    ):

        key = self.sanitize_key(key)

        value = self.sanitize_value(value)


        data = self.database.load()


        memory = data.setdefault(

            "memory",

            {}

        )


        now = datetime.now(UTC).isoformat()


        category = self.classifier.classify(

            key,

            value

        )


        priority = self.priority.calculate(

            key,

            category

        )


        created_at = now


        if (

            key in memory

            and isinstance(

                memory[key],

                dict

            )

        ):

            created_at = memory[key].get(

                "created_at",

                now

            )


        memory[key] = {

            "value": value,

            "category": category,

            "priority": priority,

            "created_at": created_at,

            "updated_at": now

        }


        self.database.save(

            data

        )


        return memory[key]



    def get(

        self,

        key,

        default=None

    ):

        data = self.database.load()

        memory = data.get(

            "memory",

            {}

        )


        item = memory.get(

            key

        )


        if item is None:

            return default


        if isinstance(

            item,

            dict

        ):

            return item.get(

                "value",

                default

            )


        return item



    def all(self):

        data = self.database.load()

        return data.get(

            "memory",

            {}

        )



    def list(self):

        result = {}


        for key, item in self.all().items():

            if isinstance(

                item,

                dict

            ):

                result[key] = item.get(

                    "value"

                )

            else:

                result[key] = item


        return result



    def delete(

        self,

        key

    ):

        data = self.database.load()


        memory = data.get(

            "memory",

            {}

        )


        if key in memory:

            del memory[key]

            self.database.save(

                data

            )

            return True


        return False



    def exists(

        self,

        key

    ):

        return key in self.all()



    def __repr__(self):

        return "MemoryRepository()"