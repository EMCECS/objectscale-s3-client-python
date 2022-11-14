# Extending an API Call to boto3 (Adding metadata parameter to create bucket call)
## Possible Solution 1: Using boto3 events before-call handler
 The primary way one would add methods to an existing boto3 call would be through events. The reason being is that all resources and clients in boto3 are created at runtime. The extensibility [document](https://boto3.amazonaws.com/v1/documentation/api/latest/guide/events.html) created by boto3 developers offers no clear way to extend and modify the create bucket function. 
 
However, there is a before-call event handler that allows the user to create a function that would execute before a function is called. The code for the create bucket event handler would look something like this...

    // Access the event system on the s3 client
    event_system = s3.meta.events
    // modify create bucket parameters
    def add_metadata_parameter(self, **kwargs):
    // code here
    // register event
    event_system.register('s3.createbucket.before-call', add_metadata_parameter)
 Source: 	https://github.com/boto/boto3/issues/484
The coding example here isn't perfect but the general idea is there. Also doubtful that this would work as we are not directly modifying the create bucket call directly. 

# How to extend createbucket call?
## Modify request shape in service-2.sdk-extras.json file
In order to extend an api call, one has to modify the shape of the request using the service-2.sdk-extras.json file. When modifying the file, it's important to note that the merge: line at the top of the file merges and doesn't overwrite anything in the source [file](https://github.com/boto/botocore/blob/develop/botocore/data/s3/2006-03-01/service-2.json). It's also important to note that when extending a call, one needs to have the exact dictionary structure used in the source [file](https://github.com/boto/botocore/blob/develop/botocore/data/s3/2006-03-01/service-2.json). Here's a link that demonstrates adding a new parameter to the createbucket request [shape](https://github.com/EMCECS/objectscale-s3-client-python/tree/main/docs/extendapicall/~/.aws/models/s3/2006-03-01)
## Using boto3 event handlers: before-call and before-parameter-build 
In order to fully accomplish our goal of extending boto3 create bucket call, we have to use two events. These events are before-call and before-parameter-build. Differences between these two events are described below and a diagram is linked [here]()
### before-call
before-call event handler allows a developer to add a new method to boto3 that is called directly before the request is sent to the server. Meaning all the input parameters from the original call are formatted and the request is built using the input parameters passed into the call. An important variable that is visible here is "headers".
### before-parameter-build 
before-parameter-build event handler allows a developer to add a new method that is called directly after the call itself. Variables visible here are every input parameter in the call. 
## Why do we need both?
For our specific purposes of adding a new field, we neeeded access to the headers variable field AND the input parameters.
## Demo of registering events and testing added input parameter in createbucket call
https://github.com/EMCECS/objectscale-s3-client-python/blob/main/docs/extendapicall/ExtendAPICallDemo.py 

# PROGRESS
## 10/17 - 10/24 
Minor progress. Setback due to family emergency.

## 10/24 - 10/31
- Custom parameters in the hook method? (Moved to Next Week)
    - Can't pass in "new" parameters into client.create_bucket (i.e. client.create_bucket(Bucket='mybucket',    CreateBucketConfiguration={'LocationConstraint': 'us-west-2'}, 'Tester' : 'I am being Tested')) )
    - Look into CreateBucketConfiguration. 
        - Able to add new parameters into CreateBucketConfiguration?
        -   Scoured [boto3](https://github.com/boto/boto3) and [botocore](https://github.com/boto/botocore) github libraries and found nothing regarding CreateBucketConfiguration.
        - Adding new parameters directly into CreateBucketConfiguration from client?
            - Error:
            botocore.exceptions.ParamValidationError: Parameter validation failed:
            Unknown parameter in CreateBucketConfiguration: "Tester", must be one of: LocationConstraint  

- Able to modify headers from hook method? (COMPLETED)
    - Yes, we can modify headers. Shown in ExtendAPICallDemo.py
    - Current: Check against ECS Testdrive. 
        - Problem: Need to figure out how to format Metadata list
        - Error: 
        botocore.exceptions.ClientError: An error occurred (Invalid metadata search list entered) when calling the CreateBucket operation: A keyname on the request is not a valid indexable key, or the format of the request list is incorrect
        - ERROR FIXED AND TASK COMPLETED
        - Seen in add_metadata_parameter

## 10/31 - 11/7
- Custom parameters in the hook method? (Completed)
    - Can't pass in "new" parameters into client.create_bucket (i.e. client.create_bucket(Bucket='mybucket',    CreateBucketConfiguration={'LocationConstraint': 'us-west-2'}, 'Tester' : 'I am being Tested')) )
    - Look into CreateBucketConfiguration. 
        - Able to add new parameters into CreateBucketConfiguration?
        -   Scoured [boto3](https://github.com/boto/boto3) and [botocore](https://github.com/boto/botocore) github libraries and found nothing regarding CreateBucketConfiguration.
        - Adding new parameters directly into CreateBucketConfiguration from client?
            - Error:
            botocore.exceptions.ParamValidationError: Parameter validation failed:
            Unknown parameter in CreateBucketConfiguration: "Tester", must be one of: LocationConstraint  
    - [DISCOVERY](https://github.com/EMCECS/objectscale-s3-client-python/blob/main/docs/newapicall/newapicall.md): Using botocore loaders and shape definitions, we should be able to extend existing createbucket calls.
- Successfully able to add custom metadata parameter to createbucket call without breaking existing calls.