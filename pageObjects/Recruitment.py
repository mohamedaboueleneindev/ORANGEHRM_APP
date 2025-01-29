from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import random

class Recruitment:
    recrui_Menu_Xpath = "//div[@class='oxd-layout-navigation']//li[5]"
    add_candidata_Xpath = "//button[normalize-space()='Add']"
    firstName_xpath = "//input[@placeholder='First Name']"
    lastName_xpath = "//input[@placeholder='Last Name']"
    Vacancy_click_xpath = "//i[@class='oxd-icon bi-caret-down-fill oxd-select-text--arrow']"
    NoVacancy_xpath = "//div[@class='oxd-select-wrapper']/div[2]/*"
    email_xpath = "//div[3]//div[1]//div[1]//div[1]//div[2]//input[1]"
    contact_xpath = "/html/body/div/div[1]/div[2]/div[2]/div/div/form/div[3]/div/div[2]/div/div[2]/input"
    date_xpath = "//input[@placeholder='yyyy-dd-mm']"
    clear_date_xpath ="//div[@class='oxd-date-input-link --clear']"
    save_xpath = "//button[normalize-space()='Save']"
    confirm_name_xpath = "(//p[@class='oxd-text oxd-text--p'])[1]"
    confirm_role_xpath ="(//div)[28]/p"

    def __init__(self,driver):
        self.driver : webdriver.Chrome = driver

    def clickRecruitmentMenu(self):
        self.driver.find_element(By.XPATH,self.recrui_Menu_Xpath).click()
    
    def addCandidate(self):
        self.driver.find_element(By.XPATH,self.add_candidata_Xpath).click()
    
    def setFirstName(self,name):
        self.driver.find_element(By.XPATH,self.firstName_xpath).send_keys(name)
    
    def setLaseName(self,name):
        self.driver.find_element(By.XPATH,self.lastName_xpath).send_keys(name)
    
    def clickVacancy(self):
        self.driver.find_element(By.XPATH,self.Vacancy_click_xpath).click()


    def setRandomRole(self):
        roles = []
        no_rows = len(self.driver.find_elements(By.XPATH,self.NoVacancy_xpath))
        for r in range(2,no_rows+1):
            roles.append(self.driver.find_element(By.XPATH,self.NoVacancy_xpath+"["+str(r)+"]").text)
        role = random.choice(roles)
        for x in range(2,no_rows+1):
            text =self.driver.find_element(By.XPATH,self.NoVacancy_xpath+"["+str(x)+"]").text
            if text == role :
                self.driver.find_element(By.XPATH,self.NoVacancy_xpath+"["+str(x)+"]").click()
                return text
   
    def setEmail(self,email):
        self.driver.find_element(By.XPATH,self.email_xpath).send_keys(email)
    
    def setcontact(self,contact):
        self.driver.find_element(By.XPATH,self.contact_xpath).send_keys(contact)
  
    def SetDate(self,date):
        self.driver.find_element(By.XPATH,self.date_xpath).click()
        time.sleep(2)
        self.driver.find_element(By.XPATH,self.clear_date_xpath).click()
        time.sleep(1)
        self.driver.find_element(By.XPATH,self.date_xpath).send_keys(date)

    def SaveCandidate(self):
        self.driver.find_element(By.XPATH,self.save_xpath).click()

    def getName(self):
        return self.driver.find_element(By.XPATH,self.confirm_name_xpath).text

    def getRole(self):
        return self.driver.find_element(By.XPATH,self.confirm_role_xpath).text