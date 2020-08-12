Feature: Test Calculator Functionality
    Scenario: Add cucumbers
        Given: basket has "2" cucumbers
        When: "4" cucumbers are added to basket
        Then: "6" cucumbers are left
    
    Scenario: Remove cucumbers
        Given: basket has "4" cucumbers
        When: "-3" cucumbers are removed from basket
        Then: "1" cucumber is left
