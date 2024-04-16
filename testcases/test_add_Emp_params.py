import time

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


    def test_addEmp_003(self, setup,getData_for_Name):
        self.driver = setup

        self.log.info("test_addEmp_003 is started")
        self.log.info("opening browser")

        self.driver.get(self.url)
        self.log.info("go to this url-->"+self.url)

        time.sleep(2)

        self.lp = Loginpage(self.driver)


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
        self.ae.Enter_FirstName(getData_for_Name[0])
        self.ae.Enter_MiddleName(getData_for_Name[1])
        self.ae.Enter_LastName(getData_for_Name[2])

        self.log.info("Entering firstname"+getData_for_Name[0])
        self.log.info("Entering middlename"+getData_for_Name[1])
        self.log.info("Entering Lastname"+getData_for_Name[2])

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





