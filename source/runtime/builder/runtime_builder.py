"""
RanZiz AI Runtime Builder
Version 1.5
"""

from source.runtime.assembly.runtime_assembler import RuntimeAssembler
from source.runtime.factory.runtime_factory import RuntimeFactory

from source.runtime.manager.runtime_manager import RuntimeManager
from source.runtime.service.runtime_service import RuntimeService
from source.runtime.lifecycle.runtime_lifecycle import RuntimeLifecycle
from source.runtime.registry.runtime_registry import RuntimeRegistry

from source.runtime.pipeline.context_pipeline import ContextPipeline
from source.runtime.pipeline.decision_pipeline import DecisionPipeline
from source.runtime.pipeline.memory_pipeline import MemoryPipeline
from source.runtime.pipeline.capability_runtime_pipeline import CapabilityRuntimePipeline

from source.context.context_gateway import ContextGateway
from source.decision.intent_analyzer import IntentAnalyzer
from source.decision.goal_analyzer import GoalAnalyzer
from source.decision.decision_engine import DecisionEngine
from source.memory.gateway.memory_gateway import MemoryGateway
from source.memory.episode.episode_recorder import EpisodeRecorder

from source.runtime.capability.runtime_capability_registry import RuntimeCapabilityRegistry
from source.runtime.capability.runtime_capability_dispatcher import RuntimeCapabilityDispatcher
from source.runtime.capability.memory_runtime_capability import MemoryRuntimeCapability
from source.runtime.capability.plugin_runtime_capability import PluginRuntimeCapability
from source.runtime.capability.agent_runtime_capability import AgentRuntimeCapability

from source.plugins.plugin_manager import PluginManager
from source.agents.agent_manager import AgentManager

from source.runtime.coordinator.runtime_coordinator import RuntimeCoordinator
from source.runtime.integration.runtime_integration_adapter import RuntimeIntegrationAdapter
from source.runtime.gateway.runtime_gateway import RuntimeGateway
from source.core.bridge.runtime_core_bridge import RuntimeCoreBridge

from source.runtime.capability.agent_runtime_capability import AgentRuntimeCapability


class RuntimeBuilder:

    def build(self):

        context_pipeline = ContextPipeline(
            ContextGateway()
        )

        decision_pipeline = DecisionPipeline(
            IntentAnalyzer(),
            GoalAnalyzer(),
            DecisionEngine()
        )

        memory_gateway = MemoryGateway()

        memory_pipeline = MemoryPipeline(
            memory_gateway,
            EpisodeRecorder()
        )

        capability_pipeline = CapabilityRuntimePipeline()

        brain_runtime = RuntimeFactory.create(
            context_pipeline,
            decision_pipeline,
            memory_pipeline,
            capability_pipeline
        )

        manager = RuntimeManager()

        container = RuntimeAssembler().assemble(
            brain_runtime=brain_runtime
        )

        manager.register(container)

        service = RuntimeService(manager)

        lifecycle = RuntimeLifecycle(manager)

        registry = RuntimeRegistry()

        capability_registry = RuntimeCapabilityRegistry()

        capability_registry.register(
            "memory",
            MemoryRuntimeCapability(memory_gateway)
        )

        capability_registry.register(
            "plugin",
            PluginRuntimeCapability(
                PluginManager()
            )
        )

        capability_registry.register(
            "agent",
            AgentRuntimeCapability(
                AgentManager()
            )
        )

        dispatcher = RuntimeCapabilityDispatcher(
            capability_registry
        )

        coordinator = RuntimeCoordinator(
            service,
            lifecycle,
            registry,
            capability_pipeline=capability_pipeline,
            capability_dispatcher=dispatcher
        )

        adapter = RuntimeIntegrationAdapter(
            coordinator
        )

        container.set_runtime_adapter(
            adapter
        )

        return RuntimeCoreBridge(
            RuntimeGateway(adapter)
        )

    def build_gateway(self):

        return self.build()
