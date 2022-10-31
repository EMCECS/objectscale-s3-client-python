import boto3
import os

#CREDENTIALS
cur_path = os.path.realpath(__file__)
new_path = os.path.relpath('../../CREDS.txt', cur_path)

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
    print("INSIDE HOOK METHOD")

    #getting params dict in kwargs
    parameters = kwargs.get('params')

    #getting headers field
    headers = parameters.get('headers')

    # Formatting Metadata search rquest field. list of dictionaries? 
    MDList = '[{"datatype":"integer","name":"x-amz-meta-custom"}]'
    MDList2 = 'keyname[;string]'
    MDList3 = 'x-amz-meta-custom[integer]'

    # Seeing if i can modify header field
    #headers['x-emc-metadata-search'] = 'Metadata'
    
    #print((headers))
    print("END HOOK METHOD")

#register event
event_system.register('before-call.s3.CreateBucket', add_metadata_parameter)

# boto3 native createbucket call
request = s3.create_bucket(Bucket='mybucket', CreateBucketConfiguration={'LocationConstraint': 'us-west-2'})

# Adding custom parameters into createbucket 
#request = s3.create_bucket(Bucket='mybucket', CreateBucketConfiguration={'LocationConstraint': 'us-west-2', 'Tester' : 'I am being Tested'} )


# PRINTING REQUESTS / RESPONSES 
print("\n CREATE BUCKET REQUEST\n", request,"\n")
response = s3.list_buckets()
print(response)

# Response after delete bucket
response = s3.delete_bucket(Bucket = "mybucket")
print("\n", response, "\n")

# Double check to see if bucket deleted
response = s3.list_buckets()
print(response)
print("\n")