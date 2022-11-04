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

# print(cred_object)




def custom_method(self):
    res = self.head_bucket(Bucket='drayerbucket') # this operation checks to see if a bucket exists
    # print(res) # head_bucket call is possible


def add_custom_method(class_attributes, **kwargs):
    print('We can add methods to events!\n')
    class_attributes['my_method'] = custom_method





    # if 'Bucket' not in class_attributes:
    #     class_attributes['Bucket'] = 'drayerbucket'

session = Session()
session.events.register('creating-client-class.s3', add_custom_method)



client = session.client('s3', **cred_object)

# client.meta.method_to_api_mapping

if client is None: 
    print('Failed')

# registerEvent = client.meta.events

res = client.my_method() # parameters passed in method
# res = client.list_objects(Bucket='drayerbucket')
res = client.list_buckets()
# print(res)

print('----------------------------------------------------------------')

res = client.create_bucket(Bucket='new')
print("Create Bucket Response Code: ")
print(res)

res = client.delete_bucket(Bucket='new')
print("Delete Bucket Response Code: ")
print(res['ResponseMetadata']['HTTPStatusCode'])

res = client.list_buckets()
# print(res)

print('----------------------------------------------------------------')

res = client.ping()
print('Ping Response Metadata:')
print(res)






# sample = botocore.awsrequest

# sample.AWSPreparedRequest(method,url,headers,body,stream_output)

# sample.AWSResponse()














# # Complete Sig 4 process

# # Request values
# method = "GET"
# service = "s3"
# host = "examplehost.com"
# region = "us-east -1"
# endpoint = Endpoint
# request_parameters = "Action=GetMetadataSearchList"

# def sign(key, msg):
#     return hmac.new(key, msg.encode("utf-8"), hashlib.sha256).digest()

# def getSignatureKey(key, dateStamp, regionName, serviceName):
#     kDate = sign(("AWS4" + key).encode("utf-8"), dateStamp)
#     kRegion = sign(kDate, regionName)
#     kService = sign(kRegion, serviceName)
#     kSigning = sign(kService, "aws4_request")
#     return kSigning

# # Access Key
# Access_Key

# # Secret Key
# Secret_Key1

# # Create a date for headers and the credential string
# t = datetime.datetime.utcnow()
# amzdate = t.strftime("%Y%m%dT%H%M%SZ")
# datestamp = t.strftime("%Y%m%d") # Date w/o time, used in credential scope

# # Step 1 is to define the verb (GET, POST, etc.)

# # Step 2: Create canonical URI--the part of the URI from domain to query 
# canonical_uri = "/" 

# # Step 3: Create the canonical query string.
# canonical_querystring = request_parameters

# # Step 4: Create the canonical headers and signed headers.
# canonical_headers = "host:" + host + "\n" + "x-amz-date:" + amzdate + "\n"

# # Step 5: Create the list of signed headers.
# signed_headers = "host;x-amz-date"

# # Step 6: Create payload hash (hash of the request body content).
# payload_hash = hashlib.sha256(("").encode("utf-8")).hexdigest()

# # Step 7: Combine elements to create canonical request
# canonical_request = method + "\n" + canonical_uri + "\n" + canonical_querystring + "\n" + canonical_headers + "\n" + signed_headers + "\n" + payload_hash


# algorithm = "AWS4-HMAC-SHA256"
# credential_scope = datestamp + "/" + region + "/" + service + "/" + "aws4_request"
# string_to_sign = algorithm + "\n" +  amzdate + "\n" +  credential_scope + "\n" +  hashlib.sha256(canonical_request.encode("utf-8")).hexdigest()


# # Create the signing key using the function defined above.
# signing_key = getSignatureKey(Secret_Key1, datestamp, region, service)


# # Sign the string_to_sign using the signing_key
# signature = hmac.new(signing_key, (string_to_sign).encode("utf-8"), hashlib.sha256).hexdigest()

# # Create authorization header and add to request headers
# authorization_header = algorithm + " " + "Credential=" + Access_Key + "/" + credential_scope + ", " +  "SignedHeaders=" + signed_headers + ", " + "Signature=" + signature


# headers = {"x-amz-date":amzdate, "Authorization":authorization_header}


# # ************* SEND THE REQUEST *************
# request_url = endpoint + "?" + canonical_querystring

# print("\nBEGIN REQUEST++++++++++++++++++++++++++++++++++++")
# print("Request URL = " + request_url)
# r = requests.get(request_url, headers=headers)

# print("\nRESPONSE++++++++++++++++++++++++++++++++++++")
# print("Response code: %d\n" % r.status_code)
# print(r.text)





# NOT USED FUNCTIONALITY

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