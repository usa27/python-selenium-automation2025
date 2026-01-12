# Created by alexandrabugaeva at 1/5/26
Feature: Tests for Target circle page

  Scenario: User can see benefit cards
    Given Open Target circle page
    When Target benefit cards are shown
    Then Verify total benefit cards are shown