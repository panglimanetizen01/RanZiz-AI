"""
RanZiz AI Provider Registry Builder
Version 1.0
"""


class ProviderRegistryBuilder:

    def __init__(self):

        self.providers = {}

    def add(self, name, provider):

        self.providers[name] = provider

        return self

    def build(self):

        return dict(self.providers)