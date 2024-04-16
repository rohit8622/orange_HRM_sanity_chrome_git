import time

import pytest
from selenium.common import NoSuchElementException as EC
from selenium.webdriver.common.by import By

from pageobjects.AddEmp_Page import Add_Emp
from pageobjects.Loginpage1 import Loginpage
from utilities.readproperties import Readconfig
from utilities.Logger import Loggenerator


class Test_Add_Emp:


    url=Readconfig.geturl()
    username=Readconfig.getusername()
    password=Readconfig.getpassword()
    log=Loggenerator.loggen()

    @pytest.mark.sanity
    def test_addEmp_003(self, setup):
        self.driver = setup

        self.log.info("test_addEmp_003 is started")
        self.log.info("opening browser")

        self.driver.get(self.url)
        self.log.info("go to this url-->"+self.url)

        time.sleep(2)

        self.lp = Loginpage(self.driver)

        # self.lp.Enter_username("Admin")
        # self.lp.Enter_password("admin123")

        self.lp.Enter_username(self.username)
        self.lp.Enter_password(self.password)

        self.log.info("Entering username-->"+self.username)
        self.log.info("Entering password-->"+self.password)


        self.lp.click_login()
        self.log.info("click on login button")

        time.sleep(2)
        self.ae = Add_Emp(self.driver)
        self.ae.Click_PIM()
        self.ae.Click_Add()

        self.log.info("click on PIM")
        self.log.info("click on Add Button")

        time.sleep(2)
        self.ae.Enter_FirstName("credence")
        self.ae.Enter_MiddleName("credence")
        self.ae.Enter_LastName("credence")

        self.log.info("Entering firstname")
        self.log.info("Entering middlename")
        self.log.info("Entering Lastname")

        self.ae.click_save()
        self.log.info("click on save button")

        if self.ae.Add_Employee_status() == True:

            time.sleep(2)
            self.driver.save_screenshot("C:\\python projects\\pythoncredkart\\orangehrm\\Screenshots\\test_addEmp_003-pass.png")

            self.lp.click_menubutton()
            self.log.info("click on menu button")

            self.lp.click_Logout()
            self.log.info("click on logout button")
            self.log.info("test_addEmp_003 is passed")

            assert True
        else:

            time.sleep(2)

            self.log.info("test_addEmp_003 is failed")
            self.driver.save_screenshot("C:\\python projects\\pythoncredkart\\orangehrm\\Screenshots\\test_addEmp_003-fail.png")
            assert False
        self.driver.close()
        self.log.info("test_addEmp_003 is completed")






    # def test_addemp_03(self,setup):
    #     self.driver = setup
    #     # driver = webdriver.Chrome()
    #     # driver.implicitly_wait(5)
    #     # driver.get('https://opensource-demo.orangehrmlive.com/')
    #     self.driver.find_element(By.XPATH, "//input[@placeholder='Username']").send_keys("Admin")
    #     self.driver.find_element(By.XPATH, "//input[@placeholder='Password']").send_keys("admin123")
    #     self.driver.find_element(By.XPATH, "//button[normalize-space()='Login']").click()
    #     self.driver.find_element(By.XPATH, "//span[normalize-space()='PIM']").click()
    #     self.driver.find_element(By.XPATH, "//i[@class='oxd-icon bi-plus oxd-button-icon']").click()
    #     self.driver.find_element(By.XPATH, "//input[@placeholder='First Name']").send_keys("credence")
    #     self.driver.find_element(By.XPATH, "//input[@placeholder='Middle Name']").send_keys("credence")
    #     self.driver.find_element(By.XPATH, "//input[@placeholder='Last Name']").send_keys("credence")
    #     self.driver.find_element(By.XPATH, "//button[@type='submit']").click()
    #
    #     try:
    #         time.sleep(3)
    #         self.driver.find_element(By.XPATH, "//h6[normalize-space()='Personal Details']")
    #         self.driver.find_element(By.XPATH, "//p[@class='oxd-userdropdown-name']").click()
    #         self.driver.find_element(By.XPATH, "//a[normalize-space()='Logout']").click()
    #
    #         print("test_addemp_03 is passed")
    #         # assert True                   ## agar assert true ho gaya toh aage ka code i.e except block mai nahi jayega aur errror marega
    #         addemp = True
    #
    #     except EC:
    #         print("test_addemp_03 is failed")
    #         print("test_addemp_03 is completed")
    #         # assert False
    #         addemp = False  ##addemp ko flag dena kahte hai or variable bhi kehte hai
    #         ##try:except block mai assertion dena not a good thing better to give with a flag
    #
    #     if addemp == True:  ##flag leke assertion lagaoo
    #         assert True  ### better to take assertion with flag
    #     else:
    #         assert False
    #
    #     print(addemp)
    #     self.driver.close()
