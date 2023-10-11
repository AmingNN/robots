# 必应每日图片
from io import BytesIO

import requests
import json
from PIL import Image

params = {
    "format": "js",  # 返回数据格式，不存在返回xml格式, js (一般使用这个，返回json格式), xml（返回xml格式）
    "idx": 0,  # 请求图片截止天数,0 今天,-1 截止中明天 （预准备的）,1 截止至昨天，类推（目前最多获取到7天前的图片）
    "n": 1,  # 1-8 返回请求数量，目前最多一次获取8张
    "mkt": "zh-CN"  # 地区
}

api = "https://cn.bing.com/HPImageArchive.aspx"
res = requests.get(api, params=params).json()
path = "https://cn.bing.com" + res.get("images")[0].get("url")

# 美化输出
pretty_json = json.dumps(res, indent=4, ensure_ascii=False)
print(pretty_json)

# 画图
img_b = BytesIO(requests.get(path).content)
img = Image.open(img_b)
img.show()
