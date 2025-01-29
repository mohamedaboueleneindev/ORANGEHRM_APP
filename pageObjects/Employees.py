from selenium import webdriver
from selenium.webdriver.common.by import By


class Employees:
    pm_menu_xpath = "//div[@class='oxd-layout-navigation']//li[2]"
    add_employee_xpath ="//header[@class='oxd-topbar']//li[3]"
    first_name_xpath = "//input[@placeholder='First Name']"
    last_name_xpath = "//input[@placeholder='Last Name']"
    employeeid_xpath="//div[@class='oxd-input-group oxd-input-field-bottom-space']//div//input[@class='oxd-input oxd-input--active']"
    saveButton_xpath="//button[normalize-space()='Save']"
    confirmName_xpath = "//*[@id='app']/div[1]/div[2]/div[2]/div/div/div/div[1]/div[1]/div[1]/h6"

    def __init__(self,driver):
        self.driver :webdriver.Chrome = driver

    def clickOnPmMenu (self):
        self.driver.find_element(By.XPATH,self.pm_menu_xpath).click()

    def clickOnAddEmpolyee (self):
        self.driver.find_element(By.XPATH,self.add_employee_xpath).click()

    def setFirstName (self,name):
        self.driver.find_element(By.XPATH,self.first_name_xpath).send_keys(name)
    
    def setLastName (self,name):
        self.driver.find_element(By.XPATH,self.last_name_xpath).send_keys(name)
    
    def setId (self,id):
        self.driver.find_element(By.XPATH,self.employeeid_xpath).send_keys(id)

    def clickonSave (self):
        self.driver.find_element(By.XPATH,self.saveButton_xpath).click()
    
    def confirmName (self):
        return self.driver.find_element(By.XPATH,self.confirmName_xpath).text
        