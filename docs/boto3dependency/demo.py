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
from boto3.session import Session
import os
import urllib3
import sys

urllib3.disable_warnings() # removes warning for boto3 operations

sys.modules['boto3'] = None # change the boto3 module to none so the program is no longer dependent on it


script_dir = os.path.dirname(__file__) # absolute dir the script is in
rel_path = '../../../creds.txt'
abs_file_path = os.path.join(script_dir, rel_path) # constructs absolute path from relative and directory of script

# read creds from file
with open(abs_file_path) as file: # reads creds from file
    lines = file.readlines()
    Endpoint = lines[0].strip()
    Access_Key = lines[2].strip()
    Secret_Key1 = lines[3].strip()

# construct cred object
cred_object = {
    "endpoint_url": Endpoint,
    "aws_access_key_id": Access_Key,
    "aws_secret_access_key": Secret_Key1,
    "use_ssl": False,
    "verify": False
}

# instantiate session class
session = Session()



try:
    client = session.client('s3', **cred_object)
    
except ModuleNotFoundError: # catch module not found error
    print("Boto3 is a project dependency!")

