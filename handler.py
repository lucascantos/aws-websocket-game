"""Handle all communications with the client."""
import json
import logging
from typing import Any


def hello(event: dict, context: dict) -> dict[str, Any]:
    """Handle the hello world event."""
    logging.error("heck")
    body = {
        "message": "Go Serverless v2.0! Your function executed successfully!",
        "input": event,
    }

    response = {"statusCode": 200, "body": json.dumps(body)}

    return response

    # Use this code if you don't use the http event with the LAMBDA-PROXY
    # integration
    """
    return {
        "message": "Go Serverless v1.0! Your function executed successfully!",
        "event": event
    }
    """


def connection(event: dict, context: dict) -> dict[str, Any]:
    """Handle the connection with the client."""
    logging.warning(event)
    body = {
        "message": "Go Serverless v2.0! Your function executed successfully!",
        "input": event,
    }
    return {"statusCode": 200, "body": json.dumps(body)}


def client_input(event: dict, context: dict) -> None:
    """Handle the input from the client."""
    pass


def world_state(event: dict, context: dict) -> None:
    """Handle the world state from the server."""
    pass
