# coding=utf-8

from common import baseURL




def test_login(driver,user):
	driver.get(baseURL.base_url)
	driver.find_element_by_id("username").clear()
	# clear username
	driver.find_element_by_id("username").send_keys(user)
	# input username =
	driver.find_element_by_id("passwd").clear()
	# clear password
	driver.find_element_by_id("passwd").send_keys("123456")
	# input password
	driver.find_element_by_id("loginBtn").click()
	# Click Login button
	print driver.title

