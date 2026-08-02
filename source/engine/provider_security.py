from typing import ClassVar

"""
RanZiz AI Provider Security Layer
Version 1.0
"""

import os


class ProviderSecurity:


    SECRET_KEYS: ClassVar = [
        "api_key",
        "token",
        "password",
        "secret"
    ]


    @staticmethod
    def get_api_key(provider_name):

        env_name = (
            provider_name.upper()
            + "_API_KEY"
        )

        return os.getenv(
            env_name,
            ""
        )


    @staticmethod
    def mask(value):

        if not value:
            return ""

        if len(value) <= 8:
            return "****"

        return (
            value[:4]
            + "****"
            + value[-4:]
        )


    @classmethod
    def sanitize(cls, data):

        if not isinstance(data, dict):
            return data

        clean = {}

        for key, value in data.items():

            if any(
                secret in key.lower()
                for secret in cls.SECRET_KEYS
            ):

                clean[key] = cls.mask(
                    str(value)
                )

            else:

                clean[key] = value

        return clean
