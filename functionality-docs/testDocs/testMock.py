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

def custom_method(self):
    print("custom_method entered")
    res = self.head_bucket(Bucket="new") # this operation checks to see if a bucket exists
    print("res")
    print("call list buckets")
    self.list_buckets()
    # print(res) # head_bucket call is possible


def add_custom_method(class_attributes, **kwargs):
    print('We can add methods to events!\n')
    class_attributes['my_method'] = custom_method

class TestSession(unittest.TestCase):
    def testCustomMethodCalled(self):
        self.session = Session()
        self.session.events.register('creating-client-class.s3', add_custom_method)
        self.client = self.session.client('s3', **cred_object)
        
        res = self.client.create_bucket(Bucket='new')
        print("Create Bucket Response Code: ")
        print(res)
        self.client.list_buckets = mock.Mock()
        self.client.my_method()
        print("assert call")
        self.client.list_buckets.assert_called()