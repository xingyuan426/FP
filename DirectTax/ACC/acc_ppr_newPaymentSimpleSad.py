import time
from common import test_data

def newPaymentInstrumentSimpleSad(driver):
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
    driver.find_element_by_xpath(".//*[@id='pai_Type']/input[1]").send_keys(test_data.payTypeSimple)
    # Payment instrument type = CSH
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
    driver.switch_to.default_content()
    frame3 = driver.find_element_by_xpath(".//*[@id='form-tabs-iframeArea']/iframe[3]")
    driver.switch_to_frame(frame3)
    # Switch back to iframe[3]
    driver.find_element_by_xpath(".//*[@id='tbSubmit']/input").click()
    # Click submit payment button to capture draft payment
    time.sleep(10)

def submitPaymentSimpleSad(driver):
    driver.switch_to.default_content()
    frame3 = driver.find_element_by_xpath(".//*[@id='form-tabs-iframeArea']/iframe[3]")
    driver.switch_to_frame(frame3)
    # Switch back to iframe[3]
    driver.find_element_by_xpath(".//*[@id='tbSubmit']/input").click()
    # Click submit payment button to capture draft payment
    time.sleep(10)



def newPaymentSimpleSad(driver):
     newPaymentInstrumentSimpleSad(driver)
     submitPaymentSimpleSad(driver)