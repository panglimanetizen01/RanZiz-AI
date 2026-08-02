"""
RanZiz AI Brain
Version 9.0
"""

from source.agents.agent_manager import AgentManager
from source.commands.commands import Commands
from source.commands.handlers.command_handler import CommandHandler
from source.config.config import Config
from source.context.context_gateway import ContextGateway
from source.core.runtime.core_runtime_adapter import CoreRuntimeAdapter
from source.core.runtime.runtime_handler import RuntimeHandler
from source.decision.decision_engine import DecisionEngine
from source.decision.goal_analyzer import GoalAnalyzer
from source.decision.intent_analyzer import IntentAnalyzer
from source.events.trace_events import TraceEvents
from source.execution.handlers.execution_handler import ExecutionHandler
from source.memory.episode.episode_recorder import EpisodeRecorder
from source.memory.gateway.memory_gateway import MemoryGateway
from source.memory.handlers.memory_handler import MemoryHandler
from source.planner.executor import Executor
from source.planner.task_planner import TaskPlanner
from source.plugins.handlers.plugin_handler import PluginHandler
from source.plugins.plugin_manager import PluginManager
from source.request.request_context import RequestContext
from source.response.pipeline.pipeline_manager import PipelineManager
from source.session.session_manager import SessionManager
from source.workflow.handlers.router_handler import RouterHandler
from source.workflow.workflow_orchestrator import WorkflowOrchestrator
from source.workflow.workflow_router import WorkflowRouter


class Brain:

    def __init__(self):
        self.name = Config.APP_NAME
        self.version = Config.VERSION

        self.commands = Commands()

        self.command_handler = CommandHandler(
            self.commands
        )

        self.plugins = PluginManager()

        self.plugin_handler = PluginHandler(
            self.plugins
        )

        self.agents = AgentManager()

        self.planner = TaskPlanner()
        self.executor = Executor()

        self.sessions = SessionManager()
        self.pipeline = PipelineManager()

        self.memory = MemoryGateway()
        self.episode = EpisodeRecorder()

        self.memory_handler = MemoryHandler(
            self.memory,
            self.episode
        )

        self.context = ContextGateway()

        self.intent = IntentAnalyzer()
        self.goal = GoalAnalyzer()
        self.decision = DecisionEngine()

        self.runtime = CoreRuntimeAdapter()

        self.runtime_handler = RuntimeHandler(
            self.runtime
        )

        self.execution_handler = ExecutionHandler(
            self.planner,
            self.executor,
            self.runtime_handler
        )

        self.workflow = WorkflowOrchestrator(
            self.executor
        )

        self.router = WorkflowRouter(
            self.workflow,
            self.agents
        )

        self.router_handler = RouterHandler(
            self.router
        )

        self.load_plugins()


    def load_plugins(self):
        if hasattr(
            self.plugins,
            "load_plugins"
        ):
            self.plugins.load_plugins()


    def startup(self):
        return (
            f"{self.name} "
            f"v{self.version} siap digunakan."
        )


    def build_response(
        self,
        session,
        context,
        response
    ):
        return self.pipeline.process(
            session.id,
            context,
            response
        )


    def runtime_fallback(
        self,
        result,
        message,
        ai_decision
    ):
        if result is not None:
            return result

        return self.runtime_handler.handle(
            message,
            ai_decision
        )






    def process(
        self,
        message,
        session_id=None
    ):
        context = RequestContext()

        context.log(
            TraceEvents.REQUEST_CREATED,
            {
                "module": "Brain"
            }
        )

        session = self.sessions.get_or_create(
            session_id
        )

        session.add_message(
            "user",
            message
        )

        if not message.strip():
            return self.build_response(
                session,
                context,
                "Silakan tulis sesuatu."
            )


        active_context = self.context.analyze(
            message
        )

        context.set(
            "active_context",
            active_context
        )


        intent = self.intent.analyze(
            message
        )

        goal = self.goal.analyze(
            message
        )

        ai_decision = self.decision.decide(
            intent,
            goal,
            context
        )


        learned = self.memory_handler.learn(
            message,
            ai_decision,
            context
        )

        if learned is not None:

            session.add_message(
                "assistant",
                learned
            )

            return self.build_response(
                session,
                context,
                learned
            )


        memory_result = self.memory_handler.fallback(
            message,
            session,
            context,
            self.build_response
        )

        if memory_result is not None:
            return memory_result


        retrieved_result = self.memory_handler.retrieve(
            message,
            ai_decision,
            session,
            context,
            self.build_response
        )

        if retrieved_result is not None:
            return retrieved_result


        command_result = self.command_handler.handle(
            message,
            session,
            context,
            self.build_response
        )

        if command_result is not None:
            return command_result


        plugin_result = self.plugin_handler.handle(
            message,
            session,
            context,
            self.build_response
        )

        if plugin_result is not None:
            return plugin_result



        router_result = self.router_handler.handle(
            message,
            session,
            context,
            self.build_response
        )


        if router_result is not None:
            return router_result


        result = self.execution_handler.execute(
            message,
            self.context.all(),
            ai_decision
        )

        session.add_message(
            "assistant",
            str(result)
        )

        return self.build_response(
            session,
            context,
            result
        )