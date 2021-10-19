from behave import *
from selenium import webdriver
import time


@given('I launch Chrome browser')
def web_driver(self):
    self.driver = webdriver.Chrome()


@when('I open xenonstack career homepage')
def step_impl(self):
    self.driver.get("https://careers.neuralcompany.work/app/login")


@when('Enter user name "{user}" and password "{pwd}"')
def user_credentials(self, user, pwd):
    self.driver.find_element_by_id("tpt_loginUsername").send_keys(user)
    self.driver.find_element_by_id("tpt_loginPassword").send_keys(pwd)
    time.sleep(3)


@when('click on login button')
def login_button(self):
    self.driver.find_element_by_id("loginButton").click()
    time.sleep(2)


@when('click on start button to start the test')
def start_test(self):
    self.driver.find_element_by_xpath("//button[contains(text(),'Start Test')]").click()
    time.sleep(2)
    window_after = self.driver.window_handles[1]
    self.driver.switch_to_window(window_after)


@When('check the box')
def check_box(self):
    self.driver.find_element_by_xpath("//body/div[@id='root']/div[1]/div[1]/div[1]/section[1]/div[1]/div[1]/div["
                                      "1]/div[4]/label[1]/span[1]").click()
    time.sleep(2)


@Then('click on start test')
def start_test(self):
    self.driver.find_element_by_xpath("//body/div[@id='root']/div[1]/div[1]/div[1]/section[1]/div[1]/div[1]/div["
                                      "1]/div[5]/button[1]").click()
    time.sleep(3)
