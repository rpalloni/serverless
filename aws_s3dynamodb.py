import config
import boto3 # sdk

# create session
session = boto3.Session(
    # keys for user with IAM permissions on s3 and dynamodb
    region_name=config.region,
    aws_access_key_id=config.aws_access_key_id,
    aws_secret_access_key=config.aws_secret_access_key
)

# service interfaces
s3 = session.resource(service_name='s3')
dynamodb = session.resource(service_name='dynamodb')

# connect to table and write bucket data
table = dynamodb.Table('Employees')  # Add table ARN to policy
print(table.item_count)

resp = s3.Object(bucket_name='<bucketname>', key='employees.csv').get()
data = resp['Body'].read().decode('utf-8')
print(data)
employees = data.split()
for emp in employees:
    emp = emp.split(',')
    try:
        table.put_item(Item={'id': str(emp[0]), 'name': emp[1], 'age': emp[2]})
    except Exception as err:
        print('Error: '+str(err))

d = table.scan()
print('Employees data:', d['Items'])
