"""
RanZiz AI Conversation Repository
Version 3.0
"""

from copy import deepcopy

from source.database.database_manager import DatabaseManager


class ConversationRepository:

    MAX_HISTORY = 200
    MAX_MESSAGE_LENGTH = 5000

    def __init__(self):

        self.database = DatabaseManager()

    def clean_messages(self, session):

        session = deepcopy(session)

        history = session.get("history", [])

        cleaned = []

        for item in history[-self.MAX_HISTORY:]:

            cleaned.append(
                {
                    "role": item.get("role", "user"),
                    "content": str(
                        item.get("content", "")
                    )[:self.MAX_MESSAGE_LENGTH],
                    "time": item.get("time"),
                }
            )

        session["history"] = cleaned

        return session

    def save_conversation(

        self,
        session_id,
        session

    ):

        data = self.database.load()

        data["sessions"][session_id] = (
            self.clean_messages(session)
        )

        self.database.save(data)

    def get_conversation(

        self,
        session_id

    ):

        data = self.database.load()

        return data["sessions"].get(
            session_id
        )

    def delete_conversation(

        self,
        session_id

    ):

        data = self.database.load()

        if session_id in data["sessions"]:

            del data["sessions"][session_id]

            self.database.save(data)

    def list_sessions(self):

        data = self.database.load()

        return list(
            data["sessions"].keys()
        )

    def clear(self):

        data = self.database.load()

        data["sessions"] = {}

        self.database.save(data)

    def __repr__(self):

        return "ConversationRepository()"