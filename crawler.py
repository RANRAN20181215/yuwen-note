import requests
import os
import sys
from datetime import datetime

lesson_name = sys.argv[1] if len(sys.argv) > 1 else "池上"

# 1. 模拟浏览器，绕过拦截（配置了完整的请求头）
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/125.0.0.0 Safari/537.36',
    'Referer': 'https://hanchacha.com/',
    'Accept-Language': 'zh-CN,zh;q=0.9',
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8'
}

# 2. 爬取网页（加了错误日志，能看到失败原因）
url = f"https://hanchacha.com/kewen/{lesson_name}.html"
print("正在爬取：", url)

html = ""
try:
    response = requests.get(url, headers=headers, timeout=30)
    print(f"HTTP状态码：{response.status_code}")  # 关键调试信息
    response.raise_for_status()
    response.encoding = "utf-8"
    html = response.text
    print(f"✅ 爬取成功！网页长度：{len(html)} 字符")
except Exception as e:
    html = f"爬取失败：{str(e)}"
    print(f"❌ 爬取失败：{str(e)}")

# 3. 写入文件（强制把爬取的内容写进去，不会被覆盖）
os.makedirs("data", exist_ok=True)
file_path = f"data/{lesson_name}.md"

with open(file_path, "w", encoding="utf-8") as f:
    f.write(f"# 📖 {lesson_name} · 学习笔记\n\n")
    f.write("> 正在努力生成中...\n\n---\n\n")
    f.write("## 📚 课文内容\n\n")
    # 这里直接写入爬取结果，成功就是网页内容，失败就是错误信息
    f.write(html)
    f.write("\n\n---\n\n")
    f.write("## 📝 学习建议\n\n")
    f.write("1. 朗读课文3遍\n2. 标出生字词\n3. 思考课文主要内容\n\n")
    f.write(f"*生成时间：{datetime.utcnow().strftime('%Y-%m-%d %H:%M:%S')}*\n")

print(f"✅ 文件已保存到：{file_path}")
print(f"文件内容长度：{len(open(file_path, 'r', encoding='utf-8').read())} 字符")
