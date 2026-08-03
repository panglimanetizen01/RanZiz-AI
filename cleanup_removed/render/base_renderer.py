"""
RanZiz AI Base Renderer
Version 1.0
"""


class BaseRenderer:

    NAME = "BaseRenderer"

    def render(self, project, data):

        raise NotImplementedError(
            "Renderer harus mengimplementasikan method render()."
        )