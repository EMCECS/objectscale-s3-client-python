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
import boto3
import os
from ObjectScaleS3 import *
# RUN CODE FROM DIRECTLY INSIDE FOLDER

#CREDENTIALS
cur_path = os.path.realpath(__file__)
new_path = os.path.relpath('../../CREDS.txt', cur_path)
new_path = '/home/nathanmarugame/dell/project/CREDS.txt'
file1 = open(new_path, 'r')

cred_object = {}
cred_object['aws_access_key_id'] = file1.readline().strip()
cred_object['aws_secret_access_key'] = file1.readline().strip()
cred_object['endpoint_url'] = file1.readline().strip()
# END CREDENTIALS

s3 = create_objectscale_s3_client(cred_object)

# boto3 extended createbucket call 
s3.create_bucket(Bucket='mybucket', CreateBucketConfiguration={
    'LocationConstraint': 'us-west-2'}, MetaData='x-amz-meta-STR;String')

# Adding custom parameters into createbucket 
#request = s3.create_bucket(Bucket='mybucket', CreateBucketConfiguration={'LocationConstraint': 'us-west-2'} )

# PRINTING REQUESTS / RESPONSES 
print("\n CREATE BUCKET RESPONSE\n""\n")
response = s3.list_buckets()
print(response)

# Response after delete bucket
response = s3.delete_bucket(Bucket = "mybucket")
#print("\n", response, "\n")

# Double check to see if bucket deleted
response = s3.list_buckets()
print(response)
print("\n")

# Checking to make sure existing calls aren't broken
print("------------------")
response = s3.create_bucket(Bucket='secondbucket', CreateBucketConfiguration={
    'LocationConstraint': 'us-west-2'})
response = s3.list_buckets()
print(response)

s3.delete_bucket(Bucket="secondbucket")
print("-------------DELETE BUCKET---------------------")
response = s3.list_buckets()
print(response)
print("------------------")
