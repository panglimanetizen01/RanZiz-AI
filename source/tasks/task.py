"""
RanZiz AI Task
Version 1.0
"""


class Task:

    def __init__(
        self,
        name,
        capability="chat",
        payload=None
    ):

        self.name = name
        self.capability = capability
        self.payload = payload or {}

        self.status = "pending"

    def start(self):

        self.status = "running"

    def finish(self):

        self.status = "done"

    def fail(self):

        self.status = "failed"

    def info(self):

        return {
            "name": self.name,
            "capability": self.capability,
            "status": self.status,
            "payload": self.payload,
        }