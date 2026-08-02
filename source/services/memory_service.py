"""
RanZiz AI Memory Service
Version 3.1
"""

import json
from pathlib import Path

from source.config.config import Config
from source.events.event_bus import EventBus
from source.events.event_subscriber import EventSubscriber


class MemoryService:

    MEMORY_FILE = Path(Config.MEMORY_FILE)

    def __init__(self):

        self.bus = EventBus()

        self.history = []

        self.load()

        self.bus.subscribe(

            "plugin.executed",

            EventSubscriber(

                "MemoryService",

                self.on_plugin_executed

            )

        )


    def normalize(self, item):

        if not isinstance(item, dict):

            return {
                "type": "unknown",
                "source": "unknown",
                "user": str(item),
                "assistant": ""
            }

        if "assistant" in item:

            return {
                "type": item.get("type", "chat"),
                "source": item.get("source", "unknown"),
                "user": item.get("user", ""),
                "assistant": item.get("assistant", "")
            }

        if "ai" in item:

            return {
                "type": "chat",
                "source": "legacy",
                "user": item.get("user", ""),
                "assistant": item.get("ai", "")
            }

        return item


    def on_plugin_executed(

        self,

        event

    ):

        data = getattr(

            event,

            "data",

            event

        )

        self.add(

            data

        )


    def add(self, data):

        data = self.normalize(data)

        if self.history and self.history[-1] == data:
            return

        self.history.append(data)

        self.save()


    def last(self, limit=10):

        return self.history[-limit:]


    def search(self, keyword):

        keyword = keyword.lower()

        results = []

        for item in self.history:

            if keyword in str(item).lower():

                results.append(item)

        return results


    def get_history(self):

        return list(self.history)


    def clear(self):

        self.history.clear()

        self.save()


    def load(self):

        if not self.MEMORY_FILE.exists():

            return

        try:

            with self.MEMORY_FILE.open(

                "r",

                encoding="utf-8"

            ) as file:

                data = json.load(file)

            if isinstance(data, list):

                self.history = [

                    self.normalize(item)

                    for item in data

                ]

        except (
            FileNotFoundError,
            PermissionError,
            OSError,
            json.JSONDecodeError
        ):

            self.history = []


    def save(self):

        with self.MEMORY_FILE.open(

            "w",

            encoding="utf-8"

        ) as file:

            json.dump(

                self.history,

                file,

                ensure_ascii=False,

                indent=4

            )
