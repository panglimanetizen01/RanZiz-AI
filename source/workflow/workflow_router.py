"""
RanZiz AI Workflow Router
Version 2.5
"""

from source.events.trace_events import TraceEvents


class WorkflowRouter:


    def __init__(
        self,
        orchestrator,
        agent_manager
    ):

        self.orchestrator = orchestrator

        self.agent_manager = agent_manager



    def execute(
        self,
        message,
        context=None
    ):


        # ==================================================
        # PRIORITY 1
        # Decision Engine Selected Agent
        # ==================================================

        if context is not None:

            decision = context.get(
                "decision"
            )


            if decision is not None:


                agent_name = None


                if hasattr(
                    decision,
                    "agent"
                ):

                    agent_name = decision.agent


                elif isinstance(
                    decision,
                    dict
                ):

                    agent_name = decision.get(
                        "agent"
                    )



                if agent_name:


                    agent = self.agent_manager.get(
                        agent_name
                    )


                    if agent:


                        try:

                            result = agent.execute(
                                message,
                                context
                            )


                        except TypeError:

                            result = agent.execute(
                                message
                            )



                        context.log(

                            TraceEvents.WORKFLOW_SELECTED,

                            {
                                "workflow": "Decision Agent",

                                "agent": agent_name,

                                "source": "decision"
                            }

                        )


                        return result



        # ==================================================
        # PRIORITY 2
        # Existing Agent Router
        # ==================================================

        result = self.agent_manager.execute(
            message,
            context
        )


        if result is not None:


            if context is not None:


                workflow_name = None


                if isinstance(
                    result,
                    dict
                ):

                    workflow_name = result.get(
                        "workflow"
                    )


                context.log(

                    TraceEvents.WORKFLOW_SELECTED,

                    {
                        "workflow": workflow_name,

                        "source": "agent"
                    }

                )


            return result



        # ==================================================
        # PRIORITY 3
        # Orchestrator
        # ==================================================

        if context is not None:

            context.log(

                TraceEvents.WORKFLOW_SELECTED,

                {
                    "workflow": "Auto Workflow",

                    "source": "orchestrator"
                }

            )


        return self.orchestrator.run(
            message,
            context
        )