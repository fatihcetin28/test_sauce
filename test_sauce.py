from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from time import sleep
from selenium.webdriver.support.wait import WebDriverWait as wait
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.common.action_chains import ActionChains as AC

class Test_Sauce:
    def __init__(self):
        self.driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
        self.driver.maximize_window()
        self.driver.get("https://www.saucedemo.com/")

    def test_invalid_login(self):
        wait(self.driver,10).until(ec.visibility_of_element_located((By.ID,"user-name")))
        usernameInput = self.driver.find_element(By.ID,'user-name')
        wait(self.driver,10).until(ec.visibility_of_element_located((By.ID,"password")))
        passwordInput = self.driver.find_element(By.ID,"password")

        usernameInput.send_keys(1)
        passwordInput.send_keys(2)

        loginBtn =self.driver.find_element(By.ID,"login-button")
        loginBtn.click()

        errorMessage = self.driver.find_element(By.XPATH,"//*[@id='login_button_container']/div/form/div[3]/h3").text
        testResult = errorMessage == "Epic sadface: Username and password do not match any user in this service"
        print(testResult)


    def test_valid_login(self):
        self.driver.get("https://www.saucedemo.com/")
        wait(self.driver,10).until(ec.visibility_of_element_located((By.ID,"user-name")))
        usernameInput = self.driver.find_element(By.ID,'user-name')
        wait(self.driver,10).until(ec.visibility_of_element_located((By.ID,"password")))
        passwordInput = self.driver.find_element(By.ID,"password")

         #Action Chains
        actions = AC(self.driver)
        actions.send_keys_to_element(usernameInput,'standard_user')
        actions.send_keys_to_element(passwordInput,'secret_sauce')
        actions.perform()
        # usernameInput.send_keys('standard_user')
        # passwordInput.send_keys('secret_sauce')

        loginBtn = self.driver.find_element(By.ID,"login-button")
        loginBtn.click()
        sleep(30)
       

        


        
    
ts = Test_Sauce()

ts.test_invalid_login()
ts.test_valid_login()

# //*[@id="login_button_container"]/div/form/div[3]/h3/text()