"""
RanZiz AI Provider Registry
Version 3.0
"""

import importlib
from pathlib import Path


def _legacy_class_name(module_name):

    special = {

        "openai_provider": "OpenAIProvider",

        "deepseek_provider": "DeepSeekProvider",

    }

    if module_name in special:

        return special[module_name]

    base = module_name.replace(

        "_provider",

        ""

    )

    return (

        "".join(

            word.capitalize()

            for word in base.split("_")

        )

        + "Provider"

    )


def _load_provider(module_name):

    module = importlib.import_module(

        f"source.engine.providers.{module_name}"

    )

    provider_class = getattr(

        module,

        "Provider",

        None

    )

    if provider_class is None:

        provider_class = getattr(

            module,

            _legacy_class_name(

                module_name

            )

        )

    provider = provider_class()

    if not hasattr(

        provider,

        "name"

    ):

        raise AttributeError(

            "Provider tidak memiliki atribut name"

        )

    if not hasattr(

        provider,

        "capabilities"

    ):

        raise AttributeError(

            "Provider tidak memiliki capabilities"

        )

    if not callable(

        getattr(

            provider,

            "models",

            None

        )

    ):

        raise TypeError(

            "Provider tidak memiliki method models()"

        )

    return provider


def load_providers():

    providers = {}

    providers_dir = (

        Path(__file__).parent

        / "providers"

    )

    loaded = set()

    failed = {}

    for file in sorted(

        providers_dir.glob(

            "*_provider.py"

        )

    ):

        module_name = file.stem

        if module_name == "base_provider":

            continue

        try:

            provider = _load_provider(

                module_name

            )

            name = provider.name.lower()

            if name in loaded:

                raise ValueError(

                    f"Provider '{name}' sudah terdaftar"

                )

            providers[name] = provider

            loaded.add(name)

        except Exception as error:  # noqa: BLE001
            # Provider discovery must continue even if one provider fails to load.
            failed[module_name] = str(error)

            print(

                "[ProviderRegistry]",

                module_name,

                "gagal dimuat:",

                error

            )

    load_providers.failed = failed

    return providers


def failed_providers():

    return getattr(

        load_providers,

        "failed",

        {}

    )
