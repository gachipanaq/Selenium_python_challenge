# Created by gherard at 8/10/2021
Feature: login

  Scenario: Login to Saucedemo with valid parameters
    Given I launch Chrome browser
    When I open saucedemo home page
    And Enter username "standard_user" y password "secret_sauce"
    And Click on login button
    Then User must successfully login to the form page

  Scenario Outline: Login to Saucedemo with valid parameters
    Given I launch Chrome browser
    When I open saucedemo home page
    And Enter username "<username>" y password "<password>"
    And Click on login button
    Then User must successfully login to the form page

    Examples:
      | username                | password     |
      | locked_out_user         | secret_sauce |
      | problem_user            | secret_sauce |
      | performance_glitch_user | secret_sauce |
