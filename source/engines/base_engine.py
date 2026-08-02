"""
RanZiz AI Base Engine
Version 1.0
"""


class BaseEngine:

    NAME = "BaseEngine"

    def run(self, project, request):

        raise NotImplementedError(
            "Engine harus mengimplementasikan method run()."
        )