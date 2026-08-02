"""
RanZiz AI Session Manager
Version 2.0
"""

from source.session.session_registry import SessionRegistry
from source.session.session_repository import SessionRepository


class SessionManager:


    def __init__(self):

        self.registry = SessionRegistry()

        self.repository = SessionRepository()



    def create(self):

        session = self.registry.create()

        self.repository.save(

            session

        )

        return session



    def get(

        self,

        session_id

    ):

        return self.registry.get(

            session_id

        )



    def get_or_create(

        self,

        session_id=None

    ):

        if session_id:

            session = self.get(

                session_id

            )

            if session:

                return session

        return self.create()



    def remove(

        self,

        session_id

    ):

        self.repository.delete(

            session_id

        )

        return self.registry.remove(

            session_id

        )



    def add_message(

        self,

        session_id,

        role,

        content

    ):

        session = self.get(

            session_id

        )

        if session is None:

            return None

        session.add_message(

            role,

            content

        )

        self.repository.save(

            session

        )

        return session



    def set_context(

        self,

        session_id,

        key,

        value

    ):

        session = self.get(

            session_id

        )

        if session is None:

            return None

        session.set(

            key,

            value

        )

        self.repository.save(

            session

        )

        return session



    def list(self):

        return self.registry.list()



    def count(self):

        return self.registry.count()