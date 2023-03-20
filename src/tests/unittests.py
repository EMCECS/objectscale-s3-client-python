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

'''
class CreateBucketTests(unittest.TestCase):
# boto3 extended createbucket call
 def testCreateBucketCalled(self):
        self.session = Session()
        self.client = self.session.client('s3', **cred_object)

        self.client.create_bucket = mock.Mock()
        
        self.client.create_bucket(Bucket='mybucket', CreateBucketConfiguration={'LocationConstraint': 'us-west-2'}, 
        SearchMetaData='Size,CreateTime,LastModified,x-amz-meta-STR;String,x-amz-meta-INT;Integer')

        self.client.create_bucket.assert_called()

class GetSearchMetadataTests(unittest.TestCase):
 def testGetSearchMetadataResult(self):
        self.session = Session()
        self.client = self.session.client('s3', **cred_object)
        
        self.client.create_bucket(Bucket='mybucket', CreateBucketConfiguration={'LocationConstraint': 'us-west-2'}, 
        SearchMetaData='Size,CreateTime,LastModified,x-amz-meta-STR;String,x-amz-meta-INT;Integer')

        res = self.client.get_search_metadata(Bucket='mybucket')
        self.assertEqual(res['IndexableKeys'], [{'Name': 'LastModified', 'Datatype': 'datetime'}, {'Name': 'x-amz-meta-int', 'Datatype': 'integer'}, {'Name': 'Size', 'Datatype': 'integer'}, {'Name': 'CreateTime', 'Datatype': 'datetime'}, {'Name': 'x-amz-meta-str', 'Datatype': 'string'}])

# should be failing as of 2/12/23
# Might be a bug regarding server
class DisableMetadataSearchTests(unittest.TestCase):
 def testDisableMetadataSearch(self):
        self.session = Session()
        self.client = self.session.client('s3', **cred_object)

        #boto3.set_stream_logger('')
        
        self.client.create_bucket(Bucket='mybucket', CreateBucketConfiguration={'LocationConstraint': 'us-west-2'}, 
        SearchMetaData='Size,CreateTime,LastModified,x-amz-meta-STR;String,x-amz-meta-INT;Integer')

        # Testing get call
        res = self.client.get_search_metadata(Bucket='mybucket')
        self.assertEqual(res['IndexableKeys'], [{'Name': 'LastModified', 'Datatype': 'datetime'}, {'Name': 'x-amz-meta-int', 'Datatype': 'integer'}, {'Name': 'Size', 'Datatype': 'integer'}, {'Name': 'CreateTime', 'Datatype': 'datetime'}, {'Name': 'x-amz-meta-str', 'Datatype': 'string'}])

        # Test disable call return code = 204
        res = self.client.disable_metadata_search(Bucket='mybucket')
        self.assertEqual(204, res['ResponseMetadata']['HTTPStatusCode'])

        # Testing get call again
        # Shouldn't return anything if disabled!!
        # check getcall with bucket wihtout indexed fields, put it here
        res = self.client.get_search_metadata(Bucket='mybucket')

        # TODO: determine expected response after metadata search is disabled (after ObjectScale bug is fixed)
        self.assertEqual(res.get('IndexableKeys', None), None)

'''
class ObjectScaleUnitTestSuite(unittest.TestCase):
    def setUp(self):
        self.session = Session()
        self.client = self.session.client('s3', **cred_object)

        #boto3.set_stream_logger('')
        
        self.client.create_bucket(Bucket='TESTBUCKET1', CreateBucketConfiguration={'LocationConstraint': 'us-west-2'}, 
        SearchMetaData='Size,CreateTime,LastModified,x-amz-meta-STR;String,x-amz-meta-INT;Integer')
        
        self.client.create_bucket(Bucket='TESTBUCKET2', CreateBucketConfiguration={'LocationConstraint': 'us-west-2'}, 
        SearchMetaData='LastModified;datetime')
        
        # Set-up / put objects in bucket 
        content = "This is a test string for body of object"
        self.client.put_object(Body= content, Bucket='TESTBUCKET2', Key="testObj1.txt")
        self.client.put_object(Body= content, Bucket='TESTBUCKET2', Key="testObj2.txt")
        self.client.put_object(Body= content, Bucket='TESTBUCKET2', Key="testObj3.txt")
        
    def tearDown(self):
        self.client.delete_bucket(Bucket='TESTBUCKET1')
        
        # Clean up/ teardown of objects/buckets testbucket 2
        self.client.delete_object(Bucket="TESTBUCKET2", Key="testObj1.txt")
        self.client.delete_object(Bucket="TESTBUCKET2", Key="testObj2.txt")
        self.client.delete_object(Bucket="TESTBUCKET2", Key="testObj3.txt")
        self.client.delete_bucket(Bucket='TESTBUCKET2')
        
    # Tests to see if boto3 native createbucket call works
    def testCreateBucketCall(self):
        # Check extended call
        response = self.client.create_bucket(Bucket='TESTCREATEBUCKET', CreateBucketConfiguration={'LocationConstraint': 'us-west-2'}, 
        SearchMetaData='LastModified;datetime')
        
        # Get status code
        statusCode = response.get("ResponseMetadata").get("HTTPStatusCode")
        # Check if status code is good
        self.assertEqual(statusCode, 200)
        
        # Check native call
        response = self.client.create_bucket(Bucket='TESTCREATEBUCKET2', CreateBucketConfiguration={'LocationConstraint': 'us-west-2'})
        
        # Get status code
        statusCode = response.get("ResponseMetadata").get("HTTPStatusCode")
        # Check if status code is good
        self.assertEqual(statusCode, 200)
        
    # Checks to see if search metadata is being returned    
    def testGetSearchMetadata(self):
        res = self.client.get_search_metadata(Bucket='TESTBUCKET1')
        self.assertEqual(res['IndexableKeys'], [{'Name': 'LastModified', 'Datatype': 'datetime'}, {'Name': 'x-amz-meta-int', 'Datatype': 'integer'}, {'Name': 'Size', 'Datatype': 'integer'}, {'Name': 'CreateTime', 'Datatype': 'datetime'}, {'Name': 'x-amz-meta-str', 'Datatype': 'string'}])
    
    # should be failing as of 2/12/23
    # Might be a bug regarding server
    def testDisableMetadataSearch(self):
        # Test disable call return code = 204
        res = self.client.disable_metadata_search(Bucket='TESTBUCKET1')
        # Testing get call again
        # Shouldn't return anything if disabled!!
        # check getcall with bucket wihtout indexed fields, put it here
        res = self.client.get_search_metadata(Bucket='mybucket')

        # TODO: determine expected response after metadata search is disabled (after ObjectScale bug is fixed)
        self.assertEqual(res.get('IndexableKeys', None), None)
        
        
    # Checks to see if metadata query is working with pagination
    def testMetadataSearch(self):
        # metadatasearch on last modified, maxkeys = 1
        response = self.client.metadata_search(Bucket='TESTBUCKET2', Query='LastModified > 2018-03-01T11:22:00Z', MaxKeys=1)
        self.assertEqual(response['ObjectMatches'][0]['objectName'], 'testObj1.txt')

        # Using nextmarker from response, get next page
        mark1 = response.get('NextMarker')
        response = self.client.metadata_search(Bucket='TESTBUCKET2', Query='LastModified > 2018-03-01T11:22:00Z', MaxKeys=1, Marker=mark1)
        self.assertEqual(response['ObjectMatches'][0]['objectName'], 'testObj2.txt')

        # Using nextmarker from response, get next page
        mark2 = response.get('NextMarker')
        response = self.client.metadata_search(Bucket='TESTBUCKET2', Query='LastModified > 2018-03-01T11:22:00Z', MaxKeys=1, Marker=mark2)
        self.assertEqual(response['ObjectMatches'][0]['objectName'], 'testObj3.txt')
        
