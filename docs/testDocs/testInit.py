from unittest import mock
import unittest
import urllib3, os, sys

from boto3.session import Session
from botocore import exceptions
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

def custom_method(self):
    print("custom_method entered")
    res = self.head_bucket(Bucket="new") # this operation checks to see if a bucket exists
    # print(res) # head_bucket call is possible


def add_custom_method(class_attributes, **kwargs):
    print('We can add methods to events!\n')
    class_attributes['my_method'] = custom_method

class TestSession(unittest.TestCase):
    #def setUp(self):
        #self.session = Session()
        #custom_method = mock.Mock()
        #self.session.events.register('creating-client-class.s3', add_custom_method)
        #session = mock.Mock()
        #client = self.session.client('s3', **cred_object)
        #client.my_method()
        #client.create_bucket()
        #client.delete_bucket()
        #custom_method.assert_called()

    def testCustomMethodCalled(self):
        self.session = Session()
        custom_method = mock.Mock()
        print("register")
        self.session.events.register('creating-client-class.s3', add_custom_method)
        print("client create")
        client = self.session.client('s3', **cred_object)
        print("create bucket call")
        res = client.create_bucket(Bucket='new')
        print("Create Bucket Response Code: ")
        print(res)
        res = client.list_buckets()
        print(res)
        custom_method = mock.Mock()
        try:
            print("call client methods")
            client.my_method()
            client.create_bucket()
            client.delete_bucket()
        except exceptions.ClientError:
            print("HeadBucket failed") 
        custom_method.assert_called()

#if __name__ == "__main__":
#    test = TestSession()
#    TestSession.testCustomMethodCalled(test)