Feature: Bpbonline login


@Bpb_login
Scenario: login and signoff for Bpbonline
    Given I am on the Bpbonline homepage
    When I Login in Bpbonloine account
    Then I signoff from Bpbonline account