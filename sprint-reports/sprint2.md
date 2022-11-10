# Sprint 2 Report (10/09/22 - 11/09/2022)

## What's New (User Facing)
 * Proof of concept for extending api call
 * Proof of concept for adding api call
 * Boto3 added as a project dependency

## Work Summary (Developer Facing)
We utilize an agile framework for project management and perform two week sprints. During these sprints each memember is deligated a spike or story and is to finish that spike by the end of the sprint. We meet weekly so there is a midsprint check in to make sure all barriers are overcome. The largest barrier for the whole project thus far is determining how we could make modifications to the boto3 library while only changing the bare minimum amount of the source code. Fortunately this sprint we were able to overcome this by making use of boto3 extras. A JSON file that allows us to dynamically merge changes to the existing boto3 API calls. 

We now have a direction and were able to complete a couple of our larger spikes due to this break through. We were able to learn about the extensibility possibilities within boto3 and also explored the underlying mechanisms behind boto3 as a project dependency. All this was accomplished through a lot of research and extensive testing for a proof of concepts demo for each spike. 

## Unfinished Work
We were able to get a large part of the publishing to pypi work done however the process needs to be finalized and this will be taking place during our next sprint. The spike had been completed but not to the level of specification that was needed. For the publishing process to be marked completed it needs to have every criteria in the document correct and verified. 

This wil be completed in sprint three.

Outside of this one spike all other spikes have been completed during this sprint. 

## Completed Issues/User Stories
Here are links to the issues that we completed in this sprint:

 * https://app.clickup.com/t/30tutj3
    
 * https://app.clickup.com/t/30tutx1

 * https://app.clickup.com/t/30tuypd
 
 ## Incomplete Issues/User Stories
 Here are links to issues we worked on but did not complete in this sprint:
 
 * https://app.clickup.com/t/30tutyg

This issue was not completed because we did not fully understand or meet the acceptance criteria.

Note: it was marked complete but Dell has instructed us this it is not complete. However a new spike was written for it to be completed the next sprint.


## Code Files for Review
Please review the following code files, which were actively developed during this sprint, for quality:
 * [extendapicall](https://github.com/EMCECS/objectscale-s3-client-python/tree/main/docs/extendapicall)
 * [newapicall](https://github.com/EMCECS/objectscale-s3-client-python/tree/main/docs/newapicall)
 * [boto3dependency](https://github.com/EMCECS/objectscale-s3-client-python/tree/main/docs/boto3dependency)
 
## Retrospective Summary
Here's what went well:
  * We worked during the week much more actively
  * Communication with Dell employees greatly improved
  * Locating solutions to spikes was more effective
 
Here's what we'd like to improve:
   * More diversity of work being done by individual
   * Completion of spikes before weekend
   * Collaborating with team members more frequently
  
Here are changes we plan to implement in the next sprint:
   * Change spikes to different type of work for each individual
   * More questions asked within our WSU team memebers
   * Working hours spread out through week (1 hour a day)

Link to sprint Kaizen: https://app.clickup.com/t/34htdg6

Link to Sprint 2 Demo video: https://youtu.be/ETwf5DlvGZg 