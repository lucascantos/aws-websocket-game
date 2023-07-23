import json
import logging


def hello(event, context):
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

def connection(event, context):
    logging.warning(event)
    body = {
        "message": "Go Serverless v2.0! Your function executed successfully!",
        "input": event,
    }
    return {"statusCode": 200, "body": json.dumps(body)}

def input_receiver(e)