# Extending an API Call (Adding metadata parameter to create bucket call)
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
## Possible Solution 2: Modifying S3 client at runtime using events
For this approach, the boto3 extensibility [document](https://boto3.amazonaws.com/v1/documentation/api/latest/guide/events.html) is very helpful as it has coding examples to add methods to the client class or creating classes for the client class to inherit from. The primary event for this solution is ...

    'creating-client-class.service-name'
where service-name is the name of the service (s3)

I'm doubtful that this solution would work as we are still not able to modify the createbucket call itself. 

