# Created by alexandrabugaeva at 1/5/26
Feature: Tests for cart

  Scenario: User can add product to the cart
    Given Open Target main page
    When Search for dyson
    And Click on add to cart icon
    And Click Pick up button
    And Close added to cart window
    And Click on cart icon
    Then Verify dyson is added to cart