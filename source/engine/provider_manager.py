"""
RanZiz AI Provider Manager
Version 3.0
"""

from source.engine.provider_registry import load_providers


class ProviderManager:

    def __init__(self):

        self.providers = load_providers()

    def list_providers(self):

        return list(
            self.providers.keys()
        )

    def get(

        self,

        name

    ):

        if not name:

            return None

        return self.providers.get(
            name.lower()
        )

    def get_by_capability(

        self,

        capability

    ):

        for provider in self.providers.values():

            if provider.supports(
                capability
            ) and self.is_ready(
                provider
            ):

                return provider

        return None

    def has(

        self,

        name

    ):

        return self.get(name) is not None

    def is_ready(

        self,

        provider

    ):

        try:

            provider.models()

            return True

        except Exception:  # noqa: BLE001
            # Provider health checks must never propagate failures.
            return False

    def health(self):

        result = {}

        for name, provider in self.providers.items():

            result[name] = {

                "provider": name,

                "ready": self.is_ready(
                    provider
                ),

                "capabilities": provider.capabilities,

                "models": provider.models()

            }

        return result

    def ready_providers(self):

        result = []

        for name, provider in self.providers.items():

            if self.is_ready(
                provider
            ):

                result.append(
                    name
                )

        return result

    def info(self):

        output = {}

        for name, provider in self.providers.items():

            output[name] = provider.info()

        return output

    def __repr__(self):

        return "ProviderManager()"