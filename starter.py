import boto3;

# Get the service resource.
dynamodb = boto3.resource('dynamodb')

# Create the DynamoDB table.
# note that you do not need to define non-key attributes of table, here we have only defined post_id
table = dynamodb.create_table(
    TableName='posts',
    KeySchema=[
        {
            'AttributeName': 'post_id',
            'KeyType': 'HASH'
        },
    ],
    AttributeDefinitions=[
        {
            'AttributeName': 'post_id',
            'AttributeType': 'N'
        },
    ],
    ProvisionedThroughput={
        'ReadCapacityUnits': 1,
        'WriteCapacityUnits': 1
    }
)

# Wait until the table exists.
table.wait_until_exists()

# Print out some data about the table.
print(table.item_count)