# Created by alexandrabugaeva at 1/4/26
Feature: Tests for search

  Scenario: User can search for a tea on Target
    Given Open Target main page
    When Search for tea
    Then Search results for tea are shown

  Scenario: User can click on cart icon
    Given Open Target main page
    When Click on cart icon
    Then Empty cart message is shown
