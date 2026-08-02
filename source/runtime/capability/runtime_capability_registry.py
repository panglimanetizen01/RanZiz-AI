"""
RanZiz AI Runtime Capability Registry
Version 1.0
"""


class RuntimeCapabilityRegistry:


    def __init__(

        self

    ):

        self.capabilities = {}



    def register(

        self,

        name,

        capability

    ):

        self.capabilities[name] = capability



    def get(

        self,

        name

    ):

        return self.capabilities.get(

            name

        )



    def exists(

        self,

        name

    ):

        return (

            name in self.capabilities

        )



    def all(

        self

    ):

        return dict(

            self.capabilities

        )



    def clear(

        self

    ):

        self.capabilities.clear()