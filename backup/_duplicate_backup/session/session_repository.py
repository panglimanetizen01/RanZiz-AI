"""
RanZiz AI Session Repository
Version 1.1
"""

from src.database.conversation_repository import ConversationRepository


class SessionRepository:


    def __init__(self):

        self.repository = ConversationRepository()



    def save(

        self,

        session

    ):

        self.repository.save_conversation(

            session.id,

            session.to_dict()

        )



    def load(

        self,

        session_id

    ):

        return self.repository.get_conversation(

            session_id

        )



    def delete(

        self,

        session_id

    ):

        self.repository.delete_conversation(

            session_id

        )



    def list_sessions(self):

        return self.repository.list_sessions()



    def __repr__(self):

        return "SessionRepository()"