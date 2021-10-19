Feature: career portal Login

  Scenario Outline:  Login to xenonstack with Multiple parameters
    Given I launch Chrome browser
    When I open xenonstack career homepage
    And Enter user name "<username>" and password "<password>"
    And click on login button
    And click on start button to start the test
    And Check the box
    Then click on start test

    Examples:
      | username                   | password         |
      | lucky@xenonstack.com       | Luckyshukla@123* |
      | luckyshuklakunda@gmail.com | Lucky@123        |