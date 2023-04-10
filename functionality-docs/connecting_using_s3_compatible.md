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