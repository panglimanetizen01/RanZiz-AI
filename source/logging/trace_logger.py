"""
RanZiz AI Trace Logger
Version 2.0
"""

from datetime import UTC, datetime


class TraceLogger:

    def __init__(self):
        self.logs = {}

    def log(
        self,
        request_id,
        event,
        data=None
    ):

        if data is None:
            data = {}

        timestamp = datetime.now(UTC)

        entry = {
            "timestamp": timestamp.isoformat(),
            "timestamp_obj": timestamp,
            "request_id": request_id,
            "event": event,
            "data": data
        }

        self.logs.setdefault(
            request_id,
            []
        ).append(entry)

        return entry

    def get_logs(
        self,
        request_id
    ):

        logs = self.logs.get(
            request_id,
            []
        )

        if not logs:
            return []

        first = logs[0]["timestamp_obj"]

        result = []

        for item in logs:

            elapsed = (
                item["timestamp_obj"] - first
            ).total_seconds() * 1000

            result.append({
                "timestamp": item["timestamp"],
                "request_id": item["request_id"],
                "event": item["event"],
                "elapsed_ms": round(elapsed, 3),
                "data": item["data"]
            })

        return result