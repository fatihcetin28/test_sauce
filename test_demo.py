from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from time import sleep
from selenium.webdriver.support.wait import WebDriverWait as wait
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.common.action_chains import ActionChains as AC
import pytest

class Test_demo:
    #Her testten önce çağrılır
    def setup_method(self):
        self.driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
        self.driver.maximize_window()
        self.driver.get("https://www.saucedemo.com/")
        #Her testten sonra çağrılır
    def teardown_method(self):
        self.driver.quit()

    def test_demo(self):
        assert True
    

    # @pytest.mark.skip()
    @pytest.mark.parametrize("username,password",[("1","2"),("kulAdi","sifre")])
    def test_invalid_login(self, username, password):
        wait(self.driver,10).until(ec.visibility_of_element_located((By.ID,"user-name")))
        usernameInput = self.driver.find_element(By.ID,'user-name')
        wait(self.driver,10).until(ec.visibility_of_element_located((By.ID,"password")))
        passwordInput = self.driver.find_element(By.ID,"password")

        usernameInput.send_keys(username)
        passwordInput.send_keys(password)

        loginBtn =self.driver.find_element(By.ID,"login-button")
        loginBtn.click()

        errorMessage = self.driver.find_element(By.XPATH,"//*[@id='login_button_container']/div/form/div[3]/h3").text
        assert errorMessage == "Epic sadface: Username and password do not match any user in this service"
       