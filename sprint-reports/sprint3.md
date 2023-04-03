# Sprint x Report (3/3/23 - 4/2/23)

## What's New (User Facing)
 * Metadata query
 * Documentation
 * Test publication to testpypi

## Work Summary (Developer Facing)
This sprint marked the close of our boto3 client library (other than publishing). Our final call metadata query was completed after rolling over from subsequent sprints. The call itself had some difficulting as it was the culmination of the other calls in the library. Fortunately after playing with the response shapes Nathan was able to complete the call passing the test cases that were previously written. The documentation generation proved to be a much bigger task than we had anticipated. The generation required shadowing the AWS documentation generation and then modifying the outputs to meet Dells specifications. The story unraveled in complexity but after some help from our Dell mentor was completed by the end. Publication to testpypi was repeated as in previous sprints however this time in a much more end to end fashion, ensuring that all the dependencies were met before final library publication is done.

All team members learned the importance of sprint planning as the stories all were much more work than when they were planned and pointed. 

## Unfinished Work
All work was completed and our team also began to work ahead on the .NET project, starting new stories including: extension methods, and versions to target. 

## Completed Issues/User Stories
Here are links to the issues that we completed in this sprint:

 * https://app.clickup.com/t/32dazej
 * https://app.clickup.com/t/358t181 and https://app.clickup.com/t/863g9gt2c
 * https://app.clickup.com/t/863g3rv5v
 
 ## Incomplete Issues/User Stories
 Here are links to issues we worked on but did not complete in this sprint: None

## Code Files for Review
Please review the following code files, which were actively developed during this sprint, for quality:
 * [Metadata Query](https://github.com/EMCECS/objectscale-s3-client-python/blob/main/src/main/python/service-2.sdk-extras.json#L28)
 * [Documentation - all files](https://github.com/EMCECS/objectscale-s3-client-python/tree/main/docs)
 * [Publication](https://test.pypi.org/project/obs-s3-client/)
 
## Retrospective Summary
Here's what went well:
  * Overcoming of blockers
  * Collaboration with Dell mentor
  * Time management
 
Here's what we'd like to improve:
   * More effective sprint planning
   * Pointing of stories
   * Worktime during the week
  
Here are changes we plan to implement in the next sprint:
   * Critcally assess all possible solutions and their time constraints during sprint planning
   * Point on the safe side (higher then expected)
   * Put in at least 2 hours toward the sprint during weekdays
