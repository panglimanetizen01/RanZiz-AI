"""
RanZiz AI Workflow Engine
Version 5.1
"""

from source.capability.capability_executor import CapabilityExecutor
from source.capability.capability_loader import CapabilityLoader
from source.capability.capability_registry import CapabilityRegistry
from source.events.event import Event
from source.events.event_manager import EventManager
from source.events.trace_events import TraceEvents
from source.workflow.workflow_context import WorkflowContext


class WorkflowEngine:

    MAX_TASKS = 100

    def __init__(self, executor=None):

        self.executor = executor

        self.context = WorkflowContext()

        self.registry = CapabilityRegistry()

        self.events = EventManager()

        loader = CapabilityLoader()

        executors = loader.load()

        for name, capability in executors.items():

            self.registry.register(
                name,
                capability
            )

        self.capability_executor = CapabilityExecutor(
            self.registry
        )

    def validate_workflow(self, workflow):

        if workflow is None:
            return False

        if not hasattr(
            workflow,
            "name"
        ):
            return False

        return hasattr(
            workflow,
            "get_tasks"
        )

    def validate_task(self, task):

        if task is None:
            return False

        if not hasattr(
            task,
            "payload"
        ):
            return False

        return isinstance(
            task.payload,
            dict
        )

    def run(
        self,
        workflow,
        context=None
    ):

        if not self.validate_workflow(
            workflow
        ):

            raise TypeError(
                "Workflow tidak valid"
            )

        tasks = workflow.get_tasks()

        if len(tasks) > self.MAX_TASKS:

            raise ValueError(
                "Jumlah task melebihi batas workflow"
            )

        self.context.clear()

        request_id = None

        if context is not None:

            request_id = context.get_id()

            self.context.set(
                "request_id",
                request_id
            )

            context.log(
                TraceEvents.WORKFLOW_STARTED,
                {
                    "workflow": workflow.name
                }
            )

        self.events.publish(

            Event(

                "workflow.started",

                {
                    "workflow": workflow.name,
                    "request_id": request_id
                }

            )

        )

        results = []

        for task in tasks:

            if not self.validate_task(
                task
            ):

                raise TypeError(
                    "Task workflow tidak valid"
                )

            # ==================================================
            # Sinkronkan workflow context ke payload executor
            # ==================================================

            task.payload["context"] = self.context.all()

            task.payload["workflow_context"] = self.context

            task.payload["request_context"] = context

            result = self.capability_executor.execute(
                task
            )

            self.context.set(
                task.name,
                result.output
            )

            results.append(
                result.to_dict()
            )

        if context is not None:

            context.log(
                TraceEvents.WORKFLOW_FINISHED,
                {
                    "workflow": workflow.name
                }
            )

        self.events.publish(

            Event(

                "workflow.finished",

                {
                    "workflow": workflow.name,
                    "request_id": request_id
                }

            )

        )

        return {

            "workflow": workflow.name,

            "request_id": request_id,

            "context": self.context.all(),

            "results": results,

            "output": self._build_output(results)

        }


    def _build_output(
        self,
        results
    ):

        output = []

        for item in results:

            if not isinstance(
                item,
                dict
            ):
                continue

            capability = item.get(
                "capability",
                ""
            )

            data = item.get(
                "output",
                ""
            )

            output.append(
                f"{capability}\n\n{data}"
            )


        return "\n\n".join(
            output
        )
