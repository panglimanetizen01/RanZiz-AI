"""
RanZiz AI Capability Executor
Version 3.0
"""

from source.capability.result.capability_result import CapabilityResult
from source.events.event import Event
from source.events.event_manager import EventManager
from source.events.trace_events import TraceEvents
from source.recovery.recovery_manager import RecoveryManager
from source.reliability.retry_manager import RetryManager
from source.tasks.task import Task


class CapabilityExecutor:


    def __init__(self, registry):

        self.registry = registry

        self.events = EventManager()

        self.recovery = RecoveryManager()



    def retry_callback(self, request_context):

        def callback(event, data):

            if request_context is not None:

                request_context.log(
                    event,
                    data
                )


        return callback



    def validate_executor(self, executor):

        if executor is None:
            return False


        if not hasattr(
            executor,
            "execute"
        ):
            return False


        return hasattr(
            executor,
            "metadata"
        )



    def execute(self, task):


        if not isinstance(
            task,
            Task
        ):

            raise TypeError(
                "task harus berupa Task"
            )


        executor = self.registry.get(
            task.capability
        )


        request_context = task.payload.get(
            "request_context"
        )


        workflow_context = task.payload.get(
            "workflow_context"
        )


        if not self.validate_executor(
            executor
        ):


            if request_context:

                request_context.log(
                    TraceEvents.ERROR_OCCURRED,
                    {
                        "module": "CapabilityExecutor",
                        "error": "Executor tidak valid",
                        "capability": task.capability
                    }
                )


            return CapabilityResult(
                task.capability,
                status="FAILED",
                output="Executor tidak valid"
            )



        if not isinstance(
            task.payload,
            dict
        ):

            return CapabilityResult(
                task.capability,
                status="FAILED",
                output="Payload harus dictionary"
            )



        if request_context:

            request_context.log(

                TraceEvents.CAPABILITY_STARTED,

                {
                    "capability": task.capability,
                    "executor": executor.__class__.__name__
                }

            )


        self.events.publish(

            Event(

                "capability.started",

                {
                    "capability": task.capability
                }

            )

        )


        task.start()


        retry = RetryManager(

            callback=self.retry_callback(
                request_context
            )

        )


        execution = retry.execute(

            executor.execute,

            task.payload,

            capability=task.capability

        )


        if execution["status"] == "SUCCESS":


            task.finish()


            if request_context:

                request_context.log(
                    TraceEvents.CAPABILITY_FINISHED,
                    {
                        "capability": task.capability
                    }
                )


            result = CapabilityResult(

                task.capability,

                output=execution["result"]

            )


            if workflow_context:

                workflow_context.set(
                    task.capability,
                    result
                )


            return result



        task.fail()


        error = execution["error"]


        recovery = self.recovery.recover(

            task.capability,

            error

        )


        return CapabilityResult(

            task.capability,

            status="FAILED",

            output=recovery

        )
