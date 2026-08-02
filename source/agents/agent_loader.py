"""
RanZiz AI Agent Loader
Version 3.0
"""

import importlib
import inspect
import pkgutil

from source.agents import __path__


class AgentLoader:


    def load(self):

        agents = {}

        package = "source.agents"


        for module_info in pkgutil.walk_packages(
            __path__,
            package + "."
        ):

            module_name = module_info.name


            # hanya ambil agent dalam folder spesialis
            allowed = [
                ".music.",
                ".coding.",
                ".research."
            ]


            if not any(
                item in module_name
                for item in allowed
            ):
                continue


            if not module_name.endswith(
                "_agent"
            ):
                continue


            module = importlib.import_module(
                module_name
            )


            for _, obj in inspect.getmembers(
                module,
                inspect.isclass
            ):

                if obj.__module__ != module.__name__:
                    continue


                if not obj.__name__.endswith(
                    "Agent"
                ):
                    continue


                try:

                    instance = obj()

                except TypeError:

                    continue


                if hasattr(
                    instance,
                    "name"
                ):

                    agents[
                        instance.name
                    ] = instance


        return agents