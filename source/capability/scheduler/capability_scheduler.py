"""
RanZiz AI Capability Scheduler
Version 1.0
"""


class CapabilityScheduler:

    def ready(self, plan):

        ready = []

        for item in plan:

            if item["status"] != "PENDING":
                continue

            dependencies = item.get(
                "dependencies",
                []
            )

            blocked = False

            for dependency in dependencies:

                target = plan.get(
                    dependency
                )

                if target is None:

                    blocked = True
                    break

                if target["status"] != "SUCCESS":

                    blocked = True
                    break

            if not blocked:

                ready.append(
                    item
                )

        return ready

    def finished(self, plan):

        return len(
            plan.completed()
        ) == len(plan)

    def failed(self, plan):

        return len(
            plan.failed()
        ) > 0

    def __repr__(self):

        return "CapabilityScheduler(v1)"
