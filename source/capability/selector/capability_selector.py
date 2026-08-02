"""
RanZiz AI Capability Selector
Version 1.4
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

        capabilities = []


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
                "CODING"
            ],

            "RESEARCH": [
                "RESEARCH"
            ],

            "IMAGE": [
                "IMAGE"
            ],

            "VIDEO": [
                "IMAGE"
            ]

        }


        allowed_categories = category_map.get(
            goal,
            []
        )


        for item in self.catalog.list():

            category = item.get(
                "category",
                ""
            ).upper()


            if category in allowed_categories:

                capabilities.append(
                    item["name"]
                )


        dependency_order = {

            "Lyric Engine": 1,

            "Composer": 2,

            "Audio Engine": 3

        }


        capabilities.sort(
            key=lambda name: dependency_order.get(
                name,
                99
            )
        )


        return capabilities