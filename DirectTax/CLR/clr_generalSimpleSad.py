import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from common import test_data


def movementLabel(driver):
    time.sleep(10)
    # driver.implicit.wait(30)
    locator1 = (By.XPATH, ".//*[@id='form-tabs-iframeArea']/iframe[2]")
    WebDriverWait(driver, 10, 0.5).until(EC.frame_to_be_available_and_switch_to_it(locator1))
    # Switch to frame[2]
    locator2 = (By.XPATH, ".//*[@id='Con7631']/tbody/tr[1]/td/div/div/div/div[2]/div[2]")
    WebDriverWait(driver, 10, 0.5).until(EC.element_to_be_clickable(locator2)).click()
    # driver.find_element_by_xpath(".//*[@id='Con7631']/tbody/tr[1]/td/div/div/div/div[2]/div[2]").click()
    # Switch to Movement Label


def inputBox18(driver):
    locater1 = (By.XPATH, ".//*[@id='Field8969']/input")
    WebDriverWait(driver, 10, 0.5).until(EC.element_to_be_clickable(locater1)).send_keys(test_data.b18)
    # Input box18 = test abc


def saveGeneralBtn(driver):
    time.sleep(1)
    driver.find_element_by_xpath(".//*[@id='tbSave']/input").click()
    time.sleep(10)
    # print ("Save successfully")
    # Click save button on GS page

def gotoItemSeg(driver):
    # driver.implicity.wait(30)
    #locator1 = (By.XPATH,".//*[@id='Field8462']/input")
    #WebDriverWait(driver,10,0.5).until(EC.element_to_be_clickable(locator1)).click()
    driver.find_element_by_id("Field8462").click()
    # go to item page
    print ("Go to item page successfully")
    time.sleep(10)

def saveGeneralSimpleSad(driver):
    movementLabel(driver)
    inputBox18(driver)
    saveGeneralBtn(driver)
    gotoItemSeg(driver)
