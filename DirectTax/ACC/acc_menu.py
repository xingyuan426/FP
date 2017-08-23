from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.support.wait import WebDriverWait
import time


def acc_ppr(driver):
    time.sleep(8)
    locator = (By.XPATH, ".//*[@id='PPR']/a/span[2]")
    WebDriverWait(driver, 10, 0.1).until(ec.element_to_be_clickable(locator))
    #driver.implicitly_wait(30)
    driver.find_element_by_xpath(".//*[@id='PPR']/a/span[2]").click()
    # Select menu: Accounting -> Payment processing

def acc_tac(driver):
    time.sleep(5)
    locator = (By.XPATH, ".//*[@id='TAC']/a/span[2]")
    WebDriverWait(driver, 10, 0.1).until(ec.visibility_of_element_located(locator))
    driver.find_element_by_xpath(".//*[@id='TAC']/a/span[2]").click()


