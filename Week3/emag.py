import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager

browser = webdriver.Chrome(ChromeDriverManager().install())

browser.get('https://emag.ro/#opensearch')
get_element = browser.find_element(by = By.ID, value = "searchboxTrigger")
get_element.send_keys('telefon')
time.sleep(10)
get_element.submit()
