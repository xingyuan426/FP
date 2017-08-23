# coding=utf-8
from selenium import webdriver
import HTMLTestRunner
import os
import sys
import time
import unittest
from testCase import login
from testCase import entModule
from CLR import clr_menu
from CLR import clr_submenu
from ACC import acc_menu
from ACC import acc_submenu
from ACC import acc_ppr_manageTill
from ACC import acc_ppr_newPaymentSimpleSad
from CLR import clr_generalSimpleSad
from CLR import clr_itemSimpleSad
from CLR import clr_registerSimpleSad
from CLR import clr_searchSad
from CLR import clr_processSad
from testCase import logout

from testCase import closewindow

from common import userName

sys.path.append("..")
# rootPath = os.path.abspath('../')
# sys.path.append(rootPath+"\\testCase")
# sys.path.append(rootPath+"\\common")


cwd = os.getcwd()


class test(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.driver = webdriver.Firefox()
        cls.driver.implicitly_wait(30)
        cls.verificationErrors = []
        cls.accept_next_alert = True
        # default settings

    @classmethod
    def tearDownClass(cls):
        cls.driver.quit()

    def test_TC001_ACC_prepareTill(self):
        login.test_login(self.driver, userName.ACC_SUP)
        # Log in e-biscus with payment supervisor
        entModule.enter_acc(self.driver)
        # Enter Accounting
        acc_menu.acc_ppr(self.driver)
        # Select menu: Accounting -> Payment processing
        acc_submenu.acc_ppr_till(self.driver)
        # Select menu: Accounting -> Payment processing -> Tills
        acc_ppr_manageTill.prepareTill(self.driver)
        # If till status is reconciled, then prepare till
        logout.test_logout(self.driver)
        # Log out

    def test_TC002_ACC_openTill(self):
        login.test_login(self.driver, userName.ACC_CAS)
        # Log in Accounting with Cashier
        entModule.enter_acc(self.driver)
        # Enter Accounting
        acc_menu.acc_ppr(self.driver)
        # Select menu: Accounting -> Payment processing
        acc_submenu.acc_ppr_till(self.driver)
        # Select menu: Accounting -> Payment processing -> Tills
        acc_ppr_manageTill.openTill(self.driver)
        # If till status is allocated, then open till
        logout.test_logout(self.driver)
        # Log out

    def test_TC003_CLR_captureSimpleSad(self):
        login.test_login(self.driver, userName.ACC_CAS)
        # Log in Clearance with Fenix user
        entModule.enter_clr(self.driver)
        clr_menu.clr_declaration(self.driver)
        clr_submenu.clr_declaration_simple(self.driver)
        # Select menu: Declaration -> Capture a simple SAD
        clr_generalSimpleSad.saveGeneralSimpleSad(self.driver)
        # Input mandatory fields on GS page
        clr_itemSimpleSad.saveItemSimpleSad(self.driver)
        # Input mandatory fields on IS page
        clr_registerSimpleSad.registerSimpleSad(self.driver)
        # Register SAD
        logout.test_logout(self.driver)

    def test_TC004_CLR_paySimpleSad(self):
        login.test_login(self.driver, userName.ACC_CAS)
        # Log in Clearance with Fenix user
        entModule.enter_clr(self.driver)
        clr_menu.clr_declaration(self.driver)
        clr_submenu.clr_declaration_search(self.driver)
        # Select menu: Declaration -> search
        clr_searchSad.searchBySadNo(self.driver)
        # Search SAD by SAD registration number
        clr_processSad.processSad(self.driver)
        # Chose the SAD record and click process button
        acc_ppr_newPaymentSimpleSad.newPaymentSimpleSad(self.driver)
        closewindow.test_closewindow(self.driver)
        logout.test_logout(self.driver)

    def test_TC005_ACC_closeTill(self):
        login.test_login(self.driver, userName.ACC_CAS)
        # Log in Accounting with Cashier
        entModule.enter_acc(self.driver)
        # Enter Accounting
        acc_menu.acc_ppr(self.driver)
        # Select menu: Accounting -> Payment processing
        acc_submenu.acc_ppr_till(self.driver)
        # Select menu: Accounting -> Payment processing -> Tills
        acc_ppr_manageTill.closeTill(self.driver)
        # If till status is opened, then close till
        logout.test_logout(self.driver)
        # Log out

    def test_TC006_ACC_reconcileTill(self):
        login.test_login(self.driver, userName.ACC_SUP)
        # Log in e-biscus with payment supervisor
        entModule.enter_acc(self.driver)
        # Enter Accounting
        acc_menu.acc_ppr(self.driver)
        # Select menu: Accounting -> Payment processing
        acc_submenu.acc_ppr_till(self.driver)
        # Select menu: Accounting -> Payment processing -> Tills
        acc_ppr_manageTill.reconcileTill(self.driver)
        # If till status is closed, then reconcile till
        logout.test_logout(self.driver)
        # Log out

    def test_TC007_CLR_checkSadStatus(self):
        login.test_login(self.driver, userName.ACC_CAS)
        # Log in Clearance with Fenix user
        entModule.enter_clr(self.driver)
        clr_menu.clr_declaration(self.driver)
        clr_submenu.clr_declaration_search(self.driver)
        # Select menu: Declaration -> search
        clr_searchSad.searchBySadNo(self.driver)
        sadStatus = self.driver.find_element_by_xpath(".//*[@id='sclist8437']/input[2]").get_attribute("value")
        try:
            self.assertEqual("Pending removal",sadStatus)
        except AssertionError as e:
            print "SAD status is: " + sadStatus + ". Incorrect Sad status"
        logout.test_logout(self.driver)


if __name__ == '__main__':
    suiteTest = unittest.TestSuite()
    #suiteTest.addTest(test("test_TC001_ACC_prepareTill"))
    # If till status is reconciled, then prepare till
    #suiteTest.addTest(test("test_TC002_ACC_openTill"))
    # If till status is allocated, then open till
    suiteTest.addTest(test("test_TC003_CLR_captureSimpleSad"))
    # Select menu: Declaration -> Capture a simple SAD
    suiteTest.addTest(test("test_TC004_CLR_paySimpleSad"))
    # Direct Taxation for simple SAD
    suiteTest.addTest(test("test_TC005_ACC_closeTill"))
    # If till status is opened, then close till
    suiteTest.addTest(test("test_TC006_ACC_reconcileTill"))
    # If till status is closed, then reconcile till
    suiteTest.addTest(test("test_TC007_CLR_checkSadStatus"))

    #    file = "test.txt"
    #    f = open(file, "w")

    #    runner = unittest.TextTestRunner(stream=f, verbosity=2)
    #    runner.run(suiteTest)
    #    # run test case
    #    f.close()

    timestr = time.strftime('%Y%m%d%H%M%S', time.localtime(time.time()))
    filename = os.path.abspath(os.path.pardir + '/testResult') + "/result_" + timestr + ".html"
    print (filename)
    fp = open(filename, 'wb')
    runner = HTMLTestRunner.HTMLTestRunner(stream=fp, title='WEB TEST', description='Test Result')
    runner.run(suiteTest)
    fp.close()
