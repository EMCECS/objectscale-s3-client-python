'''
Copyright 2022 Dell Technologies. All Rights Reserved.

Licensed under the Apache License, Version 2.0 (the "License");
you may not use this file execpt in compliance with License.
You may obtain a copy of the License at

http://www.apache.org/licenses/LICENSE-2.0

Unless required by applicable law or agreed to in writing, software
distributed under the License is distributed on an "AS IS" BASIS,
WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied. 
See the License for the specific language governing permissions and
limitations under the License.
'''

from unittest import mock
import unittest
import urllib3, os, sys
from cgitb import reset
import boto3

from boto3.session import Session

urllib3.disable_warnings()


script_dir = os.path.dirname(__file__) #<-- absolute dir the script is in
rel_path = '../../../../creds.txt'
abs_file_path = os.path.join(script_dir, rel_path)

with open(abs_file_path) as file:
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


session = Session()
client = session.client('s3', **cred_object)

# res = client.list_buckets()
# print(res)

res = client.create_bucket(Bucket='mybucket', CreateBucketConfiguration={'LocationConstraint': 'us-west-2'}, SearchMetaData='Size,CreateTime,LastModified,x-amz-meta-STR;String,x-amz-meta-INT;Integer')

res = client.create_bucket(Bucket='ourbucket', CreateBucketConfiguration={'LocationConstraint': 'us-west-2'}, SearchMetaData='Size,CreateTime,LastModified,x-amz-meta-STR;String,x-amz-meta-INT;Integer')


# res = client.get_bucket_acl(Bucket='mybucket')
# print(res)

boto3.set_stream_logger('')


res = client.get_system_metadata()
print(res)

# res = client.get_search_metadata(Bucket='mybucket')
# print(res['IndexableKeys'])

# res = client.disable_metadata_search(Bucket='mybucket')
# print(res['ResponseMetadata']['HTTPStatusCode'])

client.delete_bucket(Bucket='mybucket')
client.delete_bucket(Bucket='ourbucket')




