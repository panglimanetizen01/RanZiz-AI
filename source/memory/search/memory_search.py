from typing import ClassVar

"""
RanZiz AI Memory Search
Version 3.2
"""

from source.memory.memory_service import MemoryService


class MemorySearch:

    HIDDEN_KEYS: ClassVar = {

        "system_prompt",
        "developer_prompt",
        "internal_prompt",
        "root_prompt"

    }

    def __init__(self):

        self.memory = MemoryService()

    def is_visible(

        self,

        key

    ):

        key = str(key).lower()

        if key in self.HIDDEN_KEYS:

            return False

        if key.startswith("create:"):

            return False

        if key.startswith("system:"):

            return False

        return not key.startswith("_")

    def normalize(

        self,

        item

    ):

        if not isinstance(item, dict):

            return item

        value = item.get(
            "value"
        )

        while (

            isinstance(value, dict)

            and

            "value" in value

        ):

            value = value["value"]

        return value

    def find(

        self,

        keyword

    ):

        keyword = keyword.lower()

        results = []

        memories = self.memory.repository.all()

        for key, item in memories.items():

            if not self.is_visible(key):

                continue

            value = self.normalize(item)

            category = ""

            priority = 3

            if isinstance(item, dict):

                category = item.get(
                    "category",
                    ""
                )

                priority = item.get(
                    "priority",
                    3
                )

            if (

                keyword in key.lower()

                or

                keyword in str(value).lower()

                or

                keyword in category.lower()

            ):

                results.append(

                    (

                        priority,

                        key,

                        value

                    )

                )

        results.sort(

            key=lambda x: x[0],

            reverse=True

        )

        output = {}

        for _, key, value in results:

            output[key] = value

        return output

    def category(

        self,

        category

    ):

        category = category.lower()

        results = []

        memories = self.memory.repository.all()

        for key, item in memories.items():

            if not self.is_visible(key):

                continue

            if not isinstance(item, dict):

                continue

            if item.get(

                "category",

                ""

            ).lower() != category:

                continue

            results.append(

                (

                    item.get(

                        "priority",

                        0

                    ),

                    key,

                    self.normalize(item)

                )

            )

        results.sort(

            key=lambda x: x[0],

            reverse=True

        )

        output = {}

        for _, key, value in results:

            output[key] = value

        return output

    def all(self):

        memories = self.memory.repository.all()

        output = {}

        for key, item in memories.items():

            if not self.is_visible(key):

                continue

            output[key] = self.normalize(item)

        return output

    def __repr__(self):

        return "MemorySearch()"
