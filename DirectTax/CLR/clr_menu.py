from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.support.wait import WebDriverWait
import time





def clr_declaration(driver):
    time.sleep(5)
    locator = (By.XPATH, ".//*[@id='menu112']")
    WebDriverWait(driver, 10, 0.1).until(ec.element_to_be_clickable(locator))
    #driver.implicitly_wait(30)
    driver.find_element_by_xpath(".//*[@id='menu112']").click()
    # Select menu: Clearance -> Declaration


def clr_loader(driver):
    time.sleep(5)
    locator = (By.XPATH, ".//*[@id='menu114']/a/span[2]")
    WebDriverWait(driver, 10, 0.1).until(ec.element_to_be_clickable(locator))
    driver.find_element_by_xpath(".//*[@id='menu114']/a/span[2]").click()
    # Select menu: Clearance -> Loader
