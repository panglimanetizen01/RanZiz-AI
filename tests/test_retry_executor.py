"""
RanZiz AI Retry Executor Test
Version 1.0
"""

from source.runtime.retry.retry_executor import RetryExecutor
from source.runtime.retry.retry_policy import RetryPolicy


class FlakyExecutor:

    def __init__(self):

        self.attempts = 0


    def execute(
        self,
        payload
    ):

        self.attempts += 1

        if self.attempts < 3:

            raise Exception(
                "temporary failure"
            )

        return {
            "status": "SUCCESS"
        }



class FailedExecutor:

    def execute(
        self,
        payload
    ):

        raise Exception(
            "permanent failure"
        )



def test_retry_success_after_failure():

    executor = FlakyExecutor()

    retry = RetryExecutor(
        executor,
        RetryPolicy(3)
    )

    result = retry.execute({})

    assert result["status"] == "SUCCESS"

    assert executor.attempts == 3



def test_retry_failed_after_limit():

    retry = RetryExecutor(
        FailedExecutor(),
        RetryPolicy(2)
    )

    try:

        retry.execute({})

        assert False

    except Exception as error:

        assert str(error) == "permanent failure"
