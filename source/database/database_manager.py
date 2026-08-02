from typing import ClassVar

"""
RanZiz AI Database Manager
Version 3.0
"""

import json
import os
import shutil


class DatabaseManager:

    DEFAULT_DATABASE: ClassVar = {

        "sessions": {},

        "memory": {},

        "settings": {},

        "observability": {}

    }

    def __init__(

        self,

        filename="database.json"

    ):

        self.filename = filename

        self.backup = filename + ".bak"
        self.temp = filename + ".tmp"

        if not os.path.exists(self.filename):

            self.save(
                self.DEFAULT_DATABASE.copy()
            )

        else:

            self._ensure_structure()

    def _ensure_structure(self):

        data = self.load()

        changed = False

        for key, value in self.DEFAULT_DATABASE.items():

            if key not in data:

                data[key] = value

                changed = True

        if changed:

            self.save(data)

    def load(self):

        try:

            with open(

                self.filename,

                "r",

                encoding="utf-8"

            ) as file:

                return json.load(file)

        except (
            FileNotFoundError,
            PermissionError,
            OSError,
            json.JSONDecodeError
        ):

            if os.path.exists(self.backup):

                with open(

                    self.backup,

                    "r",

                    encoding="utf-8"

                ) as file:

                    return json.load(file)

            return self.DEFAULT_DATABASE.copy()

    def save(

        self,

        data

    ):

        with open(

            self.temp,

            "w",

            encoding="utf-8"

        ) as file:

            json.dump(

                data,

                file,

                indent=4,

                ensure_ascii=False

            )

            file.flush()

            os.fsync(file.fileno())

        if os.path.exists(self.filename):

            shutil.copy2(

                self.filename,

                self.backup

            )

        os.replace(

            self.temp,

            self.filename

        )

    def reset(self):

        self.save(

            self.DEFAULT_DATABASE.copy()

        )

    def __repr__(self):

        return (

            f"DatabaseManager('{self.filename}')"

        )