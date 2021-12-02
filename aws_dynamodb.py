import boto3 # sdk

client = boto3.client('dynamodb',
                      # keys for user with IAM permissions on dynamodb
                      aws_access_key_id='iam_key',
                      aws_secret_access_key='iam_secret_key',
                      region_name='selected_region')

dynamodb = boto3.resource('dynamodb')
table = dynamodb.Table('Users')
print(table.item_count)

# GetItem
response = table.get_item(
    Key={'id': '1'}
)
print(response['Item'])

# Scan (get all)
response = table.scan()
print(response['Items'])

# PutItem
table.put_item(
    Item={
        'id': '3',
        'firstname': 'Paul',
        'lastname': 'Kerry'
    }
)

# UpdateItem
table.update_item(
    Key={'id': '3'},
    UpdateExpression='SET firstname = :newfn',
    ExpressionAttributeValues={
        ':newfn': 'Alex'
    }
)

# DeleteItem
table.delete_item(
    Key={'id': '3'}
)
