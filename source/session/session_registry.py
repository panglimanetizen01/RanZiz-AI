"""
RanZiz AI Session Registry
Version 1.0
"""

from source.session.session import Session


class SessionRegistry:


    def __init__(self):

        self.sessions = {}


    def create(self):

        session = Session()

        self.sessions[
            session.id
        ] = session

        return session


    def get(

        self,

        session_id

    ):

        return self.sessions.get(
            session_id
        )


    def remove(

        self,

        session_id

    ):

        return self.sessions.pop(
            session_id,
            None
        )


    def exists(

        self,

        session_id

    ):

        return (
            session_id
            in self.sessions
        )


    def list(self):

        return list(
            self.sessions.keys()
        )


    def count(self):

        return len(
            self.sessions
        )


    def clear(self):

        self.sessions.clear()