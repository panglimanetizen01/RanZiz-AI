from typing import ClassVar

"""
RanZiz AI Runtime Adapter
Version 3.3
"""

from source.engine.provider_manager import ProviderManager


class RuntimeAdapter:

    RULES: ClassVar = [
        {
            "keywords": [
                "website",
                "web",
                "html",
                "css",
                "javascript",
                "react",
                "vue",
                "laravel",
                "django",
                "flask",
                "api",
            ],
            "provider": "claude",
        },
        {
            "keywords": [
                "python",
                "java",
                "kotlin",
                "android",
                "bug",
                "debug",
                "program",
                "kode",
                "coding",
                "algorithm",
                "algoritma",
            ],
            "provider": "deepseek",
        },
        {
            "keywords": [
                "gambar",
                "logo",
                "image",
                "poster",
                "foto",
                "design",
                "desain",
            ],
            "provider": "openai",
            "capability": "image",
        },
        {
            "keywords": [
                "musik",
                "lagu",
                "audio",
            ],
            "provider": "gemini",
            "capability": "audio",
        },
    ]

    def __init__(self):
        self.providers = ProviderManager()

    def select(self, prompt):

        text = str(prompt).lower()

        for rule in self.RULES:

            for keyword in rule["keywords"]:

                if keyword in text:

                    provider = self.providers.get(
                        rule["provider"]
                    )

                    if provider:

                        capability = rule.get(
                            "capability",
                            "chat"
                        )

                        if provider.supports(
                            capability
                        ):
                            return provider

        provider = self.providers.get(
            "local"
        )

        if provider:
            return provider

        return self.providers.get_by_capability(
            "chat"
        )

    def select_provider(
        self,
        name
    ):

        provider = self.providers.get(
            name
        )

        if provider:
            return provider

        return self.providers.get(
            "local"
        )

    def ask(
        self,
        prompt
    ):

        provider = self.select(
            prompt
        )

        return provider.ask(
            prompt
        )

    def ask_with_provider(
        self,
        provider_name,
        prompt
    ):

        provider = self.select_provider(
            provider_name
        )

        return provider.ask(
            prompt
        )

    # ==================================================
    # Compatibility Layer
    # ==================================================

    def process(
        self,
        message,
        context=None
    ):

        # Legacy Runtime (dipakai unit test lama)
        if hasattr(self, "runtime"):

            if hasattr(self.runtime, "chat"):

                try:
                    return self.runtime.chat(
                        message,
                        context
                    )

                except TypeError:
                    return self.runtime.chat(
                        message
                    )

            if hasattr(self.runtime, "execute"):

                return self.runtime.execute(
                    message,
                    context
                )

        # Provider Runtime
        provider = self.select(
            message
        )

        if hasattr(provider, "chat"):

            try:
                return provider.chat(
                    message,
                    context
                )

            except TypeError:
                return provider.chat(
                    message
                )

        return provider.ask(
            message
        )

    # ==================================================

    def provider(
        self,
        prompt=None
    ):

        if prompt is None:
            return self.providers.get(
                "local"
            )

        return self.select(
            prompt
        )

    def ready(self):

        return self.providers.ready_providers()

    def health(self):

        return self.providers.health()

        # ==================================================

    def execute(
        self,
        message,
        context=None
    ):
        return self.process(
            message,
            context
        )
    
    def info(self):

        return self.providers.info()

    def __repr__(self):

        return "RuntimeAdapter()"