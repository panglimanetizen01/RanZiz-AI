"""
RanZiz AI Context Manager
Version 1.0
"""


class ContextManager:

    def __init__(self):

        self.context = {}

    def set(self, key, value):

        self.context[key] = value

    def get(self, key, default=None):

        return self.context.get(key, default)

    def has(self, key):

        return key in self.context

    def remove(self, key):

        if key in self.context:

            del self.context[key]

    def clear(self):

        self.context.clear()

    def all(self):

        return dict(self.context)