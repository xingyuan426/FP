import time


def test_logout(driver):
    time.sleep(5)
    driver.switch_to.default_content()
    # Switch to default iframe
    driver.find_element_by_xpath(".//*[@id='logoutLink']").click()
    # Click logout
    time.sleep(3)
