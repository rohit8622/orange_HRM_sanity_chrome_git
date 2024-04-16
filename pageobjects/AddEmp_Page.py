from selenium.webdriver.common.by import By
from selenium.common import NoSuchElementException as EC


class Add_Emp:
    click_PIM_XPATH = (By.XPATH, "//span[normalize-space()='PIM']")

    click_Add_Button_XPATH = (By.XPATH, "//i[@class='oxd-icon bi-plus oxd-button-icon']")

    Text_FirstName_XPATH = (By.XPATH, "//input[@placeholder='First Name']")

    Text_MiddleName_XPATH = (By.XPATH, "//input[@placeholder='Middle Name']")

    Text_LastName_XPATH = (By.XPATH, "//input[@placeholder='Last Name']")

    Click_Save_Button = (By.XPATH, "//button[@type='submit']")
    PersonalDetails_Tab_XPATH = (By.XPATH, "//h6[normalize-space()='Personal Details']")

    Click_Add_Emp_XPATH=(By.XPATH,"//a[normalize-space()='Add Employee']")


    def __init__(self, driver):
        self.driver = driver

    def Click_PIM(self):
        self.driver.find_element(*Add_Emp.click_PIM_XPATH).click()

    def Click_Add(self):
        self.driver.find_element(*Add_Emp.click_Add_Button_XPATH).click()

    def Enter_FirstName(self, firstname):
        self.driver.find_element(*Add_Emp.Text_FirstName_XPATH).send_keys(firstname)

    def Enter_MiddleName(self, middlename):
        self.driver.find_element(*Add_Emp.Text_MiddleName_XPATH).send_keys(middlename)

    def Enter_LastName(self, lastname):
        self.driver.find_element(*Add_Emp.Text_LastName_XPATH).send_keys(lastname)

    def click_save(self):
        self.driver.find_element(*Add_Emp.Click_Save_Button).click()

    def click_AddEmployee(self):
        self.driver.find_element(*Add_Emp.Click_Add_Emp_XPATH).click()

    def Add_Employee_status(self):
        self.driver.implicitly_wait(5)

        try:
            self.driver.find_element(*Add_Emp.PersonalDetails_Tab_XPATH)
            return True
        except EC:
            return False
