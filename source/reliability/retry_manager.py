"""
RanZiz AI Retry Manager
Version 1.1
"""


import time


class RetryManager:



    def __init__(

        self,

        max_retry=3,

        delay=0.1,

        callback=None

    ):

        self.max_retry = max_retry

        self.delay = delay

        self.callback = callback



    def emit(

        self,

        event,

        data

    ):

        if self.callback is not None:

            self.callback(

                event,

                data

            )



    def execute(

        self,

        function,

        *args,

        **kwargs

    ):

        attempts = 0

        last_error = None



        while attempts < self.max_retry:


            attempts += 1


            self.emit(

                "retry.attempt",

                {
                    "attempt": attempts
                }

            )


            try:


                result = function(

                    *args,

                    **kwargs

                )


                self.emit(

                    "retry.finished",

                    {
                        "attempts": attempts,
                        "status": "SUCCESS"
                    }

                )


                return {


                    "status": "SUCCESS",

                    "attempts": attempts,

                    "result": result

                }



            except Exception as error:  # noqa: BLE001
                # Retry manager intentionally catches all operation failures
                # so it can retry the operation instead of terminating early.
                last_error = error


                self.emit(

                    "retry.failed",

                    {
                        "attempt": attempts,
                        "error": str(error)
                    }

                )



                if attempts < self.max_retry:

                    time.sleep(

                        self.delay

                    )



        self.emit(

            "retry.finished",

            {
                "attempts": attempts,
                "status": "FAILED"
            }

        )



        return {


            "status": "FAILED",

            "attempts": attempts,

            "error": str(last_error)

        }