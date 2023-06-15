Feature: Negative Testing
  As a user
  I want to perform negative testing to ensure the API handles invalid requests properly
  So that I can verify error handling and response behavior

  Scenario: Missing parameters in the request
    When I make a request with missing parameters
    Then the response status code should be 400
    And the response should contain an appropriate error message

  Scenario: Incorrect authentication
    When I make a request with incorrect authentication
    Then the response status code should be 401
    And the response should contain an appropriate error message