import os
import boto3
import json


def handler(event, context):
    client = boto3.client('lambda')
    print('event', event)
    response = client.invoke(
        InvocationType='Event',
        FunctionName=os.environ['FUNCTION_NAME'],
        Payload=json.dumps(event),
    )
    print('response', response)
    return None
