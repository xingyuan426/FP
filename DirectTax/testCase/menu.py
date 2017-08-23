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


def clr_capture(driver):
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

def clr_loader_upload(driver):
    time.sleep(1)
    driver.find_element_by_xpath(".//*[@id='msg11168']/a/span[2]").click()

def clr_search(driver):
    time.sleep(1)
    driver.find_element_by_xpath(".//*[@id='msg10135']/a/span[2]").click()
    # Select menu: Clearance -> Declaration


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

def acc_tac(driver):
    time.sleep(5)
    locator = (By.XPATH, ".//*[@id='TAC']/a/span[2]")
    WebDriverWait(driver, 10, 0.1).until(ec.visibility_of_element_located(locator))
    driver.find_element_by_xpath(".//*[@id='TAC']/a/span[2]").click()


def acc_tac_payInstruction(driver):
    time.sleep(1)
    driver.find_element_by_xpath(".//*[@id='TAC-WGT-MENU021']/a/span[2]").click()


def clr_capture_simple(driver):
    time.sleep(1)
    locator = (By.XPATH, ".//*[@id='msg10136']")
    WebDriverWait(driver, 10, 0.1).until(ec.element_to_be_clickable(locator))
    # driver.implicitly_wait(30)
    driver.find_element_by_xpath(".//*[@id='msg10136']").click()
    # Select menu: Clearance -> Declaration -> Capture a simple SAD
