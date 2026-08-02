"""
RanZiz AI Trace Events
Version 1.3
"""


class TraceEvents:

    # Request Lifecycle
    REQUEST_CREATED = "request.created"
    RESPONSE_CREATED = "response.created"


    # Brain
    BRAIN_STARTED = "brain.started"


    # Session
    SESSION_CREATED = "session.created"


    # Command & Plugin
    COMMAND_CHECKED = "command.checked"
    PLUGIN_CHECKED = "plugin.checked"


    # Agent
    AGENT_SELECTED = "agent.selected"


    # Decision
    DECISION_CREATED = "decision.created"


    # Workflow
    WORKFLOW_SELECTED = "workflow.selected"
    WORKFLOW_STARTED = "workflow.started"
    WORKFLOW_FINISHED = "workflow.finished"


    # Capability
    CAPABILITY_STARTED = "capability.started"
    CAPABILITY_FINISHED = "capability.finished"


    # Error
    ERROR_OCCURRED = "error.occurred"


    # Recovery
    RECOVERY_STARTED = "recovery.started"
    RECOVERY_FINISHED = "recovery.finished"