"""
RanZiz AI Trace Exporter
Version 1.0
"""

import json
from pathlib import Path
from datetime import datetime


class TraceExporter:

    def export(self, data, directory="logs"):

        Path(directory).mkdir(
            parents=True,
            exist_ok=True
        )

        filename = datetime.now().strftime(
            "trace_%Y%m%d_%H%M%S.json"
        )

        filepath = Path(directory) / filename

        with open(
            filepath,
            "w",
            encoding="utf-8"
        ) as f:
            json.dump(
                data,
                f,
                indent=2,
                ensure_ascii=False
            )

        return str(filepath)
