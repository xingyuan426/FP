from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.support.wait import WebDriverWait
import time


def clr_declaration_search(driver):
    time.sleep(1)
    driver.find_element_by_xpath(".//*[@id='msg10135']/a/span[2]").click()
    # Select menu: Clearance -> Declaration

def clr_declaration_simple(driver):
    time.sleep(1)
    locator = (By.XPATH, ".//*[@id='msg10136']")
    WebDriverWait(driver, 10, 0.1).until(ec.element_to_be_clickable(locator))
    # driver.implicitly_wait(30)
    driver.find_element_by_xpath(".//*[@id='msg10136']").click()
    # Select menu: Clearance -> Declaration -> Capture a simple SAD


def clr_loader_upload(driver):
    time.sleep(1)
    driver.find_element_by_xpath(".//*[@id='msg11168']/a/span[2]").click()


