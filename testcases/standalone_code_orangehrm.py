import time

from selenium import webdriver
from selenium.webdriver.common.by import By
driver=webdriver.Chrome()
driver.implicitly_wait(5)
driver.get('https://opensource-demo.orangehrmlive.com/')
driver.find_element(By.XPATH,"//input[@placeholder='Username']").send_keys("Admin")
driver.find_element(By.XPATH,"//input[@placeholder='Password']").send_keys("admin123")
driver.find_element(By.XPATH,"//button[normalize-space()='Login']").click()
driver.find_element(By.XPATH,"//span[normalize-space()='PIM']").click()
driver.find_element(By.XPATH,"//i[@class='oxd-icon bi-plus oxd-button-icon']").click()




driver.find_element(By.XPATH,"//p[@class='oxd-userdropdown-name']").click()
driver.find_element(By.XPATH,"//a[normalize-space()='Logout']").click()






