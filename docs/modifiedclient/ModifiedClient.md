# Creation of a client with all registered events using objecscale library import
## General idea
Register method A to the ObjectScale Class. 
Within method A and using boto3, create a client X and register all necessary events to X. 
Return client X with all registered events at the end of the method. 

E.g 
client = ObjectScale.create_objscale_client(name, cred)