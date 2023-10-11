# 图片爬取工具

这是一个使用Python编写的图片爬取工具，它从指定的URL爬取图片，并提供选项来打印图片链接或将图片保存到文件中。

## 需要的第三方库

- `requests`: 用于发起HTTP请求。
- `BeautifulSoup`: 用于解析HTML并从中提取信息。
- `argparse`: 用于处理命令行参数。
- `pillow`: 用于绘图。// 必应每日图片（day_bing_img.py）需要

您可以使用pip安装上述库：

```bash
pip install requests beautifulsoup4 argparse pillow
```

## 使用方法

1. 运行工具:

```bash
python get_img.py --BASE_URL [YOUR_URL] --seach [YOUR_SEARCH_KEYWORD] --save_dir [YOUR_DIRECTORY] --save_name [YOUR_FILENAME_FORMAT] [--print_] [--save] --start [YOUR_START_OFFSET] --step [YOUR_STEP_SIZE] --num [YOUR_TOTAL_NUMBER]
```

其中:

- `--BASE_URL`：基础URL。默认为"https://www.bing.com/images/async"。
- `-s --seach`：搜索关键字。默认为"口罩 人们"。
- `--save_dir`：保存目录。默认为"img"。
- `--save_name`：保存文件名格式。默认为"mask_%s.jpg"。%s为插入为，递增
- `--print_`：是否打印图片链接。
- `--save`：是否保存图片。
- `--start`：开始的偏移量。默认为0。
- `--step`：每一步的数量。默认为5。
- `--num`：总图片数量。默认为5。

例如:

```bash
python get_img.py --seach "夏天" --save --print --num 20
```

2. 输出将显示所有找到的图片链接，然后它们将被保存到默认的"img"目录中。

## 注意

此工具目前仅在Bing图片上进行了测试。不同的网站可能有不同的结构和参数，因此在其他网站上使用此工具时可能需要修改。

