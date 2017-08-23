import time
import os
from common import test_data

def ppr_newPayerInfo(driver):
    time.sleep(10)
    frame = driver.find_element_by_xpath(".//*[@id='form-tabs-iframeArea']/iframe[2]")
    driver.switch_to_frame(frame)
    driver.find_element_by_xpath(".//*[@id='tbNew']/input").click()
    # Click New button
    time.sleep(5)
    driver.switch_to.default_content()
    frame1 = driver.find_element_by_xpath(".//*[@id='form-tabs-iframeArea']/iframe[3]")
    driver.switch_to_frame(frame1)
    f = open(os.path.pardir + '/common/payInstructionNo.txt', 'r')
    payInstructionNo=f.readline()
    f.close()
    # Read payment instruction number from the txt
    driver.find_element_by_xpath(".//*[@id='instructions']/input").send_keys(payInstructionNo)
    driver.find_element_by_xpath(".//*[@id='filed_Status']/input[2]").click()
    time.sleep(6)
    traderNo = driver.find_element_by_xpath(".//*[@id='row0cell1TinCol']/div").text
    print traderNo
    time.sleep(1)
    driver.find_element_by_xpath(".//*[@id='payerTpl-TIN']/input").send_keys(traderNo)


def ppr_newPaymentInstrument(driver):
    time.sleep(1)
    amount = driver.find_element_by_xpath(".//*[@id='payment_amount']/input").get_attribute("value")
    print amount
    time.sleep(1)
    # get payment amount
    driver.find_element_by_xpath(".//*[@id='pmtInstrumentListTabV2TableAddDelCol']/div/div/a").click()
    # Click Add payment instrument button
    time.sleep(5)
    frame2 = driver.find_element_by_class_name("fancybox-iframe")
    driver.switch_to_frame(frame2)
    driver.find_element_by_xpath(".//*[@id='pai_Type']/input[1]").send_keys(test_data.payType)
    # Payment instrument type = CHQ
    time.sleep(1)
    driver.find_element_by_xpath(".//*[@id='pai_Value']/input").send_keys(amount)
    # Pyament instrument value = Payment amount
    time.sleep(1)
    driver.find_element_by_xpath(".//*[@id='pai_Status']/input[2]").click()
    # Click on "local currency value"
    time.sleep(1)
    driver.find_element_by_xpath(".//*[@id='tbSave']/input").click()
    # Click save payment isntrument button
    time.sleep(5)
    # Click save button


def ppr_submitPayment(driver):
    driver.switch_to.default_content()
    frame3 = driver.find_element_by_xpath(".//*[@id='form-tabs-iframeArea']/iframe[3]")
    driver.switch_to_frame(frame3)
    # Switch back to iframe[3]
    driver.find_element_by_xpath(".//*[@id='tbSubmit']/input").click()
    # Click submit payment button to capture payment
    time.sleep(10)

def ppr_newPayment(driver):
    ppr_newPayerInfo(driver)
    ppr_newPaymentInstrument(driver)
    ppr_submitPayment(driver)