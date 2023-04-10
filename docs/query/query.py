'''
Copyright (c) 2021 Dell Inc., or its subsidiaries. All Rights Reserved.

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
rel_path = '../../../creds.txt'
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
s3 = session.client('s3', **cred_object)

# Access the event system on the S3 client
event_system = s3.meta.events



# Somehow modify the create bucket request parameters
def add_metadata_parameter(**kwargs):
    #print("INSIDE ADD HOOK METHOD")

    #getting params dict in kwargs
    parameters = kwargs.get('params')

    #getting headers field
    headers = parameters.get('headers')

    # Formatting Metadata search rquest field. list of dictionaries? 
    # http://doc.isilon.com/ECS/3.6/DataAccessGuide/GUID-5E2A0B34-2FE5-498F-8627-C54C0681EEA7.html
    # Must be specific format
    # Seeing if i can modify header field
    #headers['x-emc-metadata-search'] ="x-amz-meta-STR;String"
    
    headers['x-emc-metadata-search'] = MetaDataString

    #print("END ADD HOOK METHOD")

# Accessing parameters method
def get_metadata_parameter(**kwargs):

    #print("INSIDE GET HOOK METHOD")

    # Checking if metadata field was entered
    parameters = kwargs.get('params')
    if 'MetaData' in parameters:
        # Holds metadata string parameter
        global MetaDataString
        # Assign to global variable
        MetaDataString = parameters.get('MetaData')

    #print("END GET HOOK METHOD")

# Logger useful for debugging network requests/responses. Displays raw requests/responses
boto3.set_stream_logger('')


#register events
# Before call builds everything and is called just before request is sent
event_system.register('before-call.s3.CreateBucket', add_metadata_parameter)
# Before parameter build is called before anything happens to the parameters input into the original request
event_system.register('before-parameter-build.s3.CreateBucket', get_metadata_parameter)

# boto3 extended createbucket call 
request = s3.create_bucket(Bucket='mybucket', CreateBucketConfiguration={
    'LocationConstraint': 'us-west-2'}, MetaData='x-amz-meta-STR;String')

request = s3.metadata_search(Query='LastModified > 2018-03-01T11:22:00Z')
