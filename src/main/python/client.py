from boto3.session import Session

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
from cgitb import reset
import boto3
import urllib3
import botocore
import requests
import sys, os, base64, datetime, hashlib, hmac
import os

from boto3.session import Session

from botocore import BOTOCORE_ROOT

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



class MyClass(boto3):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        print('Resource instantiated!')

        event_system = s3.meta.events # Access the event system on the S3 client

        # Accessing parameters method
        def get_metadata_parameter(**kwargs):

            #print("INSIDE GET HOOK METHOD")

            # Checking if metadata field was entered
            parameters = kwargs.get('params')
            if 'SearchMetaData' in parameters:
                global MetaDataString # Holds metadata string parameter
                
                MetaDataString = parameters.get('SearchMetaData') # Assign to global variable


        # modify the create bucket request parameters
        def add_metadata_parameter(**kwargs):
            parameters = kwargs.get('params') # get params dict in kwargs

            headers = parameters.get('headers') # get headers field

            # Formatting Metadata search request field.
            # http://doc.isilon.com/ECS/3.6/DataAccessGuide/GUID-5E2A0B34-2FE5-498F-8627-C54C0681EEA7.html
            # Must be specific format
            
            headers['x-emc-metadata-search'] = MetaDataString


        #register events
        event_system.register('before-call.s3.CreateBucket', add_metadata_parameter) # Before call builds everything and is called just before request is sent

        event_system.register('before-parameter-build.s3.CreateBucket', get_metadata_parameter) # Before parameter build is called before anything happens to the parameters input into the original request






s3 = MyClass.client("s3", **cred_object)

# boto3 extended createbucket call 
request = s3.create_bucket(Bucket='mybucket', CreateBucketConfiguration={'LocationConstraint': 'us-west-2'}, 
    SearchMetaData='Size,CreateTime,LastModified,x-amz-meta-STR;String,x-amz-meta-INT;Integer')


# PRINTING REQUESTS / RESPONSES
print("\n CREATE BUCKET RESPONSE\n", request,"\n")
response = s3.list_buckets()
print(response)

# Response after delete bucket
response = s3.delete_bucket(Bucket = "mybucket")

# Double check to see if bucket deleted
response = s3.list_buckets()
print(response)