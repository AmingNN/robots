import re
import requests
from bs4 import BeautifulSoup

HEADERS = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36"
}

URL = "https://www.bing.com/images/search?q=%E5%8F%A3%E7%BD%A9+%E4%BA%BA%E4%BB%AC&qs=n&form=QBIR&sp=-1&lq=0&pq=%E5%8F%A3%E7%BD%A9+renm&sc=10-7&cvid=B3A98C9596784BFB967E1444609D0DF6&ghsh=0&ghacc=0&first=1&cw=1177&ch=977"

# 请求主页面
response = requests.get(URL, headers=HEADERS)

soup = BeautifulSoup(response.text, 'lxml')

# 从页面内容中解析含有"mimg"类的图片URL
img_tags = soup.find_all("img", class_=re.compile(r".*mimg.*"))

# 提取img标签的data-src或src属性
img_urls = [img.get("data-src") or img["src"] for img in img_tags ]
for i in img_urls:
    print(i)

# 打印提取到的图片URL数量
print(len(img_urls))

# 打印获取到的图片URL
# for url in img_urls:
#     print(url)
