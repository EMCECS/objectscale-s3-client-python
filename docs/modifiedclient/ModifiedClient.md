# Creation of a client with all registered events using objectscale library import
## General idea
Define method A into a defined module.
Use method A to return modified client. 
Modified client is then able to perform objectscale tasks.

E.g 
client = create_objectscale_s3_client( cred)

## Will it work?
Yes, it will work as the modified client is able to run the events, access parameters, and modify the headers all the same