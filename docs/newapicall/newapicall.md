# Adding a New API Call


Adding an new API call can be performed by taking advantage of the boto3 event system. The boto3 event system allows users to register a function to a specific event. The function sits idle until the program reaches a line calling the event. Once the event is reached, all registered functions are called in the order they subscribed to the event. 

An registered function is called with keyword arguments. These arguments can be modified or returned to implement the functions purpose. 

The following is an example of an event shown on the boto3 documentation page:
```
import boto3

s3 = boto3.client('s3')

# Access the event system on the S3 client
event_system = s3.meta.events

# Create a function
def add_my_bucket(params, **kwargs):
    # Add the name of the bucket you want to default to.
    if 'Bucket' not in params:
        params['Bucket'] = 'mybucket'

# Register the function to an event
event_system.register('provide-client-params.s3.ListObjects', add_my_bucket)

response = s3.list_objects()
```


## Boto3 Specific Events
Boto3 allows for functions to be registered to one of three event types. 

* 'creating-client-class'
* 'creating-resource-class'
* 'providing-client-params


### creating-client-class
This event takes place when a client class is created for a service. When the first instantiation for the client class occurs the service for that client class is also created. 

Use Case: adding methods to the client class

### creating-resource-class
This event occurs when a resouce class is created. After instantiation of the resource class this event can be used. 

Use Case: adding methods to the resource class

### provide-client-params
This event is emmited before validation of the parameters passed to the client method. 

Use Case: inject or modify parameters prior to the parameters being validated and built into a request

----


Note: All events can also utilize inheritance from their respective classes (inheriting from the client or resource class).

-------

## Conclusion

By registering functions to events we gain the ability to call functions on top of the existing boto3 library services. We can also pass into functions custom parameters to support metadata fields needed in ObjectScale.

This will allow us to extend the existing calls with no addition work by the user.

The only other functionality for a complete new API call is where the new field is held!

## Important Terms
Session: a session manages state about a particular configuration
Stores Credentials, AWS Region, and profile related info

Clients: provide low-level interface to AWS whose methods map close to 1:1 with service APIs

Resources: represent an object oriented interface to AWS.(resources must have at least one identifier

Signature Version 4 signing process: the process to add authentication information to AWS API requests sent by HTTP. 

How Signature Version 4 works
1. Create a canonical request
2. Use the canonical request and additional metadata to create a string for signing
3. Derive a signing key from your AWS secret access key. Then use the signing key, and the string from the previous setep to create a signature.
4. Add the resulitng signature to the HTTP  request in a header or as a query string paramter

References:

https://docs.aws.amazon.com/general/latest/gr/signature-version-4.html

https://boto3.amazonaws.com/v1/documentation/api/latest/index.html
