"""
RanZiz AI Trace Storage
Version 1.0
"""


class TraceStorage:


    def __init__(self):

        self.storage = {}


    def save(

        self,

        request_id,

        trace

    ):

        self.storage[request_id] = list(trace)


    def get(

        self,

        request_id

    ):

        return self.storage.get(
            request_id
        )


    def delete(

        self,

        request_id

    ):

        self.storage.pop(
            request_id,
            None
        )


    def last(

        self,

        limit=10

    ):

        keys = list(
            self.storage.keys()
        )

        keys = keys[-limit:]

        return {

            key: self.storage[key]

            for key in keys

        }


    def count(self):

        return len(
            self.storage
        )


    def clear(self):

        self.storage.clear()