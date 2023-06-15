Feature: Performance Testing
  As a user
  I want to assess the performance and responsiveness of the API under different loads
  So that I can ensure it meets the required performance standards

  Scenario: Execute Concurrent Requests
    Given I have a book with ID "123"
    And I have a list of concurrent requests for "5" concurrent users
    When I execute the concurrent requests
    Then the requests should complete within "2" seconds