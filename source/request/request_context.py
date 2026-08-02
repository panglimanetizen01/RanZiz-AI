"""
RanZiz AI Request Context
Version 2.1
"""

import uuid

from source.logging.trace_logger import TraceLogger


class RequestContext:


    MAX_KEY_LENGTH = 100

    MAX_VALUE_LENGTH = 5000


    def __init__(self):

        self.request_id = str(
            uuid.uuid4()
        )

        self.data = {}

        self.logger = TraceLogger()



    def get_id(self):

        return self.request_id



    def sanitize(self, value):

        if value is None:

            return None


        if isinstance(value, str):

            if len(value) > self.MAX_VALUE_LENGTH:

                return (
                    value[:self.MAX_VALUE_LENGTH - 14]
                    + "...[TRUNCATED]"
                )

            return value



        if isinstance(value, (int, float, bool)):

            return value



        if isinstance(value, dict):

            clean = {}

            for key, item in value.items():

                clean[str(key)[:self.MAX_KEY_LENGTH]] = (
                    self.sanitize(item)
                )

            return clean



        if isinstance(value, list):

            return [
                self.sanitize(item)
                for item in value[:100]
            ]



        return str(value)[:self.MAX_VALUE_LENGTH]



    def set(

        self,

        key,

        value

    ):

        safe_key = str(key)[
            :self.MAX_KEY_LENGTH
        ]

        self.data[safe_key] = (
            self.sanitize(value)
        )



    def get(

        self,

        key,

        default=None

    ):

        return self.data.get(
            key,
            default
        )



    def log(

        self,

        event,

        data=None

    ):

        return self.logger.log(

            self.request_id,

            event,

            self.sanitize(data)

        )



    def get_trace(self):

        return self.logger.get_logs(
            self.request_id
        )



    def to_dict(self):

        return {

            "request_id": self.request_id,

            "data": dict(
                self.data
            ),

            "trace": self.get_trace()

        }



    def __repr__(self):

        return (

            f"RequestContext("

            f"{self.request_id}"

            f")"

        )