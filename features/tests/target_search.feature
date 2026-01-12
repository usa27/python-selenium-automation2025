# Created by alexandrabugaeva at 1/4/26
Feature: Tests for search

  Scenario: User can search for a product on Target
    Given Open Target main page
    When Search for teapot
    Then Search results for teapot are shown

  Scenario: User can click on cart icon
    Given Open Target main page
    When Click on cart icon
    Then Empty cart message is shown

  Scenario Outline: User can search for different products on Target
    Given Open Target main page
    When Search for <product>
    Then Search results for <expected_product> are shown
    Examples:
    |product  |expected_product  |
    |coffee   |coffee            |
    |mug      |mug               |
    |sweater  |sweater           |
