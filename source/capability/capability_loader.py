"""
RanZiz AI Capability Loader
Version 2.1
"""

import importlib
import pkgutil

from source.capability.base_executor import BaseCapabilityExecutor
from source.capability.executors import __path__


class CapabilityLoader:


    def load(self):

        executors = {}

        package = "source.capability.executors"

        for _, module_name, _ in pkgutil.iter_modules(__path__):

            if not module_name.endswith("_executor"):
                continue

            try:

                module = importlib.import_module(
                    f"{package}.{module_name}"
                )

                for name in dir(module):

                    obj = getattr(module, name)

                    if not isinstance(obj, type):
                        continue

                    if name.startswith("Base"):
                        continue

                    if not name.endswith("Executor"):
                        continue

                    if not issubclass(
                        obj,
                        BaseCapabilityExecutor
                    ):
                        continue

                    instance = obj()

                    capability = self.normalize(
                        name.replace(
                            "Executor",
                            ""
                        )
                    )

                    executors[capability] = instance

            except Exception as error:  # noqa: BLE001
                # Capability loading is isolated; one failed capability must not stop the runtime.
                print(
                    "Capability gagal dimuat:",
                    module_name,
                    error
                )

        return executors


    def normalize(self, name):

        mapping = {

            "Lyric": "Lyric Engine",

            "Composer": "Composer",

            "Audio": "Audio Engine",

            "Code": "Code Engine",

            "Research": "Research Engine",

            "Image": "Image Engine",

            "Website": "Website Engine",

            "Video": "Video Engine",

            "Voice": "Voice Engine",

            "Script": "Script Engine",

        }

        return mapping.get(
            name,
            f"{name} Engine"
        )
