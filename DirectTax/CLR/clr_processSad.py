# coding=utf-8

import time
import os
from common import test_data


def processSadBtn(driver):
    driver.find_element_by_xpath(".//*[@id='Tbl7658']/div[2]/div/div[2]/table/tbody/tr").click()
    # Chose a record
    time.sleep(1)
    driver.find_element_by_xpath(".//*[@id='tbProcess']/input").click()
    # Click process button
    time.sleep(10)
    driver.switch_to.default_content()
    # Wait for 10 seconds until the page opened


def paySimpleSad(driver):
     driver.switch_to.default_content()
     frame = driver.find_element_by_xpath(".//*[@id='form-tabs-iframeArea']/iframe[3]")
     driver.switch_to_frame(frame)
     driver.find_element_by_xpath(".//*[@id='payBtn']/input").click()
     # Click Pay button
     time.sleep(10)
     driver.switch_to.default_content()
     driver.find_element_by_xpath(".//*[@id='win-tabs']/table/tbody/tr/td/ul/li[2]/a[1]").click()
     # Click "Search" segment
     driver.find_element_by_xpath(".//*[@id='win-tabs']/table/tbody/tr/td/ul/li[3]/a[1]").click()
     # Click "Pay" segment
     frame1 = driver.find_element_by_xpath(".//*[@id='form-tabs-iframeArea']/iframe[3]")
     driver.switch_to_frame(frame1)


def acceptUnderControlSad(driver):
     driver.switch_to.default_content()
     frame = driver.find_element_by_xpath(".//*[@id='form-tabs-iframeArea']/iframe[3]")
     driver.switch_to_frame(frame)
     driver.find_element_by_xpath(".//*[@id='tbAccept']/input").click()
     time.sleep(10)

def processSad(driver):
     processSadBtn(driver)
     # Chose a SAD record and click process button
     frame = driver.find_element_by_xpath(".//*[@id='form-tabs-iframeArea']/iframe[3]")
     driver.switch_to_frame(frame)
     cd_status = driver.find_element_by_xpath(".//*[@id='sclist8001']/input[2]").get_attribute("value")
     # Acquire SAD status
     print cd_status
     if cd_status == "Conformant":
          paySimpleSad(driver)
     # If SAD status is conformant, then pay SAD
     elif cd_status == "Under control":
          acceptUnderControlSad(driver)
          paySimpleSad(driver)
     # If SAD status is under control, then accept under control SAD and pay for it
     else:
          print ("Incorrect CD status")
     # If status is neither conformant nor under control, then print message: incorrect cd status


