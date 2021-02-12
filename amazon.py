
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from openpyxl import Workbook

url = 'https://www.amazon.in/'

driver = webdriver.Chrome(r'C:\Users\varun\OneDrive\Documents\python projects\chromedriver.exe')
driver.get(url)
driver.maximize_window()
driver.find_element(By.XPATH, "//input[@id='twotabsearchtextbox']").send_keys("oppo mobiles")
driver.find_element(By.XPATH, "//input[@value='Go']").click()
driver.find_element(By.XPATH, "//span[text() = 'Oppo']").click()
phone_models = driver.find_elements(By.XPATH, "//span[@class='a-size-medium a-color-base a-text-normal']")
all_prices = driver.find_elements(By.XPATH, "//span[@class='a-price-whole']")

phone_models_list = []
prices_list = []

for phone in phone_models:
	phone_models_list.append(phone.text)
	
for price in all_prices:
	prices_list.append(price.text)
	
wb = Workbook()
sheet = wb.active
sheet["A1"] = "Phone model"
sheet["B1"] = "Price"
for data in zip(phone_models_list, prices_list):
	print(data)
	sheet.append(data)

wb.save("oppo.xlsx")
driver.quit()


