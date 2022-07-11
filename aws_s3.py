import config
import boto3
import pandas as pd

# two interfaces: boto3.client() boto3.resource()

s3 = boto3.resource(
    service_name='s3',
    region_name=config.region,
    aws_access_key_id=config.aws_access_key_id,
    aws_secret_access_key=config.aws_secret_access_key
)

for bucket in s3.buckets.all():
    print(bucket.name)

bucket = s3.Bucket(bucket_name='<bucketname>')

for object in bucket.objects.all():
    print(object)

data = bucket.Object(key='foo.csv').get()
# s3.Object(bucket_name='<bucketname>', key='foo.csv')
data

df = pd.read_csv(data['Body'])
df

# upload file
bucket.upload_file(
        Filename='foo.csv', # local filename
        Key='foo.csv' # s3 filename
)

# download file
bucket.download_file(
        Key='foo.csv',
        Filename='foo.csv'
)

# copy between buckets
copy_source = {
    'Bucket': 'bucket_from_name',
    'Key': 'file_name'
}
s3.Object('bucket_to_name', 'file_name').copy(copy_source)

# delete
s3.Object(bucket_name='<bucketname>', key='foo.csv').delete()
s3.Bucket(bucket_name='<bucketname>').delete() # delete only if bucket is empty
