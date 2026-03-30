Feature: search for products

  Scenario: user can search for a product
    Given the user is on the wikipedia page
    When the user enters "selenium" in the search bar
    Then the search results should display products related to "selenium"