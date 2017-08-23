
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from common import test_data


def input_box33(driver):
    time.sleep(2)
    locator1 = (By.XPATH,".//*[@id='Field11029']/input")
    WebDriverWait(driver, 10, 0.5).until(EC.element_to_be_clickable(locator1)).send_keys(test_data.b33)
    #Input box33 = commodity.code_sim1
	#print ("Input box33 successfully")

def input_box42(driver):
    time.sleep(2)
    driver.find_element_by_xpath(".//*[@id='Field11213']/input").click()
    time.sleep(2)
    driver.find_element_by_xpath(".//*[@id='Field11213']/input").send_keys(test_data.b42)
    # Input box42
    #print ("Input box42 successfully")