# Steps for publishing library
## 1: Validating upstream changes
Manually check botocore [library](https://github.com/boto/botocore/blob/develop/botocore/data/s3/2006-03-01/service-2.json) for any changes in relation to the createbucketrequest shape. The process for manual verification is listed below.

### Process for manual verifcation
#### Step 1: Look at change history
Using githubs History tab located at the top of the [page](https://github.com/boto/botocore/blob/develop/botocore/data/s3/2006-03-01/service-2.json), view the commit history of the service-2.json file. 

VERIFCATION DATE: Oct. 19, 2022
If there is no new change history AFTER Oct. 19, 2022, please skip steps as library has already been validated.

#### Step 2: Read .changes/ files
Developers on the botocore project document changes using the .changes directory and therefore any changes within this commit should be documented under there. Looking through the changes made to the .changes directory, locate any change log titled "s3" (i.e, .changes/next-release/api-change-s3-89290.json). Read the description for anything pertaining the createbucketrequest call. If there's a change regarding the structure of the shape of the createbucketrequest call, then changes must be made to the source code of the library. If no change regarding the createbucketrequest call, then manual verification is complete and the verifcation date above can be updated to said commit date.
### End process for manual verification 

## 2: Make sure all tests are passing
All tests suites should be passing before final publication. This includes all types of testing (e.g. unit, integration, etc.). 

## 3: Review/merge any outstanding pull requests
All pull requests should be reviewed and merged before final publication of the library. Before any pull request is merged, developers should see if all new and existing test cases are all passing. After successful merge, all developers on the project should clean up their respective branches to keep the repository clean. 

## 4: Increment version number
Please review the publishPyPi.md file "Versioning" section for instructions on how to increment version number properly. 

## 5: Publish on PyPi
Please review the publishPyPi.md file for instructions on how to publish the library on PyPi.

## 6: Release Notes
Create a relase notes markdown document with the version number for the file name (e.g. 0-1-2.md for version 0.1.2) under the docs/releasenotes directory. 

