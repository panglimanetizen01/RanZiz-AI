"""
RanZiz AI HTML Report
Version 1.0
"""

from pathlib import Path
from datetime import datetime


class HTMLReport:

    def build(self, data, directory="logs"):

        Path(directory).mkdir(
            parents=True,
            exist_ok=True
        )

        filename = datetime.now().strftime(
            "report_%Y%m%d_%H%M%S.html"
        )

        filepath = Path(directory) / filename

        summary = data["summary"]
        health = data["health"]
        diagnosis = data["diagnosis"]

        html = f"""
<!DOCTYPE html>
<html>
<head>
<meta charset="utf-8">
<title>RanZiz AI Report</title>
<style>
body {{
    font-family: Arial;
    margin: 30px;
}}
table {{
    border-collapse: collapse;
    width: 100%;
}}
td, th {{
    border: 1px solid #ccc;
    padding: 8px;
}}
pre {{
    background: #f4f4f4;
    padding: 10px;
    overflow: auto;
}}
</style>
</head>

<body>

<h1>RanZiz AI Diagnostic Report</h1>

<table>
<tr><th>Request</th><td>{summary["request_id"]}</td></tr>
<tr><th>Status</th><td>{summary["status"]}</td></tr>
<tr><th>Health</th><td>{health["status"]}</td></tr>
<tr><th>Diagnosis</th><td>{diagnosis["status"]}</td></tr>
<tr><th>Total Events</th><td>{summary["total_events"]}</td></tr>
<tr><th>Total Errors</th><td>{summary["total_errors"]}</td></tr>
</table>

<h2>Timeline</h2>

<pre>
{data["timeline"]}
</pre>

</body>
</html>
"""

        filepath.write_text(
            html,
            encoding="utf-8"
        )

        return str(filepath)
