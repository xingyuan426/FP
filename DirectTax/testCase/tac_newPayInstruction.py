import time
import os

def tac_newPayInstruction(driver):
    time.sleep(5)
    frame = driver.find_element_by_xpath(".//*[@id='form-tabs-iframeArea']/iframe[2]")
    driver.switch_to_frame(frame)
    driver.find_element_by_xpath(".//*[@id='tbNew']/input").click()
    time.sleep(5)
    driver.switch_to.default_content()
    frame1 = driver.find_element_by_xpath(".//*[@id='form-tabs-iframeArea']/iframe[3]")
    driver.switch_to_frame(frame1)
    driver.find_element_by_xpath(".//*[@id='entityType']/input[1]").send_keys("SAD")
    # Input entity type = SAD
    f = open(os.path.pardir + '/common/SAD.txt', 'r')
    data = f.readline()
    f.close()
    driver.find_element_by_xpath(".//*[@id='refNum']/input").send_keys(data)
    # Input entity reference no = SAD registration number
    time.sleep(1)
    driver.find_element_by_xpath(".//*[@id='SearchTbl']").click()
    time.sleep(1)
    driver.find_element_by_xpath(".//*[@id='addInfo']").click()
    # Add payment instruction
    time.sleep(1)
    driver.find_element_by_xpath(".//*[@id='tbSubmit']/input").click()
    # Submit payment instruction
    time.sleep(5)


def tac_submitPayInstruction(driver):
    driver.switch_to.default_content()
    driver.find_element_by_xpath(".//*[@id='win-tabs']/table/tbody/tr/td/ul/li[2]/a[1]").click()
    driver.find_element_by_xpath(".//*[@id='win-tabs']/table/tbody/tr/td/ul/li[3]/a[1]").click()
    # Switch back to the current segment
    time.sleep(1)
    data = driver.find_element_by_xpath(".//*[@id='win-tabs']/table/tbody/tr/td/ul/li[3]/a[1]").get_attribute("title")
    payInstructionNo = filter(str.isdigit, data.encode("utf-8"))
    print payInstructionNo
    # mark SAD registration number as "segno"
    # f=open("C:\Users\A626855\PycharmProjects\DirectTax\common\SAD.txt",'w')
    f = open(os.path.pardir + '/common/payInstructionNo.txt', 'w')
    f.write(payInstructionNo)
    f.close()
    # Write payment instruction no
    frame = driver.find_element_by_xpath(".//*[@id='form-tabs-iframeArea']/iframe[3]")
    driver.switch_to_frame(frame)
    driver.find_element_by_xpath(".//*[@id='PaymentMode']/input[1]").send_keys("GCHT")
    time.sleep(1)
    driver.find_element_by_xpath(".//*[@id='tbSubmit']/input").click()

def tac_capturePayInstruction(driver):
     tac_newPayInstruction(driver)
     tac_submitPayInstruction(driver)