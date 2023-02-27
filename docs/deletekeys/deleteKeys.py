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

# BEGIN API CODE
s3 = boto3.client("s3", **cred_object)

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


# Adding custom parameters into createbucket 
#request = s3.create_bucket(Bucket='mybucket', CreateBucketConfiguration={'LocationConstraint': 'us-west-2', 'Tester' : 'I am being Tested'} )

# PRINTING REQUESTS / RESPONSES 
print("\n CREATE BUCKET RESPONSE\n", request,"\n")
response = s3.list_buckets()
print(response)

print("\n ENABLE \n")
response = s3.getmdkeys(Bucket="mybucket")
print(response)
print("\n")

# Look into head bucket call to see if metadata search is enabled
response = s3.disablemeta(Bucket = "mybucket")
print("\n Printing Disable Response \n")
print(response)

print("\n ENABLE \n")
response = s3.getmdkeys(Bucket="mybucket")
print(response)
print("\n")

# Response after delete bucket
response = s3.delete_bucket(Bucket="mybucket")
#print("\n", response, "\n")

# Double check to see if bucket deleted
response = s3.list_buckets()
print("\n", response)
print("\n")
