"""
RanZiz AI Retry Test Capability
Version 1.1
"""


class RetryTestError(Exception):
    """Simulasi retry."""


class RetryTestCapability:

    def __init__(self):
        self.counter = 0

    def execute(self, payload):
        self.counter += 1

        if self.counter < 3:
            raise RetryTestError(f"Simulasi gagal percobaan {self.counter}")

        return "Berhasil pada percobaan ketiga"
