from pageObjects.loginpage import Loginpage
from pageObjects.Recruitment import Recruitment
from utilities.customlogger import LogGen
from utilities.readproperties import Readconfig
from selenium import webdriver
import time
import string
import random

logger = LogGen.loggen()

def generate_random_text(length, chars=string.ascii_letters + string.digits):
    return ''.join(random.choice(chars) for _ in range(length))


class Test_003_addCandidate:
    baseURL = Readconfig.getApplicationURL()
    username = Readconfig.getusername()
    password = Readconfig.getpassword()

    def test_Add_Candidate(self,setup):
        logger.info("************* Test_003_addCandidate ***********")
        self.driver : webdriver.Chrome = setup
        self.driver.get(self.baseURL)
        self.driver.implicitly_wait(10)
        self.driver.maximize_window()
        self.LP =Loginpage(self.driver)
        self.LP.SetUserName(self.username)
        self.LP.SetPassword(self.password)
        self.LP.clickOnLogin()
        logger.info("*********** Login succesful*******")
        logger.info("********** Strting Add Candidate Test********")
        self.rec = Recruitment(self.driver)
        self.rec.clickRecruitmentMenu()
        self.rec.addCandidate()
        name = generate_random_text(5)
        self.rec.setFirstName(name)
        self.rec.setLaseName(name)
        self.rec.clickVacancy()
        time.sleep(2)
        role = self.rec.setRandomRole()
        time.sleep(2)
        self.rec.setEmail(name+"@example.com")
        self.rec.setcontact("12345")
        self.rec.SetDate("2020-15-11")
        self.rec.SaveCandidate()
        logger.info("******** Saving Candidate Info*********")
        time.sleep(10)
        logger.info("****** Add Candidate validation started********")
        act_n = self.rec.getName()
        act_r = self.rec.getRole()
        if act_n == name+ " "+name and act_r == role:
            logger.info("********* Add Candidate Test Passed")
            assert True 
        else:
            self.driver.save_screenshot("Screenshots/testaddCandidatei.png")
            logger.info("********* Add Candidate Test Failed")
            assert False
        self.driver.close()
        logger.info("*********End of Test_003_AddCandidate ***********")
