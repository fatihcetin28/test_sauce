from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from time import sleep

driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))


class Test_Kodlamaio:
    def test_invalid_login(self):
        driver.maximize_window()
        driver.get('https://www.kodlama.io/')
        loginBtn = driver.find_element(By.XPATH, "//*[@id='navbar']/div/div/div/ul/li[3]/a")
        loginBtn.click()

testClass = Test_Kodlamaio()
testClass.test_invalid_login()
while True:
    continue

# //*[@id="navbar"]/div/div/div/ul/li[3]/a
# //*[@id="cf-stage"]/div[6]/label/input