# get_search_metadata

## How to use call
```
client.create_bucket(Bucket='mybucket', CreateBucketConfiguration={'LocationConstraint': 'us-west-2'}, SearchMetaData='Size,CreateTime,LastModified,x-amz-meta-STR;String,x-amz-meta-INT;Integer')

res = client.get_search_metadata(Bucket='mybucket')
print(res)
```