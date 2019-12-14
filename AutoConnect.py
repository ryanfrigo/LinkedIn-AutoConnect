from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.action_chains import ActionChains
from selenium import webdriver
import time
from random import uniform
from sys import argv
from getpass import getuser, getpass

driver = webdriver.Chrome()

time.sleep(uniform(1, 3))
driver.maximize_window()

time.sleep(uniform(1, 3))
driver.get('https://linkedin.com')

time.sleep(uniform(1, 3))
driver.find_element_by_class_name("nav__button-secondary").click()

time.sleep(uniform(1, 3))
username = driver.find_element_by_xpath("//input[@name='session_key']")
password = driver.find_element_by_xpath("//input[@name='session_password']")

if "--noprompt" in argv:
    username.send_keys(argv[2])
    time.sleep(uniform(1, 3))
    password.send_keys(argv[3])
    link = argv[4]
else:
    username.send_keys(input('LinkedIn email: '))
    password.send_keys(getpass('LinkedIn password: '))
    link = input("Paste link from search query: ")

time.sleep(uniform(1, 3))
driver.find_element_by_xpath("//button[@aria-label='Sign in']").click()

driver.get(link)

for i in range(0, 40):
    print(i)
    try:
        connects = driver.find_elements_by_xpath("//button[contains(@aria-label, 'Connect with ')]")

        # click connect for every connection
        for element in connects:
            time.sleep(uniform(1, 3))
            try:
                element.click()
            except:
                time.sleep(uniform(1, 3))
            driver.implicitly_wait(uniform(1, 3))
            try:
                # cick send now in connection pane
                element = driver.find_element_by_xpath("//button[contains(string(.), 'Send now')]")

                action = webdriver.common.action_chains.ActionChains(driver)
                action.move_to_element_with_offset(element, 1, 1)
                action.click()
                action.perform()
                time.sleep(uniform(1, 3))
                driver.implicitly_wait(uniform(1, 3))

                # dismiss connect pane if connection requires email
                try:
                    driver.find_element_by_xpath("//button[@aria-label='Dismiss']").click()
                except:
                    continue

            except:
                driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
                driver.find_element_by_xpath("//button[@aria-label='Next']").click()
        driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
        driver.find_element_by_xpath("//button[@aria-label='Next']").click()
        time.sleep(uniform(1, 3))
    except:
        driver.implicitly_wait(uniform(1, 3))
        driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
        driver.find_element_by_xpath("//button[@aria-label='Next']").click()
        time.sleep(uniform(1, 3))