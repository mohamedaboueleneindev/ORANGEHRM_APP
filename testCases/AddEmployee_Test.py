from pageObjects.loginpage import Loginpage
from pageObjects.Employees import Employees
from utilities.customlogger import LogGen
from utilities.readproperties import Readconfig
from selenium import webdriver
import time
import string
import random

logger = LogGen.loggen()

def generate_random_text(length, chars=string.ascii_letters + string.digits):
    return ''.join(random.choice(chars) for _ in range(length))


class Test_002_addEmployee:
    baseURL = Readconfig.getApplicationURL()
    username = Readconfig.getusername()
    password = Readconfig.getpassword()

    def test_Add_employee(self,setup):
        logger.info("************* Test_002_addEmployee ***********")
        self.driver : webdriver.Chrome = setup
        self.driver.get(self.baseURL)
        self.driver.implicitly_wait(10)
        self.driver.maximize_window()
        self.LP =Loginpage(self.driver)
        self.LP.SetUserName(self.username)
        self.LP.SetPassword(self.password)
        self.LP.clickOnLogin()
        logger.info("*********** Login succesful*******")
        logger.info("********** Strting Add Employee Test********")
        self.emp = Employees(self.driver)
        self.emp.clickOnPmMenu()
        self.emp.clickOnAddEmpolyee()
        self.name = generate_random_text(5)
        self.emp.setFirstName(self.name)
        self.emp.setLastName(self.name)
        self.emp.setId(self.name)
        time.sleep(2)
        self.emp.clickonSave()
        logger.info("******** Saving Employee Info*********")
        logger.info("****** Add Employee validation started********")
        time.sleep(10)
        self.text = self.emp.confirmName()
        if self.text == self.name + " "+self.name:
            logger.info("********* Add Empolyee Test Passed")
            assert True
        else:
            self.driver.save_screenshot("Screenshots/testaddEmployee.png")
            logger.info("********* Add Empolyee Test Failed")
            assert False
        self.driver.close()
        logger.info("*********End of Test_002_AddCustomer ***********")


