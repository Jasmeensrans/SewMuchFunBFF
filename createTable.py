import boto3


def create_posts_table()-> int:
    """Creates a post table in dynamodb if it does not already exist

    Returns:
        int: returns the number of elements in the post table
    """
    # Get the service resource.
    dynamodb = boto3.resource('dynamodb')
    dynamodb_client = boto3.client('dynamodb')

    # check if the posts table already exists, if it does return number of elements
    all_tables = dynamodb_client.list_tables()['TableNames']
    if "posts" in all_tables:
        response = dynamodb_client.scan(
            TableName="posts",
            Select='COUNT'
        )

        post_count = response['Count']
        return post_count
    else:
        posts_table = dynamodb.create_table(
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
    posts_table.wait_until_exists()

    # return the number of
    return posts_table.item_count
