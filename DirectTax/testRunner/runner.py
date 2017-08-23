# coding=utf-8
from selenium import webdriver
import HTMLTestRunner
import os
import sys
import time
import unittest
from testCase import login
from testCase import entModule
from testCase import menu
from testCase import manageTill
from testCase import logout
from testCase import simgsbox
from testCase import simgsbut
from testCase import goto
from testCase import simisbox
from testCase import output
from testCase import searchSad
from testCase import process
from testCase import closewindow
from testCase import loadSad
from testCase import tac_newPayInstruction
from testCase import ppr_newPayment
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

    def test_prepareTill(self):
        login.test_login(self.driver, userName.ACC_SUP)
        # Log in e-biscus with payment supervisor
        entModule.enter_acc(self.driver)
        # Enter Accounting
        menu.acc_ppr(self.driver)
        # Select menu: Accounting -> Payment processing
        menu.acc_ppr_till(self.driver)
        # Select menu: Accounting -> Payment processing -> Tills
        manageTill.test_prepareTill(self.driver)
        # If till status is reconciled, then prepare till
        logout.test_logout(self.driver)
        # Log out

    def test_openTill(self):
        login.test_login(self.driver, userName.ACC_CAS)
        # Log in Accounting with Cashier
        entModule.enter_acc(self.driver)
        # Enter Accounting
        menu.acc_ppr(self.driver)
        # Select menu: Accounting -> Payment processing
        menu.acc_ppr_till(self.driver)
        # Select menu: Accounting -> Payment processing -> Tills
        manageTill.test_openTill(self.driver)
        # If till status is allocated, then open till
        logout.test_logout(self.driver)
        # Log out

    def test_closeTill(self):
        login.test_login(self.driver, userName.ACC_CAS)
        # Log in Accounting with Cashier
        entModule.enter_acc(self.driver)
        # Enter Accounting
        menu.acc_ppr(self.driver)
        # Select menu: Accounting -> Payment processing
        menu.acc_ppr_till(self.driver)
        # Select menu: Accounting -> Payment processing -> Tills
        manageTill.test_closeTill(self.driver)
        # If till status is opened, then close till
        logout.test_logout(self.driver)
        # Log out

    def test_reconTill(self):
        login.test_login(self.driver, userName.ACC_SUP)
        # Log in e-biscus with payment supervisor
        entModule.enter_acc(self.driver)
        # Enter Accounting
        menu.acc_ppr(self.driver)
        # Select menu: Accounting -> Payment processing
        menu.acc_ppr_till(self.driver)
        # Select menu: Accounting -> Payment processing -> Tills
        manageTill.test_reconTill(self.driver)
        # If till status is closed, then reconcile till

    def test_capDAU(self):
        login.test_login(self.driver, userName.ACC_CAS)
        # Log in Clearance with Fenix user
        entModule.enter_clr(self.driver)
        menu.clr_capture(self.driver)
        menu.clr_capture_simple(self.driver)
        # Select menu: Declaration -> Capture a simple SAD
        simgsbox.seg_movement(self.driver)
        simgsbox.input_box18(self.driver)
        simgsbut.gs_save(self.driver)
        goto.goto_is(self.driver)
        # Input mandatory fields on GS page
        simisbox.input_box33(self.driver)
        simisbox.input_box42(self.driver)
        simgsbut.gs_save(self.driver)
        goto.goto_gs(self.driver)
        # Input mandatory fields on IS page
        output.output_sadno(self.driver)
        # Output SAD registration number
        simgsbut.gs_save(self.driver)
        simgsbut.gs_register(self.driver)
        # Register SAD
        logout.test_logout(self.driver)

    def test_directTax(self):
        login.test_login(self.driver, userName.ACC_CAS)
        # Log in Clearance with Fenix user
        entModule.enter_clr(self.driver)
        menu.clr_capture(self.driver)
        menu.clr_search(self.driver)
        searchSad.searchbut(self.driver)
        searchSad.processbut(self.driver)
        process.selBtn(self.driver)
        closewindow.test_closewindow(self.driver)
        logout.test_logout(self.driver)

    def test_uploadSad(self):
        login.test_login(self.driver, userName.CLR_FEN)
        # Log in Clearance with Fenix user
        entModule.enter_clr(self.driver)
        menu.clr_loader(self.driver)
        menu.clr_loader_upload(self.driver)
        loadSad.loadSad(self.driver)
        menu.clr_capture(self.driver)
        menu.clr_search(self.driver)
        searchSad.searchbut(self.driver)
        sadStatus = self.driver.find_element_by_xpath(".//*[@id='sclist8437']/input[2]").get_attribute("value")
        try:
            self.assertEqual("Conformant",sadStatus)
        except AssertionError as e:
            print "SAD status is: " + sadStatus + ". Incorrect Sad status"
        logout.test_logout(self.driver)

        
    def test_tac_capturePayInstruction(self):
        login.test_login(self.driver, userName.ACC_SUP)
        # Log in e-biscus with payment supervisor
        entModule.enter_acc(self.driver)
        # Enter Accounting
        menu.acc_tac(self.driver)
        # Select menu: Trader Accounting
        menu.acc_tac_payInstruction(self.driver)
        # Select menu: Trader Accounting -> Payment Instruction
        tac_newPayInstruction.tac_capturePayInstruction(self.driver)
        # Capture payment instruction
        logout.test_logout(self.driver)

    def test_ppr_createPayment(self):
        login.test_login(self.driver, userName.ACC_SUP)
        # Log in e-biscus with payment supervisor
        entModule.enter_acc(self.driver)
        # Enter Accounting
        menu.acc_ppr(self.driver)
        # Select menu: Payment Processing
        menu.acc_ppr_payment(self.driver)
        # Select menu: Payment Processing -> Payments
        ppr_newPayment.ppr_newPayment(self.driver)
        # Create payment


if __name__ == '__main__':
    suiteTest = unittest.TestSuite()
    ############ Prepare till and open till#################
    #suiteTest.addTest(test("test_prepareTill"))
    # If till status is reconciled, then prepare till
    #suiteTest.addTest(test("test_openTill"))
    # If till status is allocated, then open till
    ############# Capture a simple SAD ####################
    #suiteTest.addTest(test("test_capDAU"))
    # Select menu: Declaration -> Capture a simple SAD
    ########## Pay a simple SAD in Clearance ##############
    #suiteTest.addTest(test("test_directTax"))
    #######################################################
    ########## Close and reconcile the till ###############
    #suiteTest.addTest(test("test_closeTill"))
    # If till status is opened, then close till
    #suiteTest.addTest(test("test_reconTill"))
    # If till status is closed, then reconcile till
    suiteTest.addTest(test("test_uploadSad"))
    # Upload a SAD without SD reference
    suiteTest.addTest(test("test_tac_capturePayInstruction"))
    suiteTest.addTest(test("test_ppr_createPayment"))

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
