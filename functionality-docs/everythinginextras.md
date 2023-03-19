# Botocore Loaders

This document will explore the limits of extensibility possible with the botocore loaders.

## Custom Search Path
The default search path of the botocore loader is as follows:

    * <botocore root>/data/
    * ~/.aws/models

The first value is the path where all the model files shipped with botocore are located

The second path is so the users can drop new model files in that desintation. 


1. 
    We can extend the search path using:
    ```
    session = boto3.Session()
    session._loader.search_paths.extend(["/tmp/boto"])
    ```

    The directory structure of /tmp/boto needs to follow the resource loader documentation, but this shows that we can add a custom search path. 

2. 
    Boto3 also allows setting the AWS_DATA_PATH environment variable which can point to a directory path of your choice.

    This solution is better than fetching models from S3 during runtime, unpacking and modifying session parameters.

## Alternative loaders
Alternative loaders can be swapped in using:
```
Session.register_component
```

## Extras Processing
```
def deep_merge(base, extra):
    """Deeply two dictionaries, overriding existing keys in the base.
    :param base: The base dictionary which will be merged into.
    :param extra: The dictionary to merge into the base. Keys from this
        dictionary will take precedence.
    """
    for key in extra:
        # If the key represents a dict on both given dicts, merge the sub-dicts
        if (
            key in base
            and isinstance(base[key], dict)
            and isinstance(extra[key], dict)
        ):
            deep_merge(base[key], extra[key])
            continue

        # Otherwise, set the key on the base to be the value of the extra.
        base[key] = extra[key]
```
The extras processing occurs by simply merging two python dictionaries.

We can already:
* add shapes
* extend shapes