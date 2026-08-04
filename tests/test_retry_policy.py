"""
RanZiz AI Retry Policy Test
Version 1.0
"""

from source.runtime.retry.retry_policy import RetryPolicy


def test_retry_policy_limit():

    retry = RetryPolicy(3)

    assert retry.should_retry(0)

    assert retry.should_retry(1)

    assert retry.should_retry(2)

    assert not retry.should_retry(3)



def test_retry_remaining():

    retry = RetryPolicy(5)

    assert retry.remaining(0) == 5

    assert retry.remaining(2) == 3

    assert retry.remaining(5) == 0



def test_retry_custom_limit():

    retry = RetryPolicy(1)

    assert retry.should_retry(0)

    assert not retry.should_retry(1)
