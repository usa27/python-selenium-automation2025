# Created by alexandrabugaeva at 1/4/26
Feature: Tests for Sign In

  Scenario: User can navigate to Sign In
    Given Open Target main page
    When Click on Account
    And Click on Sign In
    Then Sign In form opened