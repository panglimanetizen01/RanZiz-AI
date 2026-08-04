"""
RanZiz AI Capability Dependency Resolver
Version 1.0
"""



class CapabilityDependencyResolver:


    def __init__(
        self,
        registry
    ):

        self.registry = registry



    def dependencies(
        self,
        capability
    ):

        info = self.registry.info(
            capability
        )


        if info is None:

            return []


        return info.get(
            "requires",
            []
        )



    def resolve(
        self,
        capabilities
    ):

        resolved = []

        visited = set()


        for capability in capabilities:

            self._visit(
                capability,
                resolved,
                visited
            )


        return resolved



    def _visit(
        self,
        capability,
        resolved,
        visited
    ):

        if capability in visited:

            return


        visited.add(
            capability
        )


        for dependency in self.dependencies(
            capability
        ):

            self._visit(
                dependency,
                resolved,
                visited
            )


        resolved.append(
            capability
        )



    def graph(self):

        result = {}


        for capability in self.registry.list():

            result[capability] = self.dependencies(
                capability
            )


        return result



    def __repr__(self):

        return (
            "CapabilityDependencyResolver()"
        )
