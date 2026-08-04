"""
RanZiz AI API
Version 1.0
"""

from fastapi import FastAPI
from pydantic import BaseModel

from source.core.brain import Brain


app = FastAPI(
    title="RanZiz AI",
    version="1.0"
)


brain = Brain()


class ChatRequest(BaseModel):
    message: str


@app.get("/")
def index():

    return {
        "name": "RanZiz AI",
        "status": "running"
    }


@app.post("/chat")
def chat(request: ChatRequest):

    result = brain.process(
        request.message
    )

    return {
        "response": result
    }
