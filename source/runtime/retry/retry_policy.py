"""
RanZiz AI Retry Policy
Version 1.0
"""


class RetryPolicy:

    def __init__(
        self,
        max_attempts=3
    ):

        self.max_attempts = max_attempts


    def should_retry(
        self,
        attempt
    ):

        return attempt < self.max_attempts


    def remaining(
        self,
        attempt
    ):

        remaining = (
            self.max_attempts - attempt
        )

        if remaining < 0:
            return 0

        return remaining


    def __repr__(self):

        return (
            f"RetryPolicy("
            f"max_attempts={self.max_attempts})"
        )
