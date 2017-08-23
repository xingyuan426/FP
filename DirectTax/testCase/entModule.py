import time


def enter_acc(driver):
    time.sleep(5)
    driver.find_element_by_xpath(".//*[@id='middle']/div[2]/div[2]/p/a").click()
    # Entry into Accounting module


def enter_clr(driver):
    time.sleep(5)
    driver.find_element_by_id("demoCLR").click()
