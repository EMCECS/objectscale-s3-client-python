# Sprint x Report (12/10/22 - 2/21/2023)

## What's New (User Facing)
 * Create Bucket call
 * Documentation for the release process
 * Defined how to extend request objects

## Work Summary (Developer Facing)
Much of the work completed during this sprint had been rolled over from the previous sprint from last semester. The create bucket call had the implementation done, however we opened a new story to try and understand how the project would create a client to handle to hook methods necessary for call extensions. Unfortunately it was ultimately discovered that hook methods are not needed to use the boto3 extensibility. The initial solution was the correct one and the further research proved what we had initially thought to be correct. 

Outside of create bucket we were able to define how the release process will take place for the library by looking into industry standards for other python libraries. A roll over from our previous sprint was defining how to extend request objects which was discussed during our weekly stand up to already have been previously completed. 


## Unfinished Work

All of the work delegated this sprint was completed. We were able to turn the page on all uncompleted stories from the previous sprint.

## Completed Issues/User Stories
Here are links to the issues that we completed in this sprint:

 * Create Bucket call [https://app.clickup.com/t/30tutyc]
 * Documentation for the release process [https://app.clickup.com/t/358r45y]
 * Defined how to extend request objects [https://app.clickup.com/t/34c2jtx]

 
 ## Incomplete Issues/User Stories

None for this sprint!

## Code Files for Review
Please review the following code files, which were actively developed during this sprint, for quality:
 * Create Bucket call [https://github.com/EMCECS/objectscale-s3-client-python/blob/main/src/main/python/service-2.sdk-extras.json]
 * Create Bucket test [https://github.com/EMCECS/objectscale-s3-client-python/blob/main/src/tests/unittests.py]
 * Documentation for the release process [https://github.com/EMCECS/objectscale-s3-client-python/blob/main/docs/publishing/publish.md]
 * Defined how to extend request objects [None - built off of extending api call story]
 
## Retrospective Summary
Here's what went well:
  * Completion of stories
  * Usage of resources (online/dell)
  * Pull request process
 
Here's what we'd like to improve:
   * Awareness about already completed stories
   * More work done during weekdays
   * Quicker replies to team members
  
Here are changes we plan to implement in the next sprint:
   * Referencing the log better when planning new sprints
   * More worktime during the week to correlate with Dell working hours
   * Checking the team discord and slack twice a day

## Demo Video Link
