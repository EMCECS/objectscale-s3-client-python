# Sprint x Report (1/23/23 - 3/2/23)

## What's New (User Facing)
 * Get search metadata
 * Disable search metadata
 * Get search system metadata
 * Metadata query
 * Library convenience

## Work Summary (Developer Facing)
This sprint consisted of a large part of our developer facing implementation. Drayer and Nathan completed the new metadata calls to handle searching, disabling, getting, and querying. All calls were made possible using the boto3 extras file extensibility. The process of configuring new json request and response objects is very tedious however all calls ultimately were completed to the specifications of Dell's documentation. Killian focused on making the library usability convenient. Our users should be able to use our library without adding any additional logic to their code. Killian was able to develop a way to encapsulate our extensions into the package so that they are loaded during installation. 

The largest road block was making the library use convenient. This particular spike had been overlooked for a majority of our development and was a issue that needed to be addressed. Killian had some difficultly locating a solution but ultimately the implementation was trivial. Constructing proper json shapes also proved to be a difficult process of trial and error but again this was still completed. 


## Unfinished Work

All of the work delegated this sprint was completed. This was the largest set of user facing development that we finished and nothing will be continued further.

## Completed Issues/User Stories
Here are links to the issues that we completed in this sprint:

 * Get search metadata [https://app.clickup.com/t/32daze8]
 * Disable search metadata [https://app.clickup.com/t/32dazd8]
 * Get search system metadata [https://app.clickup.com/t/32dazaf]
 * Metadata query [https://app.clickup.com/t/32dazej]
 * Library convenience [https://app.clickup.com/t/8669cdqyn]

 
 ## Incomplete Issues/User Stories

None for this sprint!

## Code Files for Review
Please review the following code files, which were actively developed during this sprint, for quality:
 * Get search metadata [https://github.com/EMCECS/objectscale-s3-client-python/blob/main/src/main/python/service-2.sdk-extras.json]
 * Disable search metadata [https://github.com/EMCECS/objectscale-s3-client-python/blob/main/src/main/python/service-2.sdk-extras.json]
 * Get search system metadata [https://github.com/EMCECS/objectscale-s3-client-python/blob/main/src/main/python/service-2.sdk-extras.json]
 * Metadata query [https://github.com/EMCECS/objectscale-s3-client-python/blob/main/src/main/python/service-2.sdk-extras.json]
 * Library convenience [https://github.com/EMCECS/objectscale-s3-client-python/tree/KG_LoaderExtension]
 
## Retrospective Summary
Here's what went well:
  * Completion of stories
  * Collaboration to swarm on spike
  * Comprehension of stories
 
Here's what we'd like to improve:
   * Time to complete spikes
   * More work done during weekdays
   * Communicate road blocks more effectively
  
Here are changes we plan to implement in the next sprint:
   * Critically plan the implementation before writing the code
   * More worktime during the week to correlate with Dell working hours
   * Notify team members when a road block occurs after trying logical solutions

## Demo Video Link
https://youtu.be/oYyYATE0QOY