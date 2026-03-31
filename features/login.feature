Feature: login functionality
  Scenario: user can login with valid credentials
    Given the user is on the login page
    When the user enters username "standard_user" and password "secret_sauce"
    And the user clicks the login button
    Then the user should be redirected to the inventory page

  @regression
  Scenario: user can login with invalid credentials
    Given the user is on the login page
    When the user enters wrong username "invalid_user" and password "invalid_password"
    And the user clicks the login button
    Then the user should see an error message