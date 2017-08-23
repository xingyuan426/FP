# Prepare till
# Need optimize: 1.


from selenium import webdriver
import time
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
import random

driver = webdriver.Firefox()
driver.get("https://eb-fp-test:8101")
driver.find_element_by_id("username").clear()
# clear username
driver.find_element_by_id("username").send_keys("accsup")
# input username =
driver.find_element_by_id("passwd").clear()
# clear password
driver.find_element_by_id("passwd").send_keys("123456")
# input password
driver.find_element_by_id("loginBtn").click()
# Click Login button
print driver.title
time.sleep(2)
driver.find_element_by_xpath(".//*[@id='middle']/div[2]/div[2]/p/a").click()
# Entry into Accounting module
time.sleep(3)
#locator1 = (By.XPATH, ".//*[@id='PPR']/a/span[2]")
#WebDriverWait(driver, 10, 0.1).until(EC.element_to_be_clickable(locator1)).click()
driver.find_element_by_xpath(".//*[@id='PPR']/a/span[2]").click()
# Select menu: Payment processing
time.sleep(1)
locator2 = (By.XPATH, ".//*[@id='PPRMENU033']/a/span[2]")
WebDriverWait(driver, 10, 0.5).until(EC.visibility_of_element_located(locator2)).click()
#driver.find_element_by_xpath(".//*[@id='PPRMENU033']/a/span[2]").click()
# Select menu: Payment processing -> Tills
time.sleep(2)
locator3 = (By.XPATH,".//*[@id='form-tabs-iframeArea']/iframe[2]")
WebDriverWait(driver, 10, 0.5).until(EC.frame_to_be_available_and_switch_to_it(locator3))
#frame = driver.find_element_by_xpath(".//*[@id='form-tabs-iframeArea']/iframe[2]")
#driver.switch_to.frame(frame)
# Switch to iframe2
time.sleep(7)


#n = driver.find_elements_by_class_name("row row1")
recoTill = driver.find_elements_by_css_selector("[title='Reconciled']")
closTill = driver.find_elements_by_css_selector("[title='Closed']")
openTill = driver.find_elements_by_css_selector("[title='Opened']")
alloTill = driver.find_elements_by_css_selector("[title='Allocated']")
suspTill = driver.find_elements_by_css_selector("[title='Suspened']")

n1=len(recoTill)
n2=len(closTill)
n3=len(openTill)
n4=len(alloTill)
n5=len(suspTill)

print n1

#for i in n1:
#    recoTill[i].click()
#    driver.find_element_by_xpath(".//*[@id='tbPrepareTill']/input").click()
#    # Click process button to enter prepare till page
#    time.sleep(2)
#    driver.switch_to.default_content()
#    # switch to default iframe
#    frame = driver.find_element_by_xpath(".//*[@id='form-tabs-iframeArea']/iframe[3]")
#    driver.switch_to.frame(frame)
#    driver.find_element_by_xpath(".//*[@id='List15309']/input[2]").send_keys("ACCOFF1")
#    # Select Cashier = ACCOFF1
#    time.sleep(2)
#    driver.find_element_by_xpath(".//*[@id='tbSubmit']/input").click()
    # Allocate the till to Cahier "ACCOFF1"
#    time.sleep(5)
#for i in n2:
#    closTill[i].click()
#elements = driver.find_elements_by_css_selector("[class='row row1']")

#n=len(elements)

#t = random.randint(0, n)

#elements[t].click()
#print elements
#print n[0].index
#print n[0].text
#m = driver.find_elements_by_class_name("row row2")
#print n
#for i in n:
#    print i.get_attribute('index')
