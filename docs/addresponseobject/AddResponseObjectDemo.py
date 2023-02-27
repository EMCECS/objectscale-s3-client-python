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
from obs_s3_client import botocore
import boto3
import os
# RUN CODE FROM DIRECTLY INSIDE FOLDER

#CREDENTIALS
cur_path = os.path.realpath(__file__)
new_path = os.path.relpath('../../creds.txt', cur_path)
#new_path = '/home/nathanmarugame/dell/project/CREDS.txt'
file1 = open(new_path, 'r')

cred_object = {}
cred_object['aws_access_key_id'] = file1.readline().strip()
cred_object['aws_secret_access_key'] = file1.readline().strip()


cred_object['endpoint_url'] = file1.readline().strip()
# END CREDENTIALS

# BEGIN API CODE
s3 = boto3.client("s3", **cred_object)

#response = s3.create_bucket(Bucket='mybucket', CreateBucketConfiguration={'LocationConstraint': 'us-west-2'} )
#print(response, "\n")
#s3.delete_bucket(Bucket = "mybucket")


res = s3.ping(TestParameter="Tester")
print(res)