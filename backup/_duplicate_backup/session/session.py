from typing import ClassVar

"""
RanZiz AI Session
Version 2.0
"""

import uuid
from datetime import UTC, datetime


class Session:


    MAX_HISTORY = 200

    MAX_CONTENT = 5000

    ALLOWED_ROLES: ClassVar = {

        "user",

        "assistant",

        "system"

    }


    def __init__(self, session_id=None):

        self.id = session_id or str(
            uuid.uuid4()
        )

        self.created_at = (
            datetime.now(UTC).isoformat()
        )

        self.updated_at = (
            self.created_at
        )

        self.context = {}

        self.history = []



    def sanitize(

        self,

        value

    ):

        if isinstance(value, str):

            return value[:self.MAX_CONTENT]


        if isinstance(value, (dict, list)):

            return value


        return str(value)[:self.MAX_CONTENT]



    def add_message(

        self,

        role,

        content

    ):


        if role not in self.ALLOWED_ROLES:

            raise ValueError(
                "Role session tidak valid"
            )


        if len(self.history) >= self.MAX_HISTORY:

            self.history.pop(0)



        self.history.append(

            {

                "role": role,

                "content": self.sanitize(
                    content
                ),

                "time": datetime.now(UTC).isoformat()

            }

        )


        self.updated_at = (
            datetime.now(UTC).isoformat()
        )



    def set(

        self,

        key,

        value

    ):

        self.context[str(key)[:100]] = (
            self.sanitize(value)
        )


        self.updated_at = (
            datetime.now(UTC).isoformat()
        )



    def get(

        self,

        key,

        default=None

    ):

        return self.context.get(

            key,

            default

        )



    def to_dict(self):

        return {

            "id": self.id,

            "created_at": self.created_at,

            "updated_at": self.updated_at,

            "context": self.context,

            "history": self.history

        }



    def __repr__(self):

        return (

            f"Session({self.id})"

        )