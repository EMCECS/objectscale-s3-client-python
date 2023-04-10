# Adding a New API Call

Adding an new API call can be done by utilizing the Botocore loader. Boto3 is built atop of library called Botocore, which is shared by the AWS CLI. Botocore holds the lower level implementation that Boto3 runs overtop of. By making model manipulations during the loading phase we have the ability to add new API calls and modify existing calls. 

When a client is instanciated in Boto3 modules are loaded defining the API requests made possible by Botocore. The modules include:
* Service models (e.g. the mode for S3, and other services)
* Service model extras which customize the service models
* Other mdoels associated with a service (pagination, waiters)
* Non service-specific config (Endpoint data, retry config)

Loading a module is broken down into several steps:
* Determining the path to load
* Search the data_path for files to load
* The mechanics of loading the file
* Searching for extras a applying them to the loaded file

Botocore loaders have the concept of data path exposed through AWS_DATA_PATH. This enables users to provide additional search paths where we will attempt to load models outside of the modesl we ship with botocore. When you create a loader, two paths are automatically added to the model search path:
* botocore root>/data
* ~/.aws/models

The first value is the path where all the model files shipped with
botocore are located.

The second path is so that users can just drop new model files in
``~/.aws/models`` without having to mess around with the AWS_DATA_PATH.

Directory Layout
================

The Loader expects a particular directory layout.  In order for any
directory specified in AWS_DATA_PATH to be considered, it must have
this structure for service models:

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


That is:

* The root directory contains sub directories that are the name
    of the services.
* Within each service directory, there's a sub directory for each
    available API version.
* Within each API version, there are model specific files, including (but not limited to): service-2.json, waiters-2.json, paginators-1.json

Extras allows us to process two dictionaries, the base model used by the service and extras model which is passed in for merging. Botocore compares dictionary entries in extras and makes a deep merge if the key already exists, otherwise a new entry is created.

## Conclusion
With extras as a botocore feature new API calls can be passed into the model during the loading phase. This provides the ability to make new API calls not originally part of Boto3 without making changes to the original API model. 


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

https://github.com/boto/botocore/blob/8967329dec98a23b4ebc0497c639010ae0e3ccc3/botocore/utils.py#L1479

https://boto3.amazonaws.com/v1/documentation/api/latest/index.html
