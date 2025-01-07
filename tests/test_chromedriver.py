from selenium import webdriver
from selenium.webdriver.chrome.service import Service

chromedriver_path = r"C:\chromedriver.exe"
service = Service(chromedriver_path)
driver = webdriver.Chrome(service=service)

driver.get("https://www.google.com")
print("Chromedriver is working!")
driver.quit()
