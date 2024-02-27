from selenium import webdriver
from bs4 import BeautifulSoup

# 创建一个浏览器对象
driver = webdriver.Chrome()

# 打开网页
driver.get("https://www.zhejianglab.com/home")

# 等待页面加载完成
driver.implicitly_wait(10)  # 等待10秒钟，如果元素加载完成则继续执行

# 获取页面源代码
html_content = driver.page_source

# 使用BeautifulSoup解析HTML内容
soup = BeautifulSoup(html_content, 'html.parser')

# 提取新闻标题和链接
news_list = []
for article in soup.find_all('article'):
    title = article.find('h2').text.strip()
    link = article.find('a')['href']
    news_list.append({'title': title, 'link': link})

# 打印新闻标题和链接
for news in news_list:
    print(news['title'], news['link'])

# 关闭浏览器
driver.quit()