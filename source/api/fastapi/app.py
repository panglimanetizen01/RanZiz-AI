"""
RanZiz AI FastAPI Application
Version 1.0
"""

from fastapi import FastAPI

from source.api.server.http_server import HTTPServer

app = FastAPI(

    title="RanZiz AI",

    version="1.0"

)


server = HTTPServer()


@app.get("/")

def index():

    return {

        "service": "RanZiz AI",

        "status": "RUNNING"

    }


@app.get("/health")

def health():

    return server.health()


@app.post("/chat")

def chat(

    payload: dict

):

    return server.chat(

        payload

    )