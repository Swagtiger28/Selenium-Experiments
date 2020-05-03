from selenium import webdriver 
PATH = "C:\Program Files (x86)\chromedriver.exe"
driver = webdriver.Chrome(PATH)

driver.get("https://youtu.be/dQw4w9WgXcQ?t=1")
print(driver.title)
driver.quit()
# driver.close() # Closes current tab
# driver.quit()  # Closes browser