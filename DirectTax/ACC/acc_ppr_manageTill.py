# Manage Till
# Including:
# Prepare Till
# Close Till
# Open Till
# Reconcile Till
import string

from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
import time

def prepareTill(driver):
    time.sleep(2)
    locator1 = (By.XPATH, ".//*[@id='form-tabs-iframeArea']/iframe[2]")
    WebDriverWait(driver, 10, 0.1).until(EC.frame_to_be_available_and_switch_to_it(locator1))
    # Switch to iframe2
    time.sleep(1)
    locator2 = (By.XPATH, ".//*[@id='row2cell1Col21139']/div")
    WebDriverWait(driver, 10, 0.5).until(EC.element_to_be_clickable(locator2))
    driver.find_element_by_xpath(".//*[@id='row2cell1Col21139']/div").click()
    # Chose the till of which id = 7, and its status is reconciled
    locator3 = (By.XPATH, ".//*[@id='tbPrepareTill']/input")
    WebDriverWait(driver, 10, 0.5).until(EC.element_to_be_clickable(locator3))
    driver.find_element_by_xpath(".//*[@id='tbPrepareTill']/input").click()
    # Click process button to enter prepare till page
    driver.switch_to.default_content()
    # switch to default iframe
    locator4 = (By.XPATH, ".//*[@id='form-tabs-iframeArea']/iframe[3]")
    WebDriverWait(driver, 10, 0.5).until(EC.frame_to_be_available_and_switch_to_it(locator4))
    print "switch successfully"
    time.sleep(5)
    locator5 = (By.XPATH, ".//*[@id='List15309']/input[1]")
    WebDriverWait(driver, 10, 0.5).until(EC.element_to_be_clickable(locator5)).send_keys("ACCOFF1")
    driver.find_element_by_xpath(".//*[@id='List15309']/input[2]").send_keys("ACCOFF1")
    # Select Cashier = ACCOFF1
    time.sleep(2)
    driver.find_element_by_xpath(".//*[@id='tbSubmit']/input").click()
    # Allocate the till to Cahier "ACCOFF1"
    time.sleep(2)
    driver.switch_to.default_content()

def openTill(driver):
    time.sleep(2)
    locator1 = (By.XPATH, ".//*[@id='form-tabs-iframeArea']/iframe[2]")
    WebDriverWait(driver, 10, 0.5).until(EC.frame_to_be_available_and_switch_to_it(locator1))
    # Switch to iframe2
    locator2 = (By.XPATH, ".//*[@id='row0cell1Col21139']/div")
    WebDriverWait(driver, 10, 0.5).until(EC.element_to_be_clickable(locator2)).click()
    # Chose the till of which id = 7, and its status is reconciled
    locator3 = (By.XPATH, ".//*[@id='tbOpenTill']/input")
    WebDriverWait(driver, 10, 0.5).until(EC.element_to_be_clickable(locator3)).click()
    # Click process button to enter open till page
    time.sleep(2)
    driver.switch_to.default_content()
    # switch to default iframe
    locator4 = (By.XPATH, ".//*[@id='form-tabs-iframeArea']/iframe[3]")
    WebDriverWait(driver, 10, 0.5).until(EC.frame_to_be_available_and_switch_to_it(locator4))
    locator5 = (By.XPATH, ".//*[@id='tbSubmit']/input")
    WebDriverWait(driver, 10, 0.5).until(EC.element_to_be_clickable(locator5)).click()
    # Open the till to Cahier "ACCOFF1"
    time.sleep(2)
    driver.switch_to.default_content()

def closeTill(driver):
    time.sleep(2)
    locator1 = (By.XPATH, ".//*[@id='form-tabs-iframeArea']/iframe[2]")
    WebDriverWait(driver, 10, 0.5).until(EC.frame_to_be_available_and_switch_to_it(locator1))
    # Switch to iframe2
    locator2 = (By.XPATH, ".//*[@id='row0cell1Col21139']/div")
    WebDriverWait(driver, 10, 0.5).until(EC.element_to_be_clickable(locator2)).click()
    # Chose the till of which id = 7, and its status is reconciled
    locator3 = (By.XPATH, ".//*[@id='tbCloseTill']/input")
    WebDriverWait(driver, 10, 0.5).until(EC.element_to_be_clickable(locator3)).click()
    # Click process button to close till
    time.sleep(2)
    driver.switch_to.default_content()
    driver.find_element_by_id("flexPopupOKMsgBtn").click()
    # switch to default iframe


def reconcileTill(driver):
    time.sleep(2)
    locator1 = (By.XPATH, ".//*[@id='form-tabs-iframeArea']/iframe[2]")
    WebDriverWait(driver, 10, 0.5).until(EC.frame_to_be_available_and_switch_to_it(locator1))
    # Switch to iframe2
    locator2 = (By.XPATH, ".//*[@id='row2cell1Col21139']/div")
    WebDriverWait(driver, 10, 0.5).until(EC.element_to_be_clickable(locator2)).click()
    # Chose the till of which id = 7, and its status is reconciled
    locator3 = (By.XPATH, ".//*[@id='tbReconcileTill']/input")
    WebDriverWait(driver, 10, 0.5).until(EC.element_to_be_clickable(locator3)).click()
    # Click process button to enter reconcile till page
    time.sleep(5)
    driver.switch_to.default_content()
    # switch to default iframe
    locator4 = (By.XPATH, ".//*[@id='form-tabs-iframeArea']/iframe[3]")
    WebDriverWait(driver, 10, 0.5).until(EC.frame_to_be_available_and_switch_to_it(locator4))
    driver.find_element_by_xpath(".//*[@id='ReconcileTab']/tbody/tr[1]/td/div/div/div/div[2]/div[2]").click()
    amount = driver.find_element_by_xpath(".//*[@id='surplusShortageAmount_listVal']/input").get_attribute("value")
    amount1 = filter(str.isdigit, amount.encode("utf-8"))
    amount2=int(amount1)/100
    # acquire shortage
    driver.find_element_by_xpath(".//*[@id='row0cell0colCash01']/div").click()
    time.sleep(2)
    frame = driver.find_element_by_class_name("fancybox-iframe")
    driver.switch_to_frame(frame)
    time.sleep(1)
    target = driver.find_element_by_xpath(".//*[@id='row0cell2record03']/div")
    driver.execute_script("arguments[0].scrollIntoView();", target)
    # scroll up to the element
    driver.find_element_by_xpath(".//*[@id='row0cell2record03']/div").click()
    driver.find_element_by_xpath(".//*[@id='NoncashActualNumDis']/input").clear()
    driver.find_element_by_xpath(".//*[@id='NoncashActualNumDis']/input").send_keys(amount2)
    driver.find_element_by_xpath(".//*[@id='tbContainer']").click()
    time.sleep(1)
    driver.find_element_by_xpath(".//*[@id='tbSave']/input").click()
    time.sleep(1)
    driver.switch_to.default_content()
    frame2 = driver.find_element_by_xpath(".//*[@id='form-tabs-iframeArea']/iframe[3]")
    driver.switch_to_frame(frame2)
    locator5 = (By.XPATH, ".//*[@id='tbSubmit']/input")
    WebDriverWait(driver, 10, 0.5).until(EC.element_to_be_clickable(locator5)).click()
    # Reconciled Till
    time.sleep(10)
    driver.switch_to.default_content()