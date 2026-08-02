"""
RanZiz AI Log Repository
Version 1.0
"""

import json

from source.database.connection import DatabaseConnection


class LogRepository:


    def __init__(self):

        self.connection = DatabaseConnection()


    def save(self, entry):

        db = self.connection.connect()

        cursor = db.cursor()

        cursor.execute(

            """

            INSERT INTO logs(

                timestamp,

                level,

                category,

                message,

                metadata

            )

            VALUES(

                ?, ?, ?, ?, ?

            )

            """,

            (

                entry.timestamp,

                entry.level,

                entry.category,

                entry.message,

                json.dumps(
                    entry.metadata
                )

            )

        )

        db.commit()

        db.close()


    def all(self):

        db = self.connection.connect()

        cursor = db.cursor()

        cursor.execute(

            """

            SELECT

                timestamp,

                level,

                category,

                message,

                metadata

            FROM logs

            ORDER BY id

            """

        )

        rows = cursor.fetchall()

        db.close()

        return rows