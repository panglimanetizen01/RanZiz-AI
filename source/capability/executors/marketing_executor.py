"""
RanZiz AI Marketing Executor
Version 1.0
"""

from source.capability.base_executor import BaseCapabilityExecutor
from source.capability.schema.capability_info import CapabilityInfo


class MarketingExecutor(BaseCapabilityExecutor):

    def execute(self, payload):

        message = payload.get(
            "message",
            ""
        )

        return (
            "Marketing Engine Result\n\n"
            f"Product Request : {message}\n\n"
            "Headline : Nikmati kopi pilihan dengan rasa yang membuat hari lebih hidup.\n"
            "Description : Kopi berkualitas dengan aroma khas untuk menemani aktivitas Anda.\n"
            "CTA : Pesan sekarang dan rasakan pengalaman kopi terbaik.\n"
            "Status : Marketing workflow ready"
        )


    def metadata(self):

        return CapabilityInfo(

            name="Marketing Engine",

            category="Marketing",

            description="Membuat konsep iklan dan copywriting produk",

            inputs=[
                "text"
            ],

            outputs=[
                "advertisement"
            ],

            requires=[],

            priority=10

        )
