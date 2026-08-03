"""
RanZiz AI Trace Diff
Version 1.0
"""

import json


class TraceDiff:

    def load(self, filepath):
        with open(filepath, "r", encoding="utf-8") as f:
            return json.load(f)

    def compare(self, old_file, new_file):
        old = self.load(old_file)
        new = self.load(new_file)

        old_summary = old.get("summary", {})
        new_summary = new.get("summary", {})

        old_metrics = old_summary.get("metrics", {})
        new_metrics = new_summary.get("metrics", {})

        old_duration = old_metrics.get("capability_duration", {})
        new_duration = new_metrics.get("capability_duration", {})

        report = {
            "status_before": old_summary.get("status"),
            "status_after": new_summary.get("status"),
            "events_before": old_summary.get("total_events"),
            "events_after": new_summary.get("total_events"),
            "duration_changes": {}
        }

        capabilities = (
            set(old_duration.keys()) |
            set(new_duration.keys())
        )

        for capability in sorted(capabilities):
            report["duration_changes"][capability] = {
                "before": old_duration.get(capability),
                "after": new_duration.get(capability)
            }

        total = 0.0

        for item in report["duration_changes"].values():
            before = item["before"]
            after = item["after"]

            if before is None or after is None:
                continue

            total += after - before

        if total < 0:
            report["verdict"] = "IMPROVED"
        elif total > 0:
            report["verdict"] = "REGRESSION"
        else:
            report["verdict"] = "UNCHANGED"

        return report
