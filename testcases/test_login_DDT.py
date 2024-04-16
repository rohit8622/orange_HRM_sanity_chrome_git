import time

from selenium import webdriver
from selenium.common import NoSuchElementException as EC
from selenium.webdriver.common.by import By
from pageobjects.Loginpage1 import Loginpage
from testcases.conftest import getData_for_login
from utilities import XLutils
from utilities.readproperties import Readconfig
from utilities.Logger import Loggenerator


class Test_login_DDT:
    url = Readconfig.geturl()
    # username = Readconfig.getusername()
    # password = Readconfig.getpassword()
    log = Loggenerator.loggen()
    path = "C:\\python projects\\pythoncredkart\\orangehrm\\testcases\\TestData\\LoginData.xlsx"

    def test_login_ddt_06(self, setup):
        self.driver = setup
        self.log.info("test_login_ddt_06 is started")
        self.driver.get(self.url)
        self.log.info("Go to this url--->" + self.url)
        self.lp = Loginpage(self.driver)
        self.rows = XLutils.getrowcount(self.path, "Sheet1")
        print("Number of rows are-->", self.rows)
        login_status = []
        for r in range(2, self.rows + 1):
            time.sleep(3)
            self.username = XLutils.readData(self.path, "Sheet1", r, 2)
            self.password = XLutils.readData(self.path, "Sheet1", r, 3)
            time.sleep(2)

            self.lp.Enter_username(self.username)
            self.lp.Enter_password(self.password)
            time.sleep(2)

            self.log.info("Entering username-->" + self.username)
            self.log.info("Entering password--->" + self.password)
            self.lp.click_login()
            self.log.info("click on login button")
            print(self.username)
            print(self.password)
            time.sleep(5)
            if self.lp.Login_status() == True:
                self.driver.save_screenshot(
                    "D:\\Credence Class Notes\\CredenceBatches\\CredenceBatch#13\\OrangeHrm\\ScreenShots\\"+self.username+self.password+"test_login_ddt_06-pass.png")
                self.lp.click_menubutton()
                self.log.info("Click on Menu button")
                self.lp.click_Logout()
                self.log.info("Click on logout button")

                login_status.append("Pass")
                XLutils.writedata(self.path, 'Sheet1', r, 4,"Pass")
            else:

                login_status.append("Fail")
                XLutils.writedata(self.path, 'Sheet1', r, 4, "Fail")
                self.driver.save_screenshot(
                    "D:\\Credence Class Notes\\CredenceBatches\\CredenceBatch#13\\OrangeHrm\\ScreenShots\\"+self.username+self.password+"test_login_ddt_06-fail.png")
                #assert False
        print(login_status)
        time.sleep(5)
        if "Fail" not in login_status:
            self.log.info("test_login_ddt_006 is passed")
            assert True

        else:
            self.log.info("test_login_ddt_006 is failed")
            assert False
        self.driver.close()
        self.log.info("test_login_ddt_06 is completed")



#############################################################
# if self.lp.Login_status() == True:
#     time.sleep(5)
#     if self.lp.Login_status() == "Pass":
#         self.driver.save_screenshot(
#             "C:\\python projects\\pythoncredkart\\orangehrm\\Screenshots\\" + self.username + self.password + "test_login_ddt_006-pass.png")
#
#         self.lp.click_menubutton()
#         self.log.info("click on menu button")
#
#         self.lp.click_Logout()
#         self.log.info("click on logout button")
#         login_status.append("Pass")
#         XLutils.writedata(self.path, "Sheet1", r, 4, "Pass")
#     else:
#         self.log.info("test_login_params_04 is failed")
#         self.driver.save_screenshot(
#             "C:\\python projects\\pythoncredkart\\orangehrm\\Screenshots\\ " + self.username + self.password + "test_login_ddt_006-fail.png")
#
# else:
#     time.sleep(5)
#     if self.lp.Login_status() == "Fail":
#         login_status.append("Fail")
#         XLutils.writedata(self.path, "Sheet1", r, 4, "Fail")
#         self.driver.save_screenshot(
#             "C:\\python projects\\pythoncredkart\\orangehrm\\Screenshots\\" + self.username + self.password + "test_login_ddt_006-fail.png")
#
#
#     else:
#         self.log.info("test_login_params_04 is failed")
#         self.driver.save_screenshot(
#             "C:\\python projects\\pythoncredkart\\orangehrm\\Screenshots\\" + self.username + self.password + "test_login_ddt_006-fail.png")
#
###############################################################








