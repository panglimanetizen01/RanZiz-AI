"""
RanZiz AI Plugin Loader
Version 2.0
"""

import importlib
import logging
from pathlib import Path

logger = logging.getLogger(__name__)


class PluginLoader:

    def __init__(self):
        self.plugin_path = Path("source/plugins/plugins")

    def load_all(self):

        plugins = {}

        if not self.plugin_path.exists():
            return plugins

        for folder in self.plugin_path.iterdir():

            if not folder.is_dir():
                continue

            try:
                module = importlib.import_module(
                    f"source.plugins.plugins.{folder.name}"
                )

                plugin_class = getattr(
                    module,
                    "Plugin",
                    None
                )

                if plugin_class:
                    plugin = plugin_class()
                    plugins[plugin.name] = plugin

            except Exception:
                # Plugin discovery is isolated; one broken plugin must not
                # prevent other plugins from loading.
                logger.exception(
                    "Plugin %s gagal dimuat",
                    folder.name,
                )
                continue

        return plugins
