import os
import time

def output_sadno(driver):
	time.sleep(3)
	regno=driver.find_element_by_xpath(".//*[@id='Field8777']/input").get_attribute("value")
	# mark SAD registration number as "segno"
	#f=open("C:\Users\A626855\PycharmProjects\DirectTax\common\SAD.txt",'w')
	f=open(os.path.pardir + '/common/SAD.txt','w')
	f.write(regno)
	f.close()
	print regno