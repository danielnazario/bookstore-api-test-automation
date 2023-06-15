Feature: Error Handling
  As a user
  I want to verify that appropriate error messages and status codes are returned
  So that I can handle errors gracefully in my application

  Scenario: Invalid book ID
    Given I have an invalid book ID
    When I request the book details
    Then the response status code should be 404
    And the response should contain an appropriate error message

  Scenario: Invalid category ID
    Given I have an invalid category ID
    When I request the category details
    Then the response status code should be 404
    And the response should contain an appropriate error message