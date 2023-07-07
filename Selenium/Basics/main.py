import time

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdrivermanager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By

driver = webdriver.Chrome(service=Service(ChromeDriverManager().chrome_driver_base_url))

driver.get("https://www.python.org/")
upcoming_events = driver.find_elements(By.XPATH,"(//ul[@class='menu'])[3]/li")

data_upcoming_events = {}

for event in upcoming_events:
    time = event.find_element(By.TAG_NAME,"time").text
    event_name = event.find_element(By.CSS_SELECTOR,"a").text
    data_upcoming_events[len(data_upcoming_events)]={
        "time":time,
        "name":event_name
    }

print(data_upcoming_events)
driver.quit()
