from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from time import sleep

driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
driver.get('https://www.google.com/')
input = driver.find_element(By.XPATH,'/html/body/div[1]/div[2]/div/img')

input.screenshot('scrshot.png')

print(input)
driver.maximize_window()

sleep(10)
