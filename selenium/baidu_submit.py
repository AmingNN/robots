import time
import os
import ctypes

import keyboard
from selenium import webdriver
from selenium.webdriver import Keys
from selenium.webdriver.common.by import By

COOIKE_PATH = r"F:\Aming\robot\selenium\cookie"
DOUYIN_URL = "https://www.douyin.com/"
CLASS_TOUXIANG = "H2HjqV3h"


def display_notification(title, message, duration=5):
    """
    Display a Windows 10 toast notification.
    :param title: Notification title
    :param message: Notification message
    :param duration: Duration in seconds for the notification to stay visible
    """
    Shell_NotifyIcon = ctypes.windll.shell32.Shell_NotifyIcon
    NIF_INFO = 0x00000001
    NIIF_INFO = 0x00000001

    class NOTIFYICONDATA(ctypes.Structure):
        _fields_ = (
            ("cbSize", ctypes.c_ulong),
            ("hWnd", ctypes.c_void_p),
            ("uID", ctypes.c_uint),
            ("uFlags", ctypes.c_uint),
            ("uCallbackMessage", ctypes.c_uint),
            ("hIcon", ctypes.c_void_p),
            ("szTip", ctypes.c_char * 64),
            ("dwState", ctypes.c_uint),
            ("dwStateMask", ctypes.c_uint),
            ("szInfo", ctypes.c_char * 256),
            ("uVersion", ctypes.c_uint),
            ("szInfoTitle", ctypes.c_char * 64),
            ("dwInfoFlags", ctypes.c_uint),
            ("guidItem", ctypes.c_byte * 16),
            ("hBalloonIcon", ctypes.c_void_p),
            ("dwLargeIcon", ctypes.c_uint),
            ("dwSmallIcon", ctypes.c_uint),
            ("dwCustomIcon", ctypes.c_uint),
            ("hCustomIcon", ctypes.c_void_p)
        )

    nid = NOTIFYICONDATA()
    nid.cbSize = ctypes.sizeof(NOTIFYICONDATA)
    nid.hWnd = None
    nid.uFlags = NIF_INFO
    nid.szInfo = message.encode("utf-8")
    nid.szInfoTitle = title.encode("utf-8")
    nid.dwInfoFlags = NIIF_INFO
    Shell_NotifyIcon(1, ctypes.byref(nid))


def init_driver(cookie_path):
    """初始化WebDriver，并返回其实例。"""
    abs_path = os.path.abspath(cookie_path)
    options = webdriver.EdgeOptions()
    options.add_experimental_option('excludeSwitches', ['enable-automation'])  # 关闭自动测试字样
    options.add_argument(f"user-data-dir={abs_path}")  # 记录用户数据在目录
    return webdriver.Edge(options=options)


def like_post_if_followed(driver, touxiang_class):
    """如果已关注，则对帖子点赞。"""
    follows = driver.find_elements(By.CLASS_NAME, touxiang_class)
    # 调试
    for f in follows:
        print(f.get_attribute("outerHTML"))

    if follows:
        first_follow = follows[0]

        is_followed = first_follow.get_attribute("hidden")
        print(is_followed)
        print("--------------------------------------------------------------")
        if is_followed:
            driver.find_element(By.CSS_SELECTOR, "body").send_keys('z')
            time.sleep(1)  # 给它一点时间点赞
    else:
        display_notification("提示", "或许是直播", 3)  # 显示3秒的通知
        print("或许是直播")

    driver.find_element(By.CSS_SELECTOR, "body").send_keys(Keys.ARROW_DOWN)
    keyboard.wait("ctrl+z")

def main():
    driver = init_driver(COOIKE_PATH)
    driver.implicitly_wait(2)

    driver.get(DOUYIN_URL)
    driver.maximize_window()

    title = driver.title
    print(title)

    for _ in range(1000):
        time.sleep(2)
        like_post_if_followed(driver, CLASS_TOUXIANG)

    driver.quit()


if __name__ == "__main__":
    main()
