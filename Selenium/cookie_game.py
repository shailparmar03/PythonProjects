import time

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdrivermanager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By

game_url="http://orteil.dashnet.org/experiments/cookie/"

driver = webdriver.Chrome(service=Service(ChromeDriverManager().chrome_driver_base_url))

driver.get(game_url)
cookie = driver.find_element(By.CSS_SELECTOR,"div #cookie")
timeout = time.time() + 60*5

def check_right():
    store_list = driver.find_elements(By.CSS_SELECTOR,"div #store div")[::-1]
    for item in store_list:
        try:
            item.click()
        except:
            pass

def play_game():
    check_right_time = time.time()+5
    while check_right_time>time.time():
        cookie.click()
    check_right()

while True:
    if timeout<time.time():
        break
    else:
        play_game()

money = driver.find_element(By.CSS_SELECTOR,"div #store div b moni").text
print(f"Money : {money}")
cps = driver.find_element(By.CSS_SELECTOR,"div #cps").text
print(cps)