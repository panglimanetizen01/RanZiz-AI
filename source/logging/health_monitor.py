"""
RanZiz AI Health Monitor
Version 2.0
"""


class HealthMonitor:


    RETRY_WARNING_LIMIT = 3


    def check(self, trace):

        warnings = []

        events = [
            item.get("event")
            for item in trace
        ]


        if "request.created" not in events:

            warnings.append(
                "Request tidak pernah dibuat."
            )


        if (
            "workflow.started" in events
            and
            "workflow.finished" not in events
        ):

            warnings.append(
                "Workflow dimulai tetapi tidak selesai."
            )


        started = [
            item.get("data", {}).get("capability")
            for item in trace
            if item.get("event") == "capability.started"
        ]


        finished = [
            item.get("data", {}).get("capability")
            for item in trace
            if item.get("event") == "capability.finished"
        ]


        for capability in started:

            if capability not in finished:

                warnings.append(
                    f"Capability '{capability}' belum selesai."
                )


        retry_count = len(
            [
                item
                for item in trace
                if item.get("event") == "retry.attempt"
            ]
        )


        retry_map = {}

        for item in trace:

            if item.get("event") == "retry.attempt":

                capability = item.get(
                    "data",
                    {}
                ).get(
                    "capability",
                    "unknown"
                )

                retry_map[capability] = (
                    retry_map.get(capability, 0) + 1
                )


        for capability, count in retry_map.items():

            if count > self.RETRY_WARNING_LIMIT:

                warnings.append(
                    f"Retry terlalu banyak pada {capability}: {count} kali."
                )


        if any(
            "error" in warning.lower()
            for warning in warnings
        ):

            status = "FAILED"

        elif warnings:

            status = "DEGRADED"

        else:

            status = "HEALTHY"


        return {

            "healthy": status == "HEALTHY",

            "status": status,

            "retry_count": retry_count,

            "warnings": warnings

        }
