# Method for making extras file visible to boto3

The loader extension method outlined in `everythininextras.md` is a place to start when it comes to achieving our goal of having the extensions accessible to the s3 library. The main problem is in how to invoke `session._loader.search_paths.extend(["/tmp/boto"])` on the default session without requiring the user to add any lines of code. The library should ideally just be able to be imported and then our extensions can be used. The following method will allow for that.

## Override boto3 default session initialization

Upon creating a new client with boto3, it is registered under a default session that needs to be initialized. This session is where the default shapes for boto3's api calls are loaded, and as a result, this is where we need to look to make our extension of these calls accessible. This can be accomplished with the loader extension, but ideally we won't need to modify the boto3 code directly by adding this call to the session initialization function.

The best option is to override the default initialization function with one of our own that includes this loader extension. This begs the same question of how can we add this function without modifying the boto3 code, but this can be done by including it in our own separate python module. This will be an init module running upon including our library that extends boto3 and assigns the boto3 session initialization function as our custom function. 

All that is necessary to be able to invoke our extensions form here is including boto3 through our objectscale_s3_client as follows:

`from objectscale_s3_client import boto3`

For now, we have been able to test this solution by adding the python module to a package in pythons site-packages so it is visible for including in our demo modules. From here we can demonstrate that the module is accessed and the default initialization function is overwritten.

## New method

After further reasearch, the method defined above poses some problems when it comes to achieving our goal. If we add our JSON file to the loader in this way, then the file will be added as a separate service. The main problem is in how to add the extras file to the extras for the s3 service. If we include the extras in a separate sevice like with the above method, when a user wants to access our methods, they won't have the s3 session methods also available. We need to account for this. This must also be done without modifying old boto3 code, and through the simplest means possible, ideally just by including the library.

## Override loader registration and load functions

The function overriding idea in the old method will be useful in this method for changing aspects of boto3 code without having to directly update it. What we have to do with this is include a file in the extras of the s3 service without directly putting it in the repository. To do this, we must first understand how boto organizes the session packages at its disposal. Packages are organized in the following configuration:

```
<root>
  |
  |-- servicename1
  |   |-- 2012-10-25
  |       |-- service-2.json
  |-- ec2
  |   |-- 2014-01-01
  |   |   |-- paginators-1.json
  |   |   |-- service-2.json
  |   |   |-- waiters-2.json
  |   |-- 2015-03-01
  |       |-- paginators-1.json
  |       |-- service-2.json
  |       |-- waiters-2.json
  |       |-- service-2.sdk-extras.json
```

We want to add our JSON file as an extra in the s3 service. However, the loader will only add the file as an extra if the file is part of the s3 services file layout defined above. We can change this by overriding a few functions in botocore's loader and session modules. To add the extras search path to the loader, we simply need to include a search path string in the parameters of the `create_loader` function. We can do this by overriding the `register_data_loader` function in botocores session module, where the `create_loader` function is invoked, and including our own custom search path. 

Doing this step alone will not allow our extension metods to be invoked. Botocore still expects the extras file to be in the same directory as the main service commands, so it will only look there for loading any extras data. In this case, it will not find the extras file we want it to find. For that to happen, we have to modify the logic of the `load_service_model` function in botocore's loader module to make an exception for our s3 extension. We do this by overriding the function and loading extras from our version 2023-2-11 file when the service name is s3. Afte forcing the loader to load our extras file in this way, any methods we add to the JSON file can be invoked freely after including the library.