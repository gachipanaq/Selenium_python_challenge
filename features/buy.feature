# Created by gherard at 8/10/2021
Feature: buy

  Background: common steps
    Given I launch browser
    When I open application
    And Enter username "standard_user" and password "secret_sauce"
    And Click on login
    And Navigate to buy page

  Scenario: Buy Unit
    And Add cart
    And Checkout cart
    And Enter information
    And Checkout overview
    When Checkout complete
    Then Logout

  Scenario: Buy More
    And Add more cart
    And Checkout cart
    And Enter information
    And Checkout overview
    When Checkout complete
    Then Logout