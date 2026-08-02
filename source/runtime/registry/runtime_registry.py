"""
RanZiz AI Runtime Registry
Version 1.0
"""


class RuntimeRegistry:


    def __init__(

        self

    ):

        self.runtimes = {}



    def register(

        self,

        name,

        runtime

    ):

        self.runtimes[name] = runtime



    def get(

        self,

        name

    ):

        return self.runtimes.get(

            name

        )



    def exists(

        self,

        name

    ):

        return name in self.runtimes



    def remove(

        self,

        name

    ):

        if name in self.runtimes:

            del self.runtimes[name]



    def all(

        self

    ):

        return dict(

            self.runtimes

        )