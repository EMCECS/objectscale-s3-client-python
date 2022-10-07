import boto3
from boto3 import Session
import creds.py



cred_object = {
    "aws_access_key_id": creds.Access_Key,
    "aws_secret_access_key": creds.Secret_Key1,
    "endpoint_url": creds.Endpoint,
}

client = boto3.client("s3", **cred_object)

client.create_bucket(Bucket="new")

client.list_buckets()




# c = boto3.client("s3")

# print(c)



# session = Session()
# credentials = session.get_credentials()
# # Credentials are refreshable, so accessing your access key / secret key
# # separately can lead to a race condition. Use this to get an actual matched
# # set.
# current_credentials = credentials.get_frozen_credentials()

# # I would not recommend actually printing these. Generally unsafe.
# print(current_credentials.access_key)
# print(current_credentials.secret_key)
# print(current_credentials.token)