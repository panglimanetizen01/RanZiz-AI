"""
RanZiz AI Logger
Version 3.0
"""

from pathlib import Path

from source.database.repository.log_repository import LogRepository
from source.logger.log_entry import LogEntry


class Logger:


    def __init__(self):

        self.logs = []

        self.repository = LogRepository()

        self.log_dir = Path("logs")

        self.log_dir.mkdir(
            exist_ok=True
        )

        self.log_file = (
            self.log_dir /
            "system.log"
        )


    def write(

        self,

        level,

        category,

        message,

        metadata=None

    ):

        entry = LogEntry(

            level=level,

            category=category,

            message=message,

            metadata=metadata

        )

        self.logs.append(
            entry
        )

        self.save_file(
            entry
        )

        self.repository.save(
            entry
        )

        return entry


    def save_file(
        self,
        entry
    ):

        with open(

            self.log_file,

            "a",

            encoding="utf-8"

        ) as file:

            file.write(

                f"{entry.timestamp} | "

                f"{entry.level} | "

                f"{entry.category} | "

                f"{entry.message}"

            )

            if entry.metadata:

                file.write(
                    f" | {entry.metadata}"
                )

            file.write("\n")


    def info(self, category, message, metadata=None):

        return self.write(
            "INFO",
            category,
            message,
            metadata
        )


    def warning(self, category, message, metadata=None):

        return self.write(
            "WARNING",
            category,
            message,
            metadata
        )


    def error(self, category, message, metadata=None):

        return self.write(
            "ERROR",
            category,
            message,
            metadata
        )


    def all(self):

        return [
            item.to_dict()
            for item in self.logs
        ]


    def clear(self):

        self.logs.clear()