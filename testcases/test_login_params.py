import time

from selenium import webdriver
from selenium.common import NoSuchElementException as EC
from selenium.webdriver.common.by import By
from pageobjects.Loginpage1 import Loginpage
from utilities.readproperties import Readconfig
from utilities.Logger import Loggenerator

class Test_login_params:

    url = Readconfig.geturl()
    username = Readconfig.getusername()
    password = Readconfig.getpassword()
    log=Loggenerator.loggen()

    def test_login_params_04(self, setup,getData_for_login):
        self.driver = setup

        self.log.info("test-login_params_04 is started")

        self.driver.get(self.url)
        self.log.info("Go to this url--->"+self.url)
        self.lp = Loginpage(self.driver)
        self.lp.Enter_username(getData_for_login[0])
        self.lp.Enter_password(getData_for_login[1])
        self.log.info("Entering username-->"+getData_for_login[0])
        self.log.info("Entering password--->"+getData_for_login[1])
        self.lp.click_login()
        self.log.info("click on login button")
        print(self.username)
        print(self.password)

        if self.lp.Login_status() == True:
            if getData_for_login[2]=="Pass":
                self.driver.save_screenshot(
                    "C:\\python projects\\pythoncredkart\\orangehrm\\Screenshots\\test_login_02-pass.png")
                self.lp.click_menubutton()
                self.log.info("click on menu button")
                self.lp.click_Logout()
                self.log.info("click on logout button")
                self.log.info("test_login_params_04 is passed")
                assert True

            else:
                self.log.info("test_login_params_04 is failed")
                self.driver.save_screenshot(
                    "C:\\python projects\\pythoncredkart\\orangehrm\\Screenshots\\test_login_02-fail.png")
                assert False

        else:
            if getData_for_login[2]=="Fail":
                assert True
            else:
                self.log.info("test_login_params_04 is failed")
                self.driver.save_screenshot(
                    "C:\\python projects\\pythoncredkart\\orangehrm\\Screenshots\\test_login_02-fail.png")
                assert False
        self.driver.close()
        self.log.info("test_login_params_04 is completed")
















