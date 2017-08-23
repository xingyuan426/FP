# coding=utf-8

import time
import os



def searchbut(driver):
    time.sleep(10)
    f = open(os.path.pardir + '/common/SAD.txt', 'r')
    data=f.readline()
    f.close()
    # read SAD no
    frame = driver.find_element_by_xpath(".//*[@id='form-tabs-iframeArea']/iframe[2]")
    driver.switch_to_frame(frame)
    driver.find_element_by_xpath(".//*[@id='Field12232']/input").send_keys(data)
    # input SAD registration number
    driver.find_element_by_xpath(".//*[@id='But8486']").click()
    time.sleep(5)
    # Click search button

def processbut(driver):
    driver.find_element_by_xpath(".//*[@id='Tbl7658']/div[2]/div/div[2]/table/tbody/tr").click()
    # Chose a record
    time.sleep(1)
    driver.find_element_by_xpath(".//*[@id='tbProcess']/input").click()
    # Click process button
    time.sleep(10)
    driver.switch_to.default_content()
    # Wait for 10 seconds until the page opened