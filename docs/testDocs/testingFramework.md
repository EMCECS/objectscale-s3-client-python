# Testing Framework for ObjectScale Product

The test framework we will be using for the project is Pytest. It is the same test framework used in boto3, which can provide a reference to aid in learning how to test this software. 

### Installation

This test framework can be installed through pip, using the following command:

`pip install pytest`

From here, the framework can be included in the test file. 

### Types of Testing

For this project, implementing unit tests, integration tests, and functional tests will be a necessity for ensuring quality of code. Unit tests will be preformed at a low level to ensure each component of the product is working as intended. These unit tests will be used to define specifications for product functionalities. A group member working on the project should be able to intermittently test what they are developing using the segmented unit testing suite. We will define the development process as follows: 

1. Preform a spike to gather knowledge and define segments of work for the developers to work on.
2. Create tickets/tasks with clear requirements and assign them to developers on the team.
3. A developer should be assigned to write a unit test for the task (if applicable). This test should be completed before work begins on the implementation of the task.
4. A developer should be assigned to complete the task, with the unit test aiding in informing the developer of input/output expectations.

This is the ideal development timeline. There may be cases where test development impedes or blocks implementation of functionality, and there may be cases where unit testing cannot be feasibly preformed on the given functionality. In these cases, it would be necessary to develop the functionality in lieu of unit testing guidance.

However, unit tests are still invaluable in defining and enforcing code requirements. It is important have people on the team prioritizing testing individual sections ofthe code they write.

