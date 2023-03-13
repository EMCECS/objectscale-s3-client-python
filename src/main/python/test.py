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

#boto3.set_stream_logger('')
'''
res = client.create_bucket(Bucket='mybucket', CreateBucketConfiguration={'LocationConstraint': 'us-west-2'}, SearchSearchMetaData='Size,CreateTime,LastModified,x-amz-meta-STR;String,x-amz-meta-INT;Integer')

res = client.get_bucket_acl(Bucket='mybucket')
# print(res)

# boto3.set_stream_logger('')


res = client.get_search_SearchMetaData(Bucket='mybucket')
print(res)

res = client.disable_SearchMetaData_search(Bucket='mybucket')
print(res)

res = client.get_search_SearchMetaData(Bucket='mybucket')
print(res)

client.delete_bucket(Bucket='mybucket')

'''
# create bucket with indexed SearchMetaData key "lastmodified"
request = client.create_bucket(Bucket='TESTBUCKET2', CreateBucketConfiguration={
    'LocationConstraint': 'us-west-2'}, SearchMetaData='LastModified;datetime,Size;integer')

# Set-up / put objects in bucket 
content1 = "This is a test string for body of object"
content2 = "Short"
content3 = "This is medium"
client.put_object(Body= content1, Bucket='TESTBUCKET2', Key="testObj1.txt")
client.put_object(Body= content2, Bucket='TESTBUCKET2', Key="testObj2.txt")
client.put_object(Body= content3, Bucket='TESTBUCKET2', Key="testObj3.txt")

print("\n\nBEFORE REQUEST\n\n")
response = client.metadata_search(Bucket='TESTBUCKET2', Query='LastModified > 2018-03-01T11:22:00Z and Size > 7', Attributes = 'ContentType', Sorted = "Size", IncludeOlderVersion=False)
print("\n\nRESPONSE\n",response,"\n\n")
print(response['ObjectMatches'][0]["objectName"])
print(response['ObjectMatches'][1]["objectName"])
print(type(response['ObjectMatches'][1]["queryMds"]["mdMap"]["size"]))


# Clean up/ teardown of objects/buckets
client.delete_object(Bucket="TESTBUCKET2", Key="testObj1.txt")
client.delete_object(Bucket="TESTBUCKET2", Key="testObj2.txt")
client.delete_object(Bucket="TESTBUCKET2", Key="testObj3.txt")
request = client.delete_bucket(Bucket='TESTBUCKET2')