class GetSearchSystemMetadataTests(unittest.TestCase):
 def testGetSystemMetadataResult(self):
        self.session = Session()
        self.client = self.session.client('s3', **cred_object)
        
        res = self.client.create_bucket(Bucket='mybucket', CreateBucketConfiguration={'LocationConstraint': 'us-west-2'}, SearchMetaData='Size,CreateTime,LastModified,x-amz-meta-STR;String,x-amz-meta-INT;Integer')

        res = self.client.create_bucket(Bucket='ourbucket', CreateBucketConfiguration={'LocationConstraint': 'us-west-2'}, SearchMetaData='Size,CreateTime,LastModified,x-amz-meta-STR;String,x-amz-meta-INT;Integer')


        res = self.client.get_system_metadata()
        self.assertTrue(res['IndexableKeys'] >= [{'Name': 'Owner', 'Datatype': 'string'}, {'Name': 'Size', 'Datatype': 'integer'}, {'Name': 'CreateTime', 'Datatype': 'datetime'}, \
            {'Name': 'ObjectName', 'Datatype': 'string'}, {'Name': 'LastModified', 'Datatype': 'datetime'}])
        self.assertTrue(res['OptionalAttributes'] >= [{'Name': 'Owner', 'Datatype': 'string'}, {'Name': 'ContentType', 'Datatype': 'string'}, {'Name': 'Size', 'Datatype': 'integer'}, \
            {'Name': 'CreateTime', 'Datatype': 'datetime'}, {'Name': 'Expiration', 'Datatype': 'datetime'}, {'Name': 'ContentEncoding', 'Datatype': 'string'}, \
            {'Name': 'Retention', 'Datatype': 'integer'}, {'Name': 'Namespace', 'Datatype': 'string'}, {'Name': 'ObjectName', 'Datatype': 'string'}, \
            {'Name': 'LastModified', 'Datatype': 'datetime'}, {'Name': 'Etag', 'Datatype': 'string'}, {'Name': 'Expires', 'Datatype': 'datetime'}])


        self.client.delete_bucket(Bucket='mybucket')
        self.client.delete_bucket(Bucket='ourbucket')

    
