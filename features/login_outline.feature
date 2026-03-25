Feature: Login with multiple users

  Scenario Outline: user can login with valid credentials
    Given the user is on the login page for outline
    When the user enters username "<username>" and password "<password>" for outline
    And the user clicks the login button for outline
    Then the result should be "<result>"

  Examples:
    | username       | password      | result              |
    | standard_user  | secret_sauce  | success             |
    | wrong_user     | wrong_sauce   | error_message       |
    