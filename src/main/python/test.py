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

# client.delete_object(Bucket="testBucket1", Key="testObj1.txt")
# client.delete_object(Bucket="testBucket1", Key="testObj2.txt")
# client.delete_object(Bucket="testBucket1", Key="testObj3.txt")
# request = client.delete_bucket(Bucket='testBucket1')

# create bucket with indexed metadata key "lastmodified"
request = client.create_bucket(Bucket='testBucket1', CreateBucketConfiguration={
    'LocationConstraint': 'us-west-2'}, SearchMetaData='LastModified;datetime')

# Set-up / put objects in bucket
content = "This is a test string for body of object"
client.put_object(Body= content, Bucket='testBucket1', Key="testObj1.txt")
client.put_object(Body= content, Bucket='testBucket1', Key="testObj2.txt")
client.put_object(Body= content, Bucket='testBucket1', Key="testObj3.txt")

# metadatasearch on last modified, maxkeys = 1
print("First Response\n")
response = client.metadata_search(Bucket='testBucket1', Query='LastModified > 2018-03-01T11:22:00Z', MaxKeys=1, Marker="")
print(response)


print("\n\nSecond Page \n")
# Using nextmarker from response, get next page
mark1 = response.get('NextMarker')
response = client.metadata_search(Bucket='testBucket1', Query='LastModified > 2018-03-01T11:22:00Z', MaxKeys=1, Marker=mark1)
print(response)

print("\n\nThird Page \n")
# Using nextmarker from response, get next page
mark2 = response.get('NextMarker')
response = client.metadata_search(Bucket='testBucket1', Query='LastModified > 2018-03-01T11:22:00Z', MaxKeys=1, Marker=mark2)
print(response)



