# 上外校园网自动登录 shisu_free/shisu_free_dot1x
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver import FirefoxOptions
import time

opts = FirefoxOptions()
opts.add_argument("--headless")  # 服务器无gui，所以使用headless模式
# driver = webdriver.Chrome(executable_path="./chromedriver")
# driver = webdriver.Firefox(executable_path="./geckodriver_mac", firefox_options=opts)
driver = webdriver.Firefox(executable_path="./geckodriver", firefox_options=opts)
driver.get("http://10.0.0.217")  # 请求上网认证的网页
time.sleep(5)  # 等5s，让页面全部加载成功
# page = driver.page_source  # 获取网页源代码，根据源代码，定位网页元素
# print(page.encode("utf-8"))
# with open('./login.html', mode="w", encoding="utf-8") as f:
#     f.write(page)
driver.save_screenshot("./1.png")  # 原始界面
driver.find_element_by_css_selector("input[type='text'][name='DDDDD']").send_keys("0204xxxxxx")
driver.find_element_by_css_selector("input[type='password'][name='upass']").send_keys("Lxxxxxxxx")
driver.save_screenshot("./2.png")  # 输入账号密码后的界面
# driver.find_element_by_css_selector("input[type='submit'][value='登 录   Login']").send_keys(Keys.ENTER)
# 点击登录
driver.find_element_by_css_selector("input[type='submit'][name='0MKKey']").send_keys(Keys.ENTER)
time.sleep(5)  # 等5s看是否登录成功
driver.save_screenshot("./3.png")  # 登录成功后的界面
time.sleep(30)  # 等30s，退出浏览器
driver.quit()
