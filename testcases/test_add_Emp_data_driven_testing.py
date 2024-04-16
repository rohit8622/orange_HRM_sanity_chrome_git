import time

from selenium.common import NoSuchElementException as EC
from selenium.webdriver.common.by import By

from pageobjects.AddEmp_Page import Add_Emp
from pageobjects.Loginpage1 import Loginpage
from utilities import XLutils
from utilities.readproperties import Readconfig
from utilities.Logger import Loggenerator


class Test_Add_Emp_DDT:
    url = Readconfig.geturl()
    username = Readconfig.getusername()
    password = Readconfig.getpassword()
    log = Loggenerator.loggen()
    path = "C:\\python projects\\pythoncredkart\\orangehrm\\testcases\\TestData\\Employeelist.xlsx"

    def test_addEmp_ddt_005(self, setup):
        self.driver = setup
        self.log.info("test_addEmp_003 is started")
        self.log.info("opening browser")
        self.driver.get(self.url)
        self.log.info("go to this url-->" + self.url)
        time.sleep(2)
        self.lp = Loginpage(self.driver)
        self.lp.Enter_username(self.username)
        self.lp.Enter_password(self.password)
        self.log.info("Entering username-->" + self.username)
        self.log.info("Entering password-->" + self.password)
        self.lp.click_login()
        self.log.info("click on login button")

        self.ae = Add_Emp(self.driver)

        self.rows = XLutils.getrowcount(self.path, "Sheet1")
        print("Number of Rows are-->", self.rows)

        # self.FirstName = XLutils.readData(self.path, "Sheet1", 3, 2)
        # print(self.FirstName)

        self.ae.Click_PIM()
        self.ae.Click_Add()
        self.log.info("click on PIM")
        self.log.info("click on Add Button")

        status_list = []

        for r in range(2, self.rows + 1):
            # time.sleep(3)
            self.FirstName = XLutils.readData(self.path, "Sheet1", r, 2)
            self.MiddleName = XLutils.readData(self.path, "Sheet1", r, 3)
            self.LastName = XLutils.readData(self.path, "Sheet1", r, 4)
            time.sleep(2)
            self.ae.Enter_FirstName(self.FirstName)
            self.ae.Enter_MiddleName(self.MiddleName)
            self.ae.Enter_LastName(self.LastName)

            self.log.info("Entering firstname-->" + self.FirstName)
            self.log.info("Entering middlename--->" + self.MiddleName)
            self.log.info("Entering Lastname--->" + self.LastName)
            time.sleep(2)

            self.ae.click_save()
            self.log.info("click on save button")

            if self.ae.Add_Employee_status() == True:
                # time.sleep(5)
                self.ae.click_AddEmployee()
                status_list.append("Pass")
                XLutils.writedata(self.path, "Sheet1", r, 5, "Pass")
                self.driver.save_screenshot(
                    "C:\\python projects\\pythoncredkart\\orangehrm\\Screenshots\\test_addEmp_003-pass.png")
                # assert True
            else:
                # time.sleep(5)
                status_list.append("Fail")
                XLutils.writedata(self.path, "Sheet1", r, 5, "Fail")
                self.driver.save_screenshot(
                    "C:\\python projects\\pythoncredkart\\orangehrm\\Screenshots\\test_addEmp_003-fail.png")
                # assert False

        print(status_list)
        time.sleep(2)
        self.lp.click_menubutton()
        self.log.info("click on menu button")
        self.lp.click_Logout()
        self.log.info("click on logout button")
        self.driver.close()
        if "Fail" not in status_list:
            self.log.info("test_addEmp_003 is passed")
            assert True
        else:
            self.log.info("test_addEmp_003 is Failed")
            assert False
        self.log.info("test_addEmp_003 is completed")


