import requests
import os
import sys
from datetime import datetime

# 1. 获取课文名
lesson_name = sys.argv[1] if len(sys.argv) > 1 else "池上"

# 2. 伪装浏览器，绕过网站拦截
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/125.0.0.0 Safari/537.36',
    'Referer': 'https://hanchacha.com/',
    'Accept-Language': 'zh-CN,zh;q=0.9'
}

# 3. 爬取网页
url = f"https://hanchacha.com/kewen/{lesson_name}.html"
print("正在爬取：", url)

try:
    # 加了headers和超时，成功率更高
    response = requests.get(url, headers=headers, timeout=30)
    response.raise_for_status()  # 会自动抛出错误，比如404/500
    response.encoding = "utf-8"
    html = response.text
    print("✅ 爬取成功！网页长度：", len(html))
except Exception as e:
    html = f"爬取失败：{str(e)}"
    print("❌ 爬取失败：", str(e))

# 4. 写入文件（直接把爬下来的内容全存进去）
os.makedirs("data", exist_ok=True)
with open(f"data/{lesson_name}.md", "w", encoding="utf-8") as f:
    f.write(f"# 📖 {lesson_name} · 学习笔记\n\n")
    f.write("> 正在努力生成中...\n\n---\n\n")
    f.write("## 📚 课文内容\n\n")
    f.write(html)  # 这里直接写入爬下来的网页内容，不会被覆盖！
    f.write("\n\n---\n\n")
    f.write("## 📝 学习建议\n\n")
    f.write("1. 朗读课文3遍\n2. 标出生字词\n3. 思考课文主要内容\n\n")
    f.write(f"*生成时间：{datetime.utcnow().strftime('%Y-%m-%d %H:%M:%S')}*\n")

print("✅ 笔记文件已保存到 data 文件夹！")
