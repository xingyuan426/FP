# coding=utf-8

import time
import os


# Search SAD by input SAD registration number
def searchBySadNo(driver):
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

def outputSadStatus(driver):
     searchBySadNo(driver)
     sadStatus = driver.find_element_by_xpath(".//*[@id='sclist8437']/input[2]").get_attribute("value")
     time.sleep(1)
     # mark SAD status is sadStatus
     f = open(os.path.pardir + '/common/sadStatus.txt', 'w')
     f.write(sadStatus)
     f.close()