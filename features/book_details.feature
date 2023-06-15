Feature: Book Details
  As a user
  I want to retrieve the details of a book by its ID
  So that I can view the book's information

  Scenario: Retrieve book details by ID
    Given I have a book ID "12345"
    When I request the book details
    Then the response status code should be 200
    And the response should contain the following book details:
      | title     | author    | category | price |
      | Book Title| Author Name  | Fiction  | 19.99 |