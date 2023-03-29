from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from time import sleep
from selenium.webdriver.support.wait import WebDriverWait as wait
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.common.action_chains import ActionChains as AC
import pytest
from pathlib import Path
from datetime import date

class Test_demo:
    #Her testten önce çağrılır
    def setup_method(self):
        self.driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
        self.driver.maximize_window()
        self.driver.get("https://www.saucedemo.com/")

        self.folderPath =str(date.today()) 
        Path(self.folderPath).mkdir(exist_ok=True)
        
        #Her testten sonra çağrılır
    def teardown_method(self):
        self.driver.quit()

    def getData():#decoratorlerden çağırdığımız fonk a self parametresi vermiyoruz
        
        return [("1","2"),("kulAdi","sifre")]

    def test_demo(self):
        assert True
    
    def waitForElementVisibility(self, locator, timeout=5):
        wait(self.driver,timeout).until(ec.visibility_of_element_located(locator))

    # @pytest.mark.skip()
    @pytest.mark.parametrize("username,password",getData())
    def test_invalid_login(self, username, password):

        self.waitForElementVisibility((By.ID,"user-name"))
        usernameInput = self.driver.find_element(By.ID,'user-name')

        self.waitForElementVisibility((By.ID,"password"))
        passwordInput = self.driver.find_element(By.ID,"password")

        usernameInput.send_keys(username)
        passwordInput.send_keys(password)

        loginBtn =self.driver.find_element(By.ID,"login-button")
        loginBtn.click()

        errorMessage = self.driver.find_element(By.XPATH,"//*[@id='login_button_container']/div/form/div[3]/h3").text
        self.driver.save_screenshot(f"{self.folderPath}/test-invalid-login-{username}-{password}.png")
        assert errorMessage == "Epic sadface: Username and password do not match any user in this service"

    def test_valid_login(self):
        
        self.waitForElementVisibility((By.ID,"user-name"))
        usernameInput = self.driver.find_element(By.ID,'user-name')
        self.waitForElementVisibility((By.ID,"password"))
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
        self.driver.execute_script('window.scrollTo(0,500)')
        sleep(7)