"""
RanZiz AI Bootstrap
Version 1.0
"""

from source.agents.agent_manager import AgentManager
from source.commands.commands import Commands
from source.context.context_gateway import ContextGateway
from source.core.service_container import ServiceContainer
from source.decision.decision_engine import DecisionEngine
from source.decision.goal_analyzer import GoalAnalyzer
from source.decision.intent_analyzer import IntentAnalyzer
from source.memory.episode.episode_recorder import EpisodeRecorder
from source.memory.gateway.memory_gateway import MemoryGateway
from source.planner.executor import Executor
from source.planner.task_planner import TaskPlanner
from source.plugins.plugin_manager import PluginManager
from source.response.pipeline.pipeline_manager import PipelineManager
from source.session.session_manager import SessionManager


class Bootstrap:


    def build(self):

        container = ServiceContainer()

        container.register(
            "commands",
            Commands()
        )

        container.register(
            "plugins",
            PluginManager()
        )

        container.register(
            "agents",
            AgentManager()
        )

        container.register(
            "planner",
            TaskPlanner()
        )

        container.register(
            "executor",
            Executor()
        )

        container.register(
            "sessions",
            SessionManager()
        )

        container.register(
            "pipeline",
            PipelineManager()
        )

        container.register(
            "memory",
            MemoryGateway()
        )

        container.register(
            "episode",
            EpisodeRecorder()
        )

        container.register(
            "context",
            ContextGateway()
        )

        container.register(
            "intent",
            IntentAnalyzer()
        )

        container.register(
            "goal",
            GoalAnalyzer()
        )

        container.register(
            "decision",
            DecisionEngine()
        )

        return container