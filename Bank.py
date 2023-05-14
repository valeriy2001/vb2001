from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
import time

s = Service('c:/users/vb200/downloads/chromedriver.exe')
driver = webdriver.Chrome(service=s)
driver.get(
    "https://idemo.bspb.ru/auth?response_type=code&client_id=1&redirect_uri=https%3A%2F%2Fidemo.bspb.ru%2Flogin%2Fsuccess&prefetch_uri=https%3A%2F%2Fidemo.bspb.ru%2Flogin%2Fprefetch&force_new_session=true&state=%2Fpayments%2Fdomestic")
driver.set_window_size(1440, 900)
driver.find_element(By.ID, "login-button").click()
driver.find_element(By.ID, "login-otp-button").click()
exitbutton = driver.find_element(By.ID, "logout-button")
driver.find_element(By.XPATH, '//*[@id="payments-form"]').click()
driver.find_element(By.XPATH, '//*[@id="show-from-card-to-card-payment-form"]').click()
driver.find_element(By.XPATH, '//*[@id="cards-list-destination-container"]/div/select').click()
driver.find_element(By.XPATH, '//*[@id="cards-list-destination-container"]/div/select/option[5]').click()
money = driver.find_element(By.XPATH, '//*[@id="amount-form-item"]/div/div/input')
money.send_keys("100")
driver.find_element(By.ID, "forward").click()
driver.find_element(By.XPATH, '//*[@id="card-to-card-payment-form"]/div[3]/div/div/div/label/input').click()
#driver.find_element(By.ID, "confirm").click()
# Победить кнопку "Подтвердить" у меня так и не получилось. Пробовал по ID, XPATH, CLASS, NAME. Везде ошибка.
time.sleep(5)