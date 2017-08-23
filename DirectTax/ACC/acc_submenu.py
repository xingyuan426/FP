from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.support.wait import WebDriverWait
import time



def acc_ppr_till(driver):
    time.sleep(1)
    locator = (By.XPATH, ".//*[@id='PPRMENU033']/a/span[2]")
    WebDriverWait(driver, 10, 0.1).until(ec.visibility_of_element_located(locator))
    # driver.implicitly_wait(30)
    driver.find_element_by_xpath(".//*[@id='PPRMENU033']/a/span[2]").click()
    # Select menu: Accounting -> Payment processing -> Tills
    time.sleep(2)

def acc_ppr_payment(driver):
    time.sleep(1)
    driver.find_element_by_xpath(".//*[@id='PPRMENU034']/a/span[2]").click()
    # Select menu: Accounting -> Payment processing -> Payments



def acc_tac_payInstruction(driver):
    time.sleep(1)
    driver.find_element_by_xpath(".//*[@id='TAC-WGT-MENU021']/a/span[2]").click()

