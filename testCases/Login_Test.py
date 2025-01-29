from pageObjects.loginpage import Loginpage
from utilities.customlogger import LogGen
from utilities.readproperties import Readconfig
from utilities import XLUtils
from selenium import webdriver
import time
from selenium.webdriver.common.by import By


logger = LogGen.loggen()
class Test_001_login:
    baseURL = Readconfig.getApplicationURL()
    path = "testData/login data.xlsx"

    def test_login(self,setup):
        logger.info("************* Test_001_login ***********")
        logger.info("************* verifting login functionality***************")
        self.driver : webdriver.Edge= setup
        self.driver.get(self.baseURL)
        self.driver.maximize_window()
        self.driver.implicitly_wait(10)
        self.LP = Loginpage(self.driver)
        
        n_rows = XLUtils.getRowCount(self.path,"Sheet1")
        statusLST = []
        for r in range(2,n_rows+1):
            username = XLUtils.readData(self.path,"Sheet1",r,1)
            password = XLUtils.readData(self.path,"Sheet1",r,2)
            exp = XLUtils.readData(self.path,"Sheet1",r,3)
            self.LP.SetUserName(username)
            self.LP.SetPassword(password)
            
            self.LP.clickOnLogin()
            time.sleep(2)
            login = self.driver.find_elements(By.XPATH,"//*[@id='app']/div[1]/div/div[1]/div/div[2]/h5")
            if exp =="pass":
                if not login:
                    statusLST.append("pass")
                    logger.info("************* Passed ***********")
                    self.LP.clickOnlogout()
                else:
                    statusLST.append("fail")
                    logger.info("************* Failed ***********")
                    self.driver.save_screenshot("Screenshots\\"+"test_login.png")
            else:
                if not login:
                    statusLST.append("fail")
                    logger.info("************* Failed ***********")
                    self.driver.save_screenshot("Screenshots\\"+"test_login.png")
                    self.LP.clickOnlogout()
                else:
                    if not username:
                        self.driver.refresh()
                    if not password:
                        self.driver.refresh()
                    statusLST.append("pass")
                    logger.info("************* Passed ***********")
        if "fail" not in statusLST:
            logger.info(".............login DDT test passed............")
            assert True
        else:
            logger.info(".............login DDT test failed............")
            assert False
        self.driver.close()
        logger.info("*********End of Test_001_login ***********")

                    

