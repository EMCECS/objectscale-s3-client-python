import boto3
from boto3 import Session
import urllib3

urllib3.disable_warnings()

with open("creds.txt") as file:
    lines = file.readlines()
    Endpoint = lines[0].strip()
    Access_Key = lines[2].strip()
    Secret_Key1 = lines[3].strip()

cred_object = {
    "endpoint_url": Endpoint,
    "aws_access_key_id": Access_Key,
    "aws_secret_access_key": Secret_Key1,
    "use_ssl": False,
    "verify": False
}

# print(cred_object)

client = boto3.client("s3", **cred_object)

if client is None: 
    print("Failed")

response = client.list_buckets()
print(response)

# use_ssl=False,
# verify=False

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