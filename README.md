# objectscale-s3-client-python
ObjectScale S3 Client for Python (based on boto3)

Link to Project Management Software: https://app.clickup.com/14398002/v/l/7-14398002-1

## Project summary

This is a library developed for Dell Technologies extending the boto3 Python library for metadata search calls.

The library takes existing S3 API calls designed for boto3 and implements new search indexes for metadata search functionality. It also generates new S3 API calls with metadata search functionality.

## Installation

The library will be accessible through PyPI. Project information can be seen here:

<https://pypi.org/project/objectscale-s3-client/>

### Prerequisites

Python is neccessary to have installed before using the library. The project will function with Python versions past Python 3.9. If the user wants to contribute to the project, Git will also be neccessary. As this library extends the existing boto3 and botocore libraries, these are also necessary prerequisites.

### Installation Steps

The package can be installed through pip, which comes with the installation of Python. Installation of the package can be done by simply executing the following command:

`pip install objectscale-s3-client`

## Functionality

The project can be used by adding the following include to the project:

`from objectscale-s3-client import botocore`

From here an s3 client can be created using boto3 and the added calls will be used. Metadata search indicies have been added to the create bucket call and the metadata search call is accessible. A user can also get the metadata search indicies and disable metadata search on a bucket.


## Known Problems

* Disable metadata search is broken due to issues with the Dell API 


## Contributing

Contributions to the project are welcomed. Outline of steps for contributions are given below:

1. Create a new GitHub issue or find one to work on
2. Assign the issue to yourself
3. Fork project, make changes, get reviewed by Dell project maintainer
4. DCO sign off

Additional details for these requirements can be found in the `CONTRIBUTING.md` file in the project repository.

## Additional Documentation

The documentation module Sphinx was used for documenting the code. This documentation can be accessed through the earlier linked github code.

## How to Generate Documentation
The documentation can be generated using the following script. 

```
git checkout gh-pages
git rm -rf .
git checkout main -- docs

make html

git add .
git commit -s -m "updated docs"
git push
```
The script checks out the orphan gh-pages branch, removes all existing files, then copies the updated docs in the main branch. "make html" generates the new documentation and the final commands push the updates to github. 

## License

This project uses the Apache License. The license can be viewed in the `LICENSE` file in the project repository.

## Finding Dependencies of package
1. install objectscale python package using pip install
2. install pipdeptree using pip install
3. run command 'pipdeptree -p obs-s3-client'
4. dependency tree should be displayed
