"""
RanZiz AI Capability Selector
Version 1.5
"""

from source.capability.catalog.catalog_service import CatalogService


class CapabilitySelector:

    def __init__(self):

        self.catalog = CatalogService()

    def select(
        self,
        goal
    ):

        goal = str(goal).upper()

        category_map = {

            "MUSIC": [
                "MUSIC"
            ],

            "CODING": [
                "CODING"
            ],

            "APPLICATION": [
                "CODING"
            ],

            "WEBSITE": [
                "WEBSITE"
            ],

            "RESEARCH": [
                "RESEARCH"
            ],

            "MARKETING": [
                "MARKETING"
            ],

            "IMAGE": [
                "IMAGE"
            ],

            "VIDEO": [
                "VIDEO"
            ],

            "DOCUMENT": [
                "DOCUMENT"
            ],

            "VISION": [
                "VISION"
            ],

            "VOICE": [
                "VOICE"
            ]

        }

        allowed = category_map.get(
            goal,
            []
        )

        capabilities = []

        for item in self.catalog.list():

            if item["category"].upper() in allowed:

                capabilities.append(
                    item["name"]
                )

        dependency_order = {

            "Lyric Engine": 1,
            "Composer": 2,
            "Audio Engine": 3

        }

        capabilities.sort(
            key=lambda x: dependency_order.get(
                x,
                99
            )
        )

        return capabilities
