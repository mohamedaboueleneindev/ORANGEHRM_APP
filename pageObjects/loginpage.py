from selenium import webdriver
from selenium.webdriver.common.by import By


class Loginpage:
    username_xpath = "/html/body/div/div[1]/div/div[1]/div/div[2]/div[2]/form/div[1]/div/div[2]/input"
    password_xpath ="/html/body/div/div[1]/div/div[1]/div/div[2]/div[2]/form/div[2]/div/div[2]/input"
    login_xpath = "//button[@type='submit']"
    menu_xpath = "//p[@class='oxd-userdropdown-name']"
    logout_xpath = "//a[normalize-space()='Logout']"

    def __init__(self,driver):
        self.driver :webdriver.Edge = driver

    def SetUserName(self,username):
        if not username:
            self.driver.find_element(By.XPATH,self.username_xpath).send_keys()
        else:
            self.driver.find_element(By.XPATH,self.username_xpath).send_keys(username)

    def SetPassword(self,password):
        if not password:
            self.driver.find_element(By.XPATH,self.username_xpath).send_keys()
        else:
            self.driver.find_element(By.XPATH,self.password_xpath).send_keys(password)

    def clickOnLogin(self):
        self.driver.find_element(By.XPATH,self.login_xpath).click()

    def clickOnlogout(self):
        self.driver.find_element(By.XPATH,self.menu_xpath).click()
        self.driver.find_element(By.XPATH,self.logout_xpath).click()

