"""
RanZiz AI Capability Catalog Service
Version 2.0
"""

from source.capability.capability_router import CapabilityRouter


class CatalogService:


    def __init__(self):

        self.router = CapabilityRouter()



    def list(self):

        result = []

        for name in self.router.available():

            info = self.router.info(
                name
            )

            if info is not None:

                result.append(
                    info
                )

        return result



    def find(
        self,
        keyword
    ):

        keyword = keyword.lower()

        results = []


        for item in self.list():

            text = (
                item["name"]
                + " "
                + item["category"]
                + " "
                + item["description"]
            ).lower()


            if keyword in text:

                results.append(
                    item
                )


        return results



    def summary(self):

        capabilities = self.list()

        return {

            "count": len(capabilities),

            "capabilities": capabilities

        }



    def count(self):

        return self.router.count()



    def __repr__(self):

        return (
            f"CatalogService("
            f"{self.count()} capabilities)"
        )
