"""
RanZiz AI Retry Executor
Version 1.0
"""

from source.runtime.retry.retry_policy import RetryPolicy


class RetryExecutor:

    def __init__(
        self,
        executor,
        policy=None
    ):

        self.executor = executor

        self.policy = policy or RetryPolicy()


    def execute(
        self,
        payload
    ):

        attempt = 0

        last_error = None


        while True:

            try:

                return self.executor.execute(
                    payload
                )

            except Exception as error:

                last_error = error

                attempt += 1

                if not self.policy.should_retry(
                    attempt
                ):

                    raise last_error


    def __repr__(self):

        return (
            f"RetryExecutor("
            f"{self.executor})"
        )
