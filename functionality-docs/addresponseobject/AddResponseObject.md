#  Adding response object (shape) to new api call in boto3
## Adding shape to sdk-extras.json file
Boto3 allows developers to add functionality to the client at runtime by using the service-2.sdk-extras.json file.json file located under the  ~/aws/models/s3/2006-03-01 folder. Here's a link for adding a new api call to boto3 (https://github.com/EMCECS/objectscale-s3-client-python/blob/main/docs/newapicall/newapicall.md)

In order to add a response object for our new method we have to define a new shpae under the the shapes section of the dictionary. 

After adding said shape, we have to add the shape to our new api call by using the "output" field. 

IMPORTANT: One also needs the fields location: and locationname: uncder the members fields
