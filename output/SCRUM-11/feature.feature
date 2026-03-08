Feature: Login to Sauce Demi Web Application

  Scenario: Successful login with valid credentials
    Given I am on the login page of the Sauce Demi Web Application
    When I enter valid username "standard_user" and valid password "secret_sauce"
    And I click on the login button
    Then I should be redirected to the dashboard
    And I should see a success message "Welcome to the Sauce Demi Application!"

  Scenario: Unsuccessful login with invalid credentials
    Given I am on the login page of the Sauce Demi Web Application
    When I enter invalid username "invalid_user" and invalid password "wrong_password"
    And I click on the login button
    Then I should see an error message "Invalid username or password."

  Scenario: Unsuccessful login with empty credentials
    Given I am on the login page of the Sauce Demi Web Application
    When I enter empty username and empty password
    And I click on the login button
    Then I should see an error message "Username and password cannot be empty."