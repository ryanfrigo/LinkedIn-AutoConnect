from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.action_chains import ActionChains
from selenium import webdriver
import time
from random import uniform
from getpass import getuser, getpass
from sys import argv

driver = webdriver.Chrome()

time.sleep(uniform(1, 3))
driver.maximize_window()

time.sleep(uniform(1, 3))
driver.get('https://linkedin.com')

time.sleep(uniform(1, 3))
driver.find_element_by_class_name("nav__button-secondary").click()

time.sleep(uniform(1, 3))
username = driver.find_element_by_xpath("//input[@name='session_key']")

if "--noprompt" in argv:
    username.send_keys(argv[2])
else:
    username.send_keys(input('LinkedIn email: '))

time.sleep(uniform(1, 3))
password = driver.find_element_by_xpath("//input[@name='session_password']")

if "--noprompt" in argv:
    password.send_keys(argv[3])
else:
    password.send_keys(getpass('LinkedIn password: '))

time.sleep(uniform(1, 3))
driver.find_element_by_xpath("//button[@aria-label='Sign in']").click()