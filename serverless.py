import json


def main(event, context):
    body = {
        "message": "Go Serverless v4.0! Your function executed successfully!",
    }

    return {"statusCode": 200, "body": json.dumps(body)}


def test(event, context):
    body = {
        "message": "test serverless",
    }

    return {"statusCode": 200, "body": json.dumps(body)}
