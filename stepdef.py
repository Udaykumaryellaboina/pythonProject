from selenium import webdriver
import os
from configparser import ConfigParser
from selenium.webdriver.common.keys import Keys
import webdriver
import os
from configparser import ConfigParser
from selenium.webdriver.common.keys import Keys
import time
from behave import given, when, then


@given('I am on the Bpbonline homepage')
def step(context):
    context.helperfunc.open('https://lambdatest.github.io/sample-todo-app/')
    context.helperfunc.maximize()

@when('I Login in Bpbonloine account')
def enter_item_name(context):
    context.helperfunc.find_by_id('sampletodotext').send_keys("Yey, Let's add it to list")

@then('I signoff from Bpbonline account')
def click_on_checkbox_one(context):
    context.helperfunc.find_by_name('li1').click()
    context.helperfunc.find_by_name('li2').click()
