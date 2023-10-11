import os
import re
import base64
import requests
import argparse
from bs4 import BeautifulSoup

def get_img_urls(BASE_URL, seach, start=0, num=100, step=35):
    """获取图片链接列表
    
    Args:
    - BASE_URL (str): 基础URL。
    - seach (str): 搜索关键字。
    - start (int): 开始的偏移量。默认为0。
    - num (int): 总图片数量。默认为100。
    - step (int): 每一步的数量。默认为35。
    
    Returns:
    - list: 图片链接列表。
    """
    
    all_image_links = []
    
    # 遍历指定的数量和步长来获取图片链接
    for offset in range(start, num, step):
        # 设置请求参数
        params = {
            'q': seach,
            'first': offset,
            'count': step,
            'cw': 1177,
            'ch': 977,
            'relp': 35,
            'datsrc': 'I',
            'layout': 'RowBased_Landscape',
            'mmasync': 1
        }
        
        # 发起请求
        response = requests.get(BASE_URL, headers=HEADERS, params=params)
        if response.status_code != 200:
            print(f"请求失败，错误码{response.status_code}")
            exit()
        
        # 使用BeautifulSoup解析响应内容
        soup = BeautifulSoup(response.content, 'html.parser')
        
        # 获取图片标签
        img_tags = soup.find_all("img", class_=re.compile(r".*mimg.*"))
        # 从标签中提取图片链接
        img_urls = [img.get("data-src") or img["src"] for img in img_tags]
        
        # 扩展链接列表
        all_image_links.extend(img_urls)

    return all_image_links

def print_url(all_image_links, print_):
    """打印图片链接
    
    Args:
    - all_image_links (list): 图片链接列表。
    - print_ (bool): 是否打印标志。
    """
    
    if print_:
        for i in all_image_links:
            print(i)
        print(len(all_image_links))

def save_image(img_link, filename):
    """保存图片到文件
    
    Args:
    - img_link (str): 图片链接。
    - filename (str): 保存的文件名。
    """
    
    if img_link.startswith("data"):
        data = img_link.split(",")[1]
        img_b = base64.b64decode(data)
    elif img_link.startswith("http"):
        response = requests.get(img_link, headers=HEADERS)
        img_b = response.content
    else:
        print(f"{img_link}: 链接不是data也不是http")
        return False

    with open(filename, 'wb') as f:
        f.write(img_b)



HEADERS = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/117.0.0.0 Safari/537.36 Edg/117.0.2045.60"
}

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='爬取并保存图片。')
    parser.add_argument("-s", '--seach', default="口罩 人们", help='搜索关键字。')
    parser.add_argument('--num', type=int, default=5, help='总图片数量。')
    parser.add_argument('--step', type=int, default=5, help='每一步的数量。')
    parser.add_argument('--start', type=int, default=0, help='开始的偏移量。')
    parser.add_argument('--save_dir', default='img', help='保存目录。')
    parser.add_argument('--save_name', default='0000_%s.jpg', help='保存文件名格式。')
    parser.add_argument('--print', action='store_true', help='打印图片链接。')
    parser.add_argument('--nosave', action='store_true', help='不保存图片。')
    parser.add_argument('--BASE_URL', default="https://www.bing.com/images/async", help='基础URL。')

    args = parser.parse_args()
    
    # 使用参数来获取图片链接
    all_image_links = get_img_urls(args.BASE_URL, args.seach, start=args.start, num=args.num, step=args.step)

    # 根据参数来决定是否打印图片链接
    print_url(all_image_links, args.print)
    
    # 根据参数来决定是否保存图片
    if not args.nosave:
        if not os.path.exists(args.save_dir):
            os.mkdir(args.save_dir)
        cnt = 0
        for img_link in all_image_links:
            save_path = os.path.join(args.save_dir, args.save_name % str(cnt))
            save_image(img_link, save_path)
            cnt += 1
        print(f"文件写入到{args.save_dir}")



