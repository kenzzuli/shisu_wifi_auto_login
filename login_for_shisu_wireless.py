# 上外校园网自动登录 shisu_wireless
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

driver = webdriver.Chrome(executable_path="./chromedriver")
# driver = webdriver.Firefox(executable_path="./geckodriver_mac")
# driver = webdriver.Firefox(executable_path="./geckodriver")
driver.get("http://10.0.0.217")
driver.find_element_by_css_selector("input[type='text'][name='DDDDD']").send_keys("02xxxxxx")
driver.find_element_by_css_selector("input[type='password'][name='upass']").send_keys("Lxxxxxx")
driver.find_element_by_css_selector("input[type='submit'][value='登录']").send_keys(Keys.ENTER)
time.sleep(100)
driver.quit()
