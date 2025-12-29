#Note: Sometimes Amazon blocks normal web-scraping

import csv, time, random
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

products = ["laptop", "headphones", "keyboard", "mouse", "phone"]
query = random.choice(products)

service = Service(ChromeDriverManager().install())
driver = webdriver.Chrome(service=service)

driver.get(f"https://www.amazon.in/s?k={query}")
time.sleep(5)

rows = []

items = driver.find_elements(By.CSS_SELECTOR, "div.s-result-item")

for i in items[:10]:
    try:
        title = i.find_element(By.CSS_SELECTOR, "h2 span").text
        price = i.find_element(By.CSS_SELECTOR, ".a-price-whole").text
        rating = i.find_element(By.CSS_SELECTOR, ".a-icon-alt").get_attribute("innerHTML")
        rows.append([title, price, rating])
    except:
        pass

driver.quit()

with open("amazon_products.csv","w",newline="",encoding="utf-8") as f:
    csv.writer(f).writerows([["Title","Price","Rating"], *rows])

print("Saved amazon_products.csv")
