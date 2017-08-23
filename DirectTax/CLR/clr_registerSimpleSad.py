import os
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait

def outputSadNo(driver):
	time.sleep(3)
	regno=driver.find_element_by_xpath(".//*[@id='Field8777']/input").get_attribute("value")
	# mark SAD registration number as "segno"
	#f=open("C:\Users\A626855\PycharmProjects\DirectTax\common\SAD.txt",'w')
	f=open(os.path.pardir + '/common/SAD.txt','w')
	f.write(regno)
	f.close()
	print regno
    # Output SAD registration number

def saveBtn(driver):
    time.sleep(1)
    driver.find_element_by_xpath(".//*[@id='tbSave']/input").click()
    time.sleep(10)
    # print ("Save successfully")
    # Click save button on GS page

def registerBtn(driver):
    time.sleep(1)
    locator1 = (By.XPATH,".//*[@id='tbRegister']/input")
    WebDriverWait(driver, 10,0.5).until(EC.element_to_be_clickable(locator1)).click()
    time.sleep(20)
    #print ("Register successfully")
    # Click assess button on GS page

def registerSimpleSad(driver):
    outputSadNo(driver)
    saveBtn(driver)
    registerBtn(driver)
