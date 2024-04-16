from selenium.webdriver.common.by import By


class Employeesearch:
    Text_Empname_XPATH = (By.XPATH,
                          "/html[1]/body[1]/div[1]/div[1]/div[2]/div[2]/div[1]/div[1]/div[2]/form[1]/div[1]/div["
                          "1]/div[1]/div[1]/div[2]/div[1]/div[1]/input[1]")

    click_search_xpath = (By.XPATH, "//button[@type='submit']")
    search_result_css_selector = (By.XPATH,"//div[contains(text(),'John Ty')]")


    # search_result_css_selector = (By.CSS_SELECTOR,"div[class='card-item card-body-slot'] div:nth-child(1) "
    #                                               "div:nth-child(1) div:nth-child(2)")


    def __init__(self, driver):
        self.driver = driver

    def Enter_EmpName(self, empname):
        self.driver.find_element(*Employeesearch.Text_Empname_XPATH).send_keys(empname)

    def Click_Searchbutton(self):
        self.driver.find_element(*Employeesearch.click_search_xpath).click()

    def search_Result(self):
        search = self.driver.find_element(*Employeesearch.search_result_css_selector)
        search_len = len(search)
        if search_len == 0:
            return False
        elif search_len == 1:
            print(self.driver.find_element(*Employeesearch.search_result_css_selector).text())
            return True
