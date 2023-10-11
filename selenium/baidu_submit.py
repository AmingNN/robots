import time, os
from selenium import webdriver
from selenium.webdriver.common.by import By


def init(cookie_path):
    cookie_path = os.path.abspath(cookie_path)
    options = webdriver.EdgeOptions()
    options.add_experimental_option('excludeSwitches', ['enable-automation'])  # 关闭自动测试字样
    options.add_argument(f"user-data-dir={cookie_path}")  # 记录用户数据在目录
    # options.add_argument("--auto-open-devtools-for-tabs")  # 自动打开开发者工具

    driver = webdriver.Edge(options=options)
    return driver


cooike_path = r"F:\Aming\robot\selenium\cookie"
driver = init(cooike_path)
driver.implicitly_wait(0.5)

url = "https://www.selenium.dev/zh-cn/documentation/webdriver/troubleshooting/errors/driver_location/"
# 添加cookie
driver.get(url)

driver.maximize_window()

title = driver.title
print(title)

for i in range(1, 10):
    driver.execute_script("window.scrollTo(0, 500);")
    # driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
    time.sleep(1)

# driver.find_element(By.XPATH, '//*[@id="nav-searchform"]/div[1]/input').send_keys(
#     "selenium say hello to you")

time.sleep(10000)
driver.quit()
