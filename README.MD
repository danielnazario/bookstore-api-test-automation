# Public API Test Automation

This project contains automated tests for the public API of a fictional online bookstore. The tests are designed to verify the functionality and reliability of the API.

## Features

- Retrieve book details by ID
- Validate response format and structure
- Perform negative testing for error scenarios
- Verify search results accuracy
- Test error handling and status codes
- Assess API performance and responsiveness

## Installation

1. Clone the repository:
```
git clone <repository_url>
```
2. Navigate to the project directory:
```  
cd bookstore-api-test-automation
```
3. Install the dependencies:
```
pip install -r requirements.txt
```

## Usage

1. Set the base URL and the credentials of the API in the `config.ini` file.

2. Execute the automated tests:
```
behave
```
The tests will be executed, and the results will be displayed in the terminal.


## Approach and Design:

In this Public API Test Automation project, the approach is to use behavior-driven development (BDD) using the Behave framework with Python. BDD promotes collaboration between stakeholders, testers, and developers by enabling clear communication through scenarios written in a natural language format. The project follows a modular and structured design, separating concerns into different files and folders.

Design Patterns:

Factory Design Pattern: The Factory Design Pattern is used to create instances of the Book and Category models. It provides a centralized way to create objects and allows for flexibility in object creation.
Frameworks and Libraries:

Behave: Behave is a Python BDD framework that helps in writing human-readable test scenarios. It uses the Gherkin syntax for writing feature files and supports step definitions to implement the test steps.

Requests: The Requests library is used for making HTTP requests to the API. It simplifies the process of sending requests, handling responses, and working with JSON data.

configparser: The configparser library is used to read the config.ini file, which stores the configuration settings such as the base URL of the API.

datetime: The datetime library is utilized to generate timestamps for measuring the performance of API requests.

logging: The logging module is used for logging informational and error messages during the test execution. It helps in debugging and tracking the test execution flow.

The project follows best practices for test automation, including proper documentation, naming conventions, and code readability. The use of modular code structure, design patterns, and appropriate libraries promotes maintainability, reusability, and scalability of the test suite.

Overall, the approach focuses on delivering reliable, maintainable, and extensible automated tests for the public API, ensuring that it behaves as expected and meets the specified requirements.