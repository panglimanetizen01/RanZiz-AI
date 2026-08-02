from typing import ClassVar

"""
RanZiz AI Provider Configuration
Version 2.0
"""

import os


class ProviderConfig:

    DEFAULT = "local"


    CONFIG: ClassVar = {

        "local": {

            "enabled": True,
            "model": "local",
            "base_url": ""

        },


        "gemini": {

            "enabled": True,
            "model": "gemini-2.5-pro",
            "api_key_env": "GEMINI_API_KEY",
            "base_url": ""

        },


        "openai": {

            "enabled": True,
            "model": "gpt-5.5",
            "api_key_env": "OPENAI_API_KEY",
            "base_url": "https://api.openai.com/v1"

        },


        "ollama": {

            "enabled": True,
            "model": "llama3.1",
            "base_url": "http://localhost:11434"

        },


        "claude": {

            "enabled": True,
            "model": "claude-sonnet",
            "api_key_env": "CLAUDE_API_KEY",
            "base_url": "https://api.anthropic.com"

        },


        "deepseek": {

            "enabled": True,
            "model": "deepseek-chat",
            "api_key_env": "DEEPSEEK_API_KEY",
            "base_url": "https://api.deepseek.com"

        }

    }


    @classmethod
    def get(cls, provider):

        config = cls.CONFIG.get(provider)

        if config is None:
            return None


        result = config.copy()


        env_key = result.get(
            "api_key_env"
        )


        if env_key:

            result["api_key"] = os.getenv(
                env_key,
                ""
            )


        else:

            result["api_key"] = ""


        return result



    @classmethod
    def providers(cls):

        return list(
            cls.CONFIG.keys()
        )