"""
RanZiz AI Database Migration
Version 1.0
"""

from source.database.connection import DatabaseConnection


class DatabaseMigration:


    def __init__(self):

        self.connection = DatabaseConnection()


    def migrate(self):

        db = self.connection.connect()

        cursor = db.cursor()


        cursor.execute("""

        CREATE TABLE IF NOT EXISTS logs (

            id INTEGER PRIMARY KEY AUTOINCREMENT,

            timestamp TEXT NOT NULL,

            level TEXT NOT NULL,

            category TEXT NOT NULL,

            message TEXT NOT NULL,

            metadata TEXT

        )

        """)


        db.commit()

        db.close()

        return "Migration SUCCESS"