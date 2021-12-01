import boto3
import json

lambda_client = boto3.client('lambda',
                      # keys for user with IAM permissions on lambda
                      aws_access_key_id='iam_key',
                      aws_secret_access_key='iam_secret_key',
                      region_name='selected_region')

test_event = dict()

response = lambda_client.invoke(
  FunctionName='getUserData', # function defined
  Payload=json.dumps(test_event),
)

print(response['Payload'])
print(response['Payload'].read().decode("utf-8"))
