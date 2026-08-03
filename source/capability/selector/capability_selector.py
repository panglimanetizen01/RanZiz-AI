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
        goal,
        text=None
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

        # Video musik membutuhkan pipeline lengkap:
        # Lyric -> Composer -> Audio -> Video
        if (
            goal == "VIDEO"
            and text is not None
            and any(
                word in str(text).lower()
                for word in [
                    "lagu",
                    "musik",
                    "lirik"
                ]
            )
        ):
            return [
                "Lyric Engine",
                "Composer",
                "Audio Engine",
                "Video Engine"
            ]


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

        def resolve_dependencies(
            names
        ):

            resolved = []

            def add(name):

                if name in resolved:
                    return

                item = self.catalog.get(
                    name
                )

                if item:

                    for req in item.get(
                        "requires",
                        []
                    ):
                        add(req)

                resolved.append(
                    name
                )


            for name in names:
                add(name)

            return resolved


        capabilities = resolve_dependencies(
            capabilities
        )


        capabilities.sort(
            key=lambda x: dependency_order.get(
                x,
                99
            )
        )

        return capabilities
