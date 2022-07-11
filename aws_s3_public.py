import boto3
import pandas as pd

s3 = boto3.resource(service_name='s3')

bucket = s3.Bucket('snowflake-cookbook')

for object in bucket.objects.all():
    print(object)


data = bucket.Object(key='Chapter02/r3/customer.csv').get()
data

df = pd.read_csv(data['Body'])
df.shape
df.head()
