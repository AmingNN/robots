import re
import requests
from bs4 import BeautifulSoup

BASE_URL = "https://www.bing.com/images/async"
QUERY = "口罩 人们"
COUNT = 35
NUM = 300

all_image_links = []

for offset in range(0, NUM, COUNT):  # 获取前500个结果为例
    params = {
        'q': QUERY,
        'first': offset,
        'count': COUNT,
        'cw': 1177,
        'ch': 977,
        'relp': 35,
        'datsrc': 'I',
        'layout': 'RowBased_Landscape',
        'mmasync': 1
    }
    
    response = requests.get(BASE_URL, params=params)
    soup = BeautifulSoup(response.content, 'html.parser')
    
    img_tags = soup.find_all("img", class_=re.compile(r".*mimg.*"))
    img_urls = [img.get("data-src") or img["src"] for img in img_tags]
    all_image_links.extend(img_urls)
    # 找到所有不含data-src或src属性的img标签
    imgs_without_data_src_or_src = [img for img in img_tags if not img.get("data-src") and not img.get("src")]

# 打印这些img标签
for img in imgs_without_data_src_or_src:
    print(img)


for i in all_image_links:
    print(i)

print(len(imgs_without_data_src_or_src))
print(len(all_image_links))