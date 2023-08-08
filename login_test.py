from selenium import webdriver
from selenium.webdriver.common.by import By

chrome = webdriver.Chrome()

chrome.maximize_window()

chrome.get('https://the-internet.herokuapp.com/login')

username=chrome.find_element(By.ID, "username").send_keys("tomsmith")

password=chrome.find_element(By.ID, "password").send_keys("SuperSecretPassword!")

loginbtn=chrome.find_element(By.XPATH,"/html/body/div[2]/div/div/form/button/i").click()

logoutbtn=chrome.find_element(By.XPATH,'//*[@id="content"]/div/a/i').click()

chrome.quit()

print('SUCCESS - TEST PASSED')