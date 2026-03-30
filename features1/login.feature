Feature: login functionality tests
  Scenario: i can login with valid credentials
    Given im on the login page
    When i enters username "standard_user" and password "secret_sauce"
    And i clicks the login button
    Then i should be redirected to the inventory page
  
  Scenario: invalid login
    Given im on the login page interface
    When i enters wrong username "invalid_user" and password "invalid_password"
    And i click on the login button