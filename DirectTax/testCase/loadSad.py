import time
import os

def loadSad(driver):
    time.sleep(8)
    frame = driver.find_element_by_xpath(".//*[@id='form-tabs-iframeArea']/iframe[2]")
    driver.switch_to_frame(frame)
    #filepath = os.path.pardir + '/common/upfile.exe'
    driver.find_element_by_xpath(".//*[@id='Field12621']/input").click()
    # Click on file selection field
    time.sleep(1)
    os.system("C:\Users\A626855\PycharmProjects\DirectTax\common\upfile.exe")
    # Run upfile.exe to open file
    time.sleep(1)
    driver.find_element_by_xpath(".//*[@id='But8593']/input").click()
    # Click Register button
    time.sleep(20)
    regno = driver.find_element_by_xpath(".//*[@id='Field12635']/input").get_attribute("value")
    # Mark SAD registraiton number as regno
    f = open(os.path.pardir + '/common/SAD.txt', 'w')
    f.write(regno)
    f.close()
    print regno
    driver.switch_to.default_content()
    driver.find_element_by_xpath(".//*[@id='win-tabs']/table/tbody/tr/td/ul/li[2]/a[2]").click()
    # Close upload sub-page
