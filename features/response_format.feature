Feature: Response Format
  As a user
  I want to ensure that the API response has the expected format and structure
  So that I can correctly process the data

  Scenario: Verify the format of book search response
    Given I have a book search query "Harry Potter"
    When I search for books
    Then the response status code should be 200
    And the response should have the correct format for book search

  Scenario: Verify the format of category response
    Given I have a category ID "123"
    When I request the category details
    Then the response status code should be 200
    And the response should have the correct format for category details