"""
RanZiz AI Capability Service
Version 2.0
"""

from collections import defaultdict

from source.capability.catalog.catalog_service import CatalogService


class CapabilityService:


    def __init__(self):

        self.catalog = CatalogService()



    def all(self):

        return self.catalog.list()



    def count(self):

        return self.catalog.count()



    def summary(self):

        return self.catalog.summary()



    def describe(self):

        return self.summary()["capabilities"]



    def find(
        self,
        keyword
    ):

        return self.catalog.find(
            keyword
        )



    def text(self):

        summary = self.summary()

        groups = defaultdict(list)


        for item in summary["capabilities"]:

            groups[item["category"]].append(
                item
            )


        lines = []


        lines.append(
            f"RanZiz AI memiliki {summary['count']} capability.\n"
        )


        for category in sorted(groups):

            lines.append(
                f"\n[{category}]"
            )


            for item in sorted(
                groups[category],
                key=lambda x: x["priority"]
            ):

                lines.append(
                    f"• {item['name']}"
                )

                lines.append(
                    f"  {item['description']}"
                )


        return "\n".join(lines)



    def __repr__(self):

        return (
            f"CapabilityService("
            f"{self.count()} capabilities)"
        )

    def pilih_dari_keputusan(self, hasil_analisis: Dict):
        """Ambil daftar kemampuan langsung dari hasil keputusan Decision Engine"""
        daftar_nama = hasil_analisis.get("kemampuan_dipilih", [])
        if not daftar_nama:
            return [self.registry.cari("ChatCapability")]
        return [self.registry.cari(nama) for nama in daftar_nama if self.registry.ada(nama)]

    def dapatkan_provider_urut(self, capability_nama: str):
        """Ambil urutan provider terbaik untuk kemampuan ini"""
        from source.engine.provider.provider_selector import ProviderSelector
        return ProviderSelector.pilih(capability_nama)
