Feature: Search Results
  As a user
  I want to search for books or categories
  So that I can find specific items of interest

  Scenario: Search for books by query
    Given I have a book search query "Harry Potter"
    When I search for books
    Then the response status code should be 200
    And the response should contain search results for books

  Scenario: Search for categories by query
    Given I have a category search query "Fiction"
    When I search for categories
    Then the response status code should be 200
    And the response should contain search results for categories