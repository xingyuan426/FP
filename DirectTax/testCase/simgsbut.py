
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait


def gs_save(driver):
    time.sleep(1)
    driver.find_element_by_xpath(".//*[@id='tbSave']/input").click()
    time.sleep(10)
    # print ("Save successfully")
    # Click save button on GS page

def gs_assess(driver):
    time.sleep(1)
    locator1 = (By.XPATH,".//*[@id='tbAssess']/input")
    WebDriverWait(driver, 10,0.5).until(EC.element_to_be_clickable(locator1)).click()
    time.sleep(10)
    # print ("Assess successfully")
    # Click assess button on GS page


def gs_register(driver):
    time.sleep(1)
    locator1 = (By.XPATH,".//*[@id='tbRegister']/input")
    WebDriverWait(driver, 10,0.5).until(EC.element_to_be_clickable(locator1)).click()
    time.sleep(20)
    #print ("Register successfully")
    # Click assess button on GS page