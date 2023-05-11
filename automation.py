from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
from bs4 import BeautifulSoup
from xlutils.copy import copy
import re
import xlwt
import time
import xlrd
from webdriver_manager.chrome import ChromeDriverManager

driver = webdriver.Chrome()
driver.get("http://www.python.org")
assert "Python" in driver.title
elem= driver.find_element(By.NAME, 'q')
elem.clear()
elem.send_keys("pycon")
elem.send_keys(Keys.RETURN)
