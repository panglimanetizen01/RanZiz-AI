"""
RanZiz AI Service Container
Version 1.0
"""

class ServiceContainer:


    def __init__(self):

        self._services = {}



    def register(

        self,

        name,

        service

    ):

        self._services[name] = service



    def get(

        self,

        name

    ):

        return self._services.get(name)



    def exists(

        self,

        name

    ):

        return name in self._services



    def remove(

        self,

        name

    ):

        if name in self._services:

            del self._services[name]



    def clear(

        self

    ):

        self._services.clear()



    def all(

        self

    ):

        return dict(self._services)



    def __len__(

        self

    ):

        return len(self._services)



    def __repr__(

        self

    ):

        return (
            f"ServiceContainer("
            f"{len(self._services)} services)"
        )