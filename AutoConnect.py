from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.action_chains import ActionChains
from selenium import webdriver
import time
from random import uniform
from sys import argv

if "--noprompt" in argv:
    link = argv[2]
else:
    link = input("Paste link from search query: ")

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
                # cick send now in connection pain
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