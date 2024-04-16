import time

import pytest
from selenium.common import NoSuchElementException as EC
from selenium.webdriver.common.by import By

from pageobjects.AddEmp_Page import Add_Emp
from pageobjects.Employee_search_page import Employeesearch
from pageobjects.Loginpage1 import Loginpage
from utilities.readproperties import Readconfig
from utilities.Logger import Loggenerator


class Test_search_Emp:
    url = Readconfig.geturl()
    username = Readconfig.getusername()
    password = Readconfig.getpassword()
    log = Loggenerator.loggen()

    @pytest.mark.sanity
    def test_searchEmp_005(self, setup):
        self.driver = setup
        self.log.info("test_searchEmp_005 is started")
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
        self.ae.Click_PIM()
        self.log.info("click on PIM")
        time.sleep(2)

        self.es = Employeesearch(self.driver)
        self.es.Enter_EmpName("selvam")
        time.sleep(5)
        self.log.info("Entering Emp Name")
        time.sleep(2)
        self.es.Click_Searchbutton()
        self.log.info("clicking on search button")
        time.sleep(2)
        print(self.es.search_Result())
        if self.es.search_Result() == True:
            time.sleep(3)
            self.log.info("search Found")
            self.lp.click_menubutton()
            self.log.info("click on menu button")
            self.lp.click_Logout()
            self.log.info("click on logout button")
            self.log.info("test_searchemp_005 is passed")

            assert True
        else:
            self.log.info("No search found")
            self.lp.click_menubutton()
            self.log.info("click on menu button")
            self.lp.click_Logout()
            self.log.info("click on logout button")

            self.log.info("test_searchemp_005 is failed")
            assert False
        self.driver.close()
