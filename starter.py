import boto3;

# some starter code to connect to s3
s3 = boto3.resource('s3');
for bucket in s3.buckets.all():
    print(bucket.name)