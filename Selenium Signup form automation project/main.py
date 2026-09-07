from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach",True)


driver = webdriver.Chrome(options=chrome_options)
driver.get("https://appbrewery.github.io/fake-newsletter-signup/")
f_name = driver.find_element(By.NAME,"fName")
l_name = driver.find_element(By.NAME,"lName")
email = driver.find_element(By.NAME,"email")

f_name.send_keys("Abdul")
l_name.send_keys("Samad")
email.send_keys("okzsamad57@gmail.com")
sign_up = driver.find_element(By.CLASS_NAME,"btn-block")
sign_up.click()


