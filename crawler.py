import requests
import os
import sys

# 这是课文名字
lesson_name = sys.argv[1] if len(sys.argv) > 1 else "池上"

# ====================== 防反爬核心（照着用就行）======================
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36'
}

# 开始爬网页
url = f"https://hanchacha.com/kewen/{lesson_name}.html"
print("正在爬取：", url)

try:
    response = requests.get(url, headers=headers, timeout=20)
    response.encoding = "utf-8"
    html = response.text
except:
    html = "无法获取内容"

# 保存内容
os.makedirs("data", exist_ok=True)
with open(f"data/{lesson_name}.md", "w", encoding="utf-8") as f:
    f.write(f"# {lesson_name} 笔记\n\n")
    f.write(html)

print("保存完成！")
