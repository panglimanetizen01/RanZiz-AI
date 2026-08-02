"""
RanZiz AI Render Registry
Version 1.0
"""


class RenderRegistry:

    def __init__(self):

        self.renderers = {}

    def register(self, renderer):

        self.renderers[renderer.NAME] = renderer

    def get(self, name):

        return self.renderers.get(name)

    def list_renderers(self):

        return sorted(self.renderers.keys())