
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from common import test_data


def inputBox33(driver):
    time.sleep(2)
    locator1 = (By.XPATH,".//*[@id='Field11029']/input")
    WebDriverWait(driver, 10, 0.5).until(EC.element_to_be_clickable(locator1)).send_keys(test_data.b33)
    # Input box33 = commodity.code_sim1
	# print ("Input box33 successfully")


def inputBox42(driver):
    time.sleep(2)
    driver.find_element_by_xpath(".//*[@id='Field11213']/input").click()
    time.sleep(2)
    driver.find_element_by_xpath(".//*[@id='Field11213']/input").send_keys(test_data.b42)
    # Input box42
    # print ("Input box42 successfully")


def saveItemBtn(driver):
    time.sleep(1)
    driver.find_element_by_xpath(".//*[@id='tbSave']/input").click()
    time.sleep(10)
    # print ("Save successfully")
    # Click save button on Item page

def gotoGeneralSeg(driver):
    locator1 = (By.XPATH, ".//*[@id='Field10996']/input")
    WebDriverWait(driver, 10, 0.5).until(EC.element_to_be_clickable(locator1)).click()
    time.sleep(10)
    # go to general segment page
    # print ("Go to general segment page successfully")

def saveItemSimpleSad(driver):
    inputBox33(driver)
    inputBox42(driver)
    saveItemBtn(driver)
    gotoGeneralSeg(driver)

