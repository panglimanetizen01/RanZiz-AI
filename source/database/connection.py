"""
RanZiz AI Database Connection
Version 1.0
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

        return sqlite3.connect(
            self.path
        )