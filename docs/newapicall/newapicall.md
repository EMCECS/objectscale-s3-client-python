# Adding a New API Call


## Method #1

Boto3 is built atop of a library called Botocore, which is shared by the AWS CLI. Botocore provides a lower level of access to the boto3 functionality. This gives us the appropriate layer to attempt a new api call for metadata search.

The plan is to try and implement Dell's metadata search API call using botocore awsrequest AWSPreparedRequest function.
```
botocore.awsrequest.AWSPreparedRequest(method,url,headers,body,stream_output)
```
After the request is made we can use botocore awsrequst AWSResponse to collect the HTTP response. 
```
botocore.awsrequest.AWSResponse(url,status_code,headers,raw)
```

## Method #2
If the previous method proves to still be at too high of a level and incompatible with the request we are trying to make, then we will create our own complete Signature Version 4 (Python) and make a custom REST API call.

Following: 
https://docs.aws.amazon.com/general/latest/gr/sigv4-signed-request-examples.html

This documentation shows how you can create a complete Signature Version 4 and send the request. 

It is anticpated that one of these two methods will allow us to make new API calls. The intended function of our new API call is to retrieve the metadata search data structure.

-------

## Connecting AWS SDK for Python using S3 Compatible Storage

First we will explain how to set up the AWS SDK for Python (boto3) using S3 compatible storage.

The testing environment for this documentation takes place using Dell's ECS Test Drive credentials. This means that to connect our credentials to boto3 we will have to take a different approach than the standard aws credentials.

Typically boto3 configures the credentials of an aws account by searching the hidden file:

```
.aws/credentials
```
Inside this file boto3 would locate the tagged default credentials and authorize the use of our aws account.
```
[default]
aws_access_key_id=AKIAIOSFODNN7EXAMPLE
aws_secret_access_key=wJalrXUtnFEMI/K7MDENG/bPxRfiCYEXAMPLEKEY
```

However, ECS Test Drive only provides service specific credentials. We must configure the S3 credentials in a different manner.

We can create a client to work with using an object with the access keys and endpoint url gathered from ECS. This will initialize the client and later allow us to perform operations directly with the S3 bucket.

```
cred_object = {
    "aws_access_key_id": "example@ecstestdrive.emc.com",
    "aws_secret_access_key": "asdf2234k23klh2klh2klj2/example",
    "endpoint_url": "https://object.ecstestdrive.com",
}

client = boto3.client("s3", **cred_object)
```


A boto3 resource can be defined using the following:
```
import boto3
 s3 = boto3.recource('s3')
```

-------

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

https://docs.aws.amazon.com/general/latest/gr/signature-version-4.html
