"""
RanZiz AI Doctor
Version 1.2
"""

from pathlib import Path
import sys
import importlib


# ==========================================================
# Tambahkan root project ke sys.path
# ==========================================================

PROJECT_ROOT = Path(__file__).resolve().parent.parent

if str(PROJECT_ROOT) not in sys.path:
    sys.path.insert(0, str(PROJECT_ROOT))


CHECKS = [
    (
        "Agent Manager",
        "source.agents.agent_manager",
        "AgentManager",
    ),
    (
        "Workflow Planner",
        "source.workflow.workflow_planner",
        "WorkflowPlanner",
    ),
    (
        "Workflow Router",
        "source.workflow.workflow_router",
        "WorkflowRouter",
    ),
    (
        "Workflow Orchestrator",
        "source.workflow.workflow_orchestrator",
        "WorkflowOrchestrator",
    ),
    (
        "Capability Manager",
        "source.planner.capability_manager",
        "CapabilityManager",
    ),
    (
        "Catalog Service",
        "source.capability.catalog.catalog_service",
        "CatalogService",
    ),
]


passed = 0
failed = 0


print("=" * 40)
print("RanZiz AI Doctor v1.2")
print("=" * 40)
print(f"Project Root : {PROJECT_ROOT}")
print(f"Python Path  : {sys.path[0]}")
print()


# ==========================================================
# Import Check
# ==========================================================

for name, module_name, class_name in CHECKS:

    try:

        module = importlib.import_module(module_name)

        getattr(module, class_name)

        print(f"[PASS] {name}")

        passed += 1

    except Exception as e:

        print(f"[FAIL] {name}")
        print(f"       {e}")

        failed += 1


print()


# ==========================================================
# Agent Check
# ==========================================================

try:

    from source.agents.agent_manager import AgentManager

    manager = AgentManager()

    agents = manager.list()

    print(f"[INFO] Agents ({len(agents)})")

    for agent in agents:
        print(f"   - {agent}")

except Exception as e:

    print("[FAIL] Agent List")
    print(e)


print()


# ==========================================================
# Capability Check
# ==========================================================

try:

    from source.capability.catalog.catalog_service import CatalogService

    catalog = CatalogService()

    capabilities = catalog.list()

    print(f"[INFO] Capabilities ({len(capabilities)})")

    for item in capabilities:

        print(
            f"   - {item['name']} ({item['category']})"
        )

except Exception as e:

    print("[FAIL] Capability List")
    print(e)


print()


# ==========================================================
# Planner Test
# ==========================================================

print("=" * 40)
print("Planner Test")
print("=" * 40)

try:

    from source.workflow.workflow_planner import WorkflowPlanner

    planner = WorkflowPlanner()

    tests = [

        "buat website sederhana",

        "buat lagu dangdut",

        "riset sejarah islam",

        "buat logo ranziz ai",

        "jelaskan python",

    ]

    for text in tests:

        plan = planner.get_plan(text)

        print()

        print(f"Input        : {text}")

        print(f"Intent       : {plan['intent']}")

        print(f"Goal         : {plan['goal']}")

        print(f"Capabilities : {plan['capabilities']}")

        if not plan["capabilities"]:

            print("WARNING : Capability kosong")


except Exception as e:

    print("[FAIL] Planner Test")

    print(e)


print()
print("=" * 40)
print(f"PASS : {passed}")
print(f"FAIL : {failed}")
print("=" * 40)