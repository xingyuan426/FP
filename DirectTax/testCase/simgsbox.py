import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from common import test_data

def seg_movement(driver):
    time.sleep(10)
    #driver.implicit.wait(30)
    locator1 = (By.XPATH, ".//*[@id='form-tabs-iframeArea']/iframe[2]")
    WebDriverWait(driver, 10, 0.5).until(EC.frame_to_be_available_and_switch_to_it(locator1))
    locator2 = (By.XPATH, ".//*[@id='Con7631']/tbody/tr[1]/td/div/div/div/div[2]/div[2]")
    WebDriverWait(driver, 10, 0.5).until(EC.element_to_be_clickable(locator2)).click()
    #driver.find_element_by_xpath(".//*[@id='Con7631']/tbody/tr[1]/td/div/div/div/div[2]/div[2]").click()
    # Switch to Movement Label
def input_box18(driver):
    locater1 = (By.XPATH, ".//*[@id='Field8969']/input")
    WebDriverWait(driver, 10,0.5).until(EC.element_to_be_clickable(locater1)).send_keys(test_data.b18)
    # Input box18 = test abc