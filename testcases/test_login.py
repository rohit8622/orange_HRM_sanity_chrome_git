import time

import pytest
from selenium import webdriver
from selenium.common import NoSuchElementException as EC
from selenium.webdriver.common.by import By
from pageobjects.Loginpage1 import Loginpage
from utilities.readproperties import Readconfig
from utilities.Logger import Loggenerator


class Test_login:


    url = Readconfig.geturl()
    username = Readconfig.getusername()
    password = Readconfig.getpassword()
    log=Loggenerator.loggen()


    @pytest.mark.sanity
    def test_page_title_01(self,setup):
        self.driver=setup
        self.log.info("test_page_title_01 is started")
        self.log.info("opening browser")

        self.driver.get(self.url)
        self.log.info("go to this url-->"+self.url)

        print(self.url)

        # driver=webdriver.Chrome()
        # driver.implicitly_wait(5)
        # driver.get("https://opensource-demo.orangehrmlive.com/")

        if self.driver.title=="OrangeHRM":
            assert True
            self.log.info("test_page_title_01 is pass")
            self.log.info("page title is-->"+self.driver.title)
        else:

            self.log.info("test_page_title_01 is failed")
            assert False
        self.driver.close()
        self.log.info("test case is completed")

        # self.log.debug("debug")
        # self.log.info("info")
        # self.log.warning("warning")
        # self.log.error("error")
        # self.log.critical("critical")



    def test_login_02(self, setup):
        self.driver = setup

        self.log.info("test-login_02 is started")

        self.driver.get(self.url)
        self.log.info("Go to this url--->"+self.url)


        # driver = webdriver.Chrome()
        # driver.implicitly_wait(5)
        # driver.get('https://opensource-demo.orangehrmlive.com/')

        self.lp = Loginpage(self.driver)
        # self.lp.Enter_username("Admin")
        # self.lp.Enter_password("admin1234")

        self.lp.Enter_username(self.username)
        self.lp.Enter_password(self.password)

        self.log.info("Entering username-->"+self.username)
        self.log.info("Entering password--->"+self.password)

        self.lp.click_login()
        self.log.info("click on login button")

        print(self.username)
        print(self.password)

        # self.driver.find_element(By.XPATH, "//input[@placeholder='Username']").send_keys("Admin")
        # self.driver.find_element(By.XPATH, "//input[@placeholder='Password']").send_keys("admin123")
        # self.driver.find_element(By.XPATH, "//button[normalize-space()='Login']").click()

        # try:
        #
        #     self.driver.find_element(By.XPATH, "//p[@class='oxd-userdropdown-name']").click()
        #     self.driver.find_element(By.XPATH, "//a[normalize-space()='Logout']").click()
        #
        #     # login=True
        #     print("test_login_01 is passed")
        #     assert True
        #
        # except EC:
        #     # login=False
        #     assert False
        #     print("test_login_01 is failed")
        #
        # print("test_login_01 is completed")

        if self.lp.Login_status() == True:
            self.driver.save_screenshot("C:\\python projects\\pythoncredkart\\orangehrm\\Screenshots\\test_login_02-pass.png")

            self.lp.click_menubutton()
            self.log.info("click on menu button")

            self.lp.click_Logout()
            self.log.info("click on logout button")
            self.log.info("test_login_02 is passed")

            assert True
        else:

            self.log.info("test_login_02 is failed")
            self.driver.save_screenshot("C:\\python projects\\pythoncredkart\\orangehrm\\Screenshots\\test_login_02-fail.png")
            assert False
        self.driver.close()
        self.log.info("test_login_02 is completed")
















