import time
from selenium.common import NoSuchElementException as EC


from selenium.webdriver.common.by import By


class Loginpage:

    Text_username_xpath=(By.XPATH,"//input[@placeholder='Username']")
    Text_password_xpath=(By.XPATH,"//input[@placeholder='Password']")
    click_login_button_xpath=(By.XPATH,"//button[normalize-space()='Login']")
    click_menu_button_xpath=(By.XPATH,"//p[@class='oxd-userdropdown-name']")
    click_logout_xpath=(By.XPATH,"//a[normalize-space()='Logout']")


    def __init__(self,driver):
        self.driver=driver


    def Enter_username(self,username):
        self.driver.find_element(*Loginpage.Text_username_xpath).send_keys(username)

    def Enter_password(self,password):
        self.driver.find_element(*Loginpage.Text_password_xpath).send_keys(password)

    def click_login(self):
        self.driver.find_element(*Loginpage.click_login_button_xpath).click()

    def click_menubutton(self):
        self.driver.find_element(*Loginpage.click_menu_button_xpath).click()

    def click_Logout(self):
        self.driver.find_element(*Loginpage.click_logout_xpath).click()


    def Login_status(self):
        time.sleep(3)

        try:
            self.driver.find_element(*Loginpage.click_menu_button_xpath)
            return True

        except EC:
            return False








