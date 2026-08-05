"""
RanZiz AI Web Interface
Version 0.2
"""

from flask import Flask, render_template, request, jsonify

import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent

if str(ROOT) not in sys.path:
    sys.path.insert(0, str(ROOT))


from source.runtime.composition.runtime_composition_root import (
    RuntimeCompositionRoot
)


app = Flask(__name__)


runtime = RuntimeCompositionRoot().get_runtime()


@app.route("/")
def index():
    return render_template(
        "index.html"
    )


@app.route("/chat", methods=["POST"])
def chat():

    data = request.json or {}

    message = data.get(
        "message",
        ""
    )

    result = runtime.chat(
        message
    )

    if isinstance(result, dict):

        response = (
            result.get("message")
            or result.get("response")
            or str(result)
        )

    else:
        response = str(result)


    return jsonify(
        {
            "response": response
        }
    )


if __name__ == "__main__":

    app.run(
        host="0.0.0.0",
        port=5000,
        debug=True
    )
