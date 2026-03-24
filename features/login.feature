Feature: login functiopnality

  Scenario: user can login with valid credentials
    Given the user is on the login page
    When the user enters valid credentials
    And clicks the login button
    Then the user should be redirected to the dashboard