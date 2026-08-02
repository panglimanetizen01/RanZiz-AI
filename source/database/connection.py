"""
RanZiz AI Database Connection
Version 1.1
"""

import sqlite3
from pathlib import Path


class DatabaseConnection:

    def __init__(self):

        Path("database").mkdir(
            exist_ok=True
        )

        self.path = "database/ranziz.db"


    def connect(self):

        db = sqlite3.connect(
            self.path
        )

        self._migrate(db)

        return db


    def _migrate(self, db):

        cursor = db.cursor()

        cursor.execute(
            """
            CREATE TABLE IF NOT EXISTS logs (

                id INTEGER PRIMARY KEY AUTOINCREMENT,

                timestamp TEXT NOT NULL,

                level TEXT NOT NULL,

                category TEXT NOT NULL,

                message TEXT NOT NULL,

                metadata TEXT

            )
            """
        )

        db.commit()
