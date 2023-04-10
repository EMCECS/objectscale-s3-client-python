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
import boto3

def create_objectscale_s3_client(cred):
    # BEGIN API CODE
    s3 = boto3.client("s3", **cred)

    # Access the event system on the S3 client
    event_system = s3.meta.events


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
            #print(MetaDataString)

        print("END GET HOOK METHOD")

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

        print("END ADD HOOK METHOD")


    #register events
    # Before call builds everything and is called just before request is sent
    event_system.register('before-call.s3.CreateBucket', add_metadata_parameter)
    # Before parameter build is called before anything happens to the parameters input into the original request
    event_system.register('before-parameter-build.s3.CreateBucket', get_metadata_parameter)

    return s3

