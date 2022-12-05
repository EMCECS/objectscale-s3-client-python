# Testing Framework for ObjectScale Product

The test framework we will be using for the project is Pytest. It is the same test framework used in boto3, which can provide a reference to aid in learning how to test this software. 

### Installation

This test framework can be installed through pip, using the following command:

`pip install pytest`

From here, the framework can be included in the test file.
Another library to use could be unittest. This comes standard to python, so no installation is necessary.

### Types of Testing

For this project, implementing unit tests, integration tests, and functional tests will be a necessity for ensuring quality of code. Unit tests will be preformed at a low level to ensure each component of the product is working as intended. These unit tests will be used to define specifications for product modules. A group member working on the project should be able to intermittently test what they are developing using the modularized unit testing suite. We will define the development process as follows: 

1. Preform a spike to gather knowledge and define segments of work for the developers to work on.
2. Create tickets/tasks with clear requirements and assign them to developers on the team.
3. A developer should be assigned to write a unit test for the task (if applicable). This test should be completed before work begins on the implementation of the task.
4. A developer should be assigned to complete the task, with the unit test aiding in informing the developer of input/output expectations.

This is the ideal development timeline. There may be cases where test development impedes or blocks implementation of functionality, and there may be cases where unit testing cannot be feasibly preformed on the given functionality. In these cases, it would be necessary to develop the functionality in lieu of unit testing guidance.

However, unit tests are still invaluable in defining and enforcing code requirements. It is important have people on the team prioritizing testing individual sections of the code they write.

Integration tests will be used to check interactions between modules. These must be done before a set of functionalities (for a sprint, for instance) is completed. These will ensure independent components of the project function together as intended, so requirements can be guarenteed to be realized as specified in the task descriptions.

A few functional tests will need to be implemented to test the full use cases of the project. Not many will be needed, as the top-level functionalities of the library are limited in scope. These will however still be necessary to prove the fulfillment of the project requirements. As the project does not have straightforward front-facing demonstrability, these tests will be one of the best means for demonstraiting project fulfillment.

### Testing Implementation

Individual portions of functionality can be organized into separate test classes. These classes can have their own SetUp and TearDown functions for the specific part of the code that they are testing. They can be defined as follows:

`class SampleTestClass(unittest.TestCase)`

There are three levels of test infrastructure, that being test module, test class, and test method. The tests we write can be ran at each of these levels. To run a test module, the following command can be used:

`python -m unittest <moduleName>`

Likewise, to run test classes and methods the following commands can be used respectively:

`python -m unittest <moduleName>.<className>`
`python -m unittest <moduleName>.<className>.<methodName>`

The parts of the tests that will be confirming functionality are the assert statements. These check the validity of certain statements. Templates for these statements is shown here:

`assert <condition>`
`self.assertEqual(<condition>)`

They will throw assertion errors on a failure, which will be uset to tell if the test was successful. To customize the grouping of tests, one can use a test suite. A test suite can be instantiated as `unittest.TestSuite()` and tests can be added to the suite using the `suite.addTest()` method.

On observing the testing implementation for boto3, it appears to be beneficial to use unittests Mock class to test how different methods have been used. To generate a mock object of a function or class, the following can be invoked:

`object = mock.Mock()`

The object will be converted to a mock object, where data of how the mock is used can be stored. As actions are performed with the mock object, data about these actions can be used in assertions, like the following assertion:

`object.assert_called()`

This assertion succeeds when the mock object has been called at least once. There are also assertions confirming the number of times the moack was called and the specific parameters with which they were called.