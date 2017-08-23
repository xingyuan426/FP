from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
import time

def goto_is(driver):
    # driver.implicity.wait(30)
    #locator1 = (By.XPATH,".//*[@id='Field8462']/input")
    #WebDriverWait(driver,10,0.5).until(EC.element_to_be_clickable(locator1)).click()
    driver.find_element_by_id("Field8462").click()
    # go to item page
    print ("Go to item page successfully")
    time.sleep(10)

def goto_gs(driver):
    #driver.implicity.wait(30)
    locator1 = (By.XPATH, ".//*[@id='Field10996']/input")
    WebDriverWait(driver, 10, 0.5).until(EC.element_to_be_clickable(locator1)).click()
    time.sleep(10)
    # go to general segment page
    #print ("Go to general segment page successfully")