# Sprint x Report (8/26/21 - 9/24/2021)

## What's New (User Facing)
 * Documentation for extending API call
 * Documentation for adding new API call
 * Documentation for publishing in Pypi
 * Added Contributions document

## Work Summary (Developer Facing)
The goal of this sprint was to familiarize ourselves with the technologies involved in creating a S3 client library. Most of our group came into this sprint will little to no knowledge of S3 as a service and the Dell ObjectScale product. It was necessary to learn about the products and then dive into the necessary components to accomplish the project. 

Each team memeber was assigned a spike as shown in the "What's New" section, and was tasked with looking into the problem and possible solutions for solving it. We researched and collected all our learnings in documentation found under the docs folder. Some members of the group attempted to put that documentation into Python code to get a better feel how the implementation might work. 

It became apparent after beginning our spike work that some of the solutions to our spikes were still going to be unclear, even after completing the documentation. The possible methods relative to each spike are difficult to test without knowing more about what other members of the groups solutions will be. 

Each member of our group learned a significant amount about boto3 and its supporting structures. We also have started to see a clearer picture of how the project implementation might occur. 


## Unfinished Work

Although the documentation for adding an API call is complete we are still unsure if either of the two methods are a sure solution. This is due to the fact that the testing for each method is incomplete. We ran out of time to completely test both methods and therefore only have an idea of a solution and some of the supporting code.

Extending the API call is also dealing with similar barriers as we have located possible solutions but are unable to confirm or deny their effectiveness. More exploration will need to go into adding and extending an API call. The documentation completed in this sprint is proof that there is progress being made towards our spikes but there is still experimentation needed to ensure that our proposed solutions are going to work in the actual library.

It is very likely that testing of the new and extended API will take place in the upcoming sprint.

## Completed Issues/User Stories
Here are links to the issues that we completed in this sprint:

Public link to project management:
https://sharing.clickup.com/14398002/l/h/7-14398002-1/044ce05e5498743

Due to this repository becoming public after the projects completetion we are using click up as our primary source of assigning and tracking issues. Click up will serve as our project management software for the duration of development. Any spikes, stories or issues assigned for the project will be posted at the link above. 
 
 ## Incomplete Issues/User Stories
 Here are links to issues we worked on but did not complete in this sprint:
 
 * https://app.clickup.com/t/30tv0jv

Progress of issue:
 https://github.com/EMCECS/objectscale-s3-client-python/blob/main/docs/newapicall/test.py
 
 The issue was not completed because of the vast amount of solutions that were considered and the difficulties that were had to set up the test environment.
 

## Code Files for Review
Please review the following code files, which were actively developed during this sprint, for quality:
 * Link to folder containing new API call documentation: https://github.com/EMCECS/objectscale-s3-client-python/tree/main/docs/newapicall
 * Contributions.md: https://github.com/EMCECS/objectscale-s3-client-python/blob/main/docs/Contributions.md
 * extendapicall.md: https://github.com/EMCECS/objectscale-s3-client-python/blob/main/docs/extendapicall.md
 * Publish.md: https://github.com/EMCECS/objectscale-s3-client-python/blob/main/docs/publish.md
 
## Retrospective Summary
Here's what went well:
  * Communication with Dell about problems that arose
  * Completion of our spikes
  * Collection of knowledge in readable md files for documentation
 
Here's what we'd like to improve:
   * Testing of documentation methods
   * More work done during weekdays
   * Better pull request communication
  
Here are changes we plan to implement in the next sprint:
   * More upfront communication about resources to use
   * More worktime during the week to correlate with Dell working hours
   * Two people taking on difficult spikes if necessary
