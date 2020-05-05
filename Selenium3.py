from selenium.webdriver.common.keys import Keys
import time

PATH = "C:\Program Files (x86)\chromedriver.exe"
driver = webdriver.Chrome(PATH)

driver.get("https://techwithtim.net/")

link = driver.find_element_by_link_text("Python Programming")