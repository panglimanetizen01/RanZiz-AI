"""
RanZiz AI Runtime Builder
Version 1.4
"""


from source.agents.agent_manager import AgentManager
from source.core.bridge.runtime_core_bridge import RuntimeCoreBridge
from source.memory.gateway.memory_gateway import MemoryGateway
from source.planner.executor import Executor
from source.plugins.plugin_manager import PluginManager
from source.runtime.assembly.runtime_assembler import RuntimeAssembler
from source.runtime.capability.agent_runtime_capability import AgentRuntimeCapability
from source.runtime.capability.memory_runtime_capability import MemoryRuntimeCapability
from source.runtime.capability.plugin_runtime_capability import PluginRuntimeCapability
from source.runtime.capability.runtime_capability_dispatcher import (
    RuntimeCapabilityDispatcher,
)
from source.runtime.capability.runtime_capability_registry import (
    RuntimeCapabilityRegistry,
)
from source.runtime.capability.workflow_runtime_capability import (
    WorkflowRuntimeCapability,
)
from source.runtime.coordinator.runtime_coordinator import RuntimeCoordinator
from source.runtime.gateway.runtime_gateway import RuntimeGateway
from source.runtime.integration.runtime_integration_adapter import (
    RuntimeIntegrationAdapter,
)
from source.runtime.lifecycle.runtime_lifecycle import RuntimeLifecycle
from source.runtime.pipeline.capability_runtime_pipeline import CapabilityRuntimePipeline
from source.runtime.manager.runtime_manager import RuntimeManager
from source.runtime.registry.runtime_registry import RuntimeRegistry
from source.runtime.service.runtime_service import RuntimeService


class RuntimeBuilder:


    def build(self):

        manager = RuntimeManager()

        assembler = RuntimeAssembler()

        container = assembler.assemble()

        manager.register(
            container
        )

        service = RuntimeService(
            manager
        )

        lifecycle = RuntimeLifecycle(
            manager
        )

        registry = RuntimeRegistry()

        capability_registry = RuntimeCapabilityRegistry()

        memory_capability = MemoryRuntimeCapability(
            MemoryGateway()
        )

        plugin_capability = PluginRuntimeCapability(
            PluginManager()
        )

        workflow_capability = None

        agent_capability = AgentRuntimeCapability(
            AgentManager()
        )

        capability_registry.register(
            "memory",
            memory_capability
        )

        capability_registry.register(
            "plugin",
            plugin_capability
        )

        if workflow_capability is not None:

            capability_registry.register(
                "workflow",
                workflow_capability
            )

        capability_registry.register(
            "agent",
            agent_capability
        )

        capability_dispatcher = RuntimeCapabilityDispatcher(
            capability_registry
        )

        capability_pipeline = CapabilityRuntimePipeline()

        coordinator = RuntimeCoordinator(

            service,

            lifecycle,

            registry,

            capability_pipeline=capability_pipeline,

            capability_dispatcher=capability_dispatcher

        )

        adapter = RuntimeIntegrationAdapter(
            coordinator
        )

        gateway = RuntimeGateway(
            adapter
        )

        bridge = RuntimeCoreBridge(
            gateway
        )

        return bridge