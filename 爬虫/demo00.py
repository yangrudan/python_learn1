"""
Copyright (c) Cookie Yang. All right reserved.
"""
import requests


response = requests.get("http://books.toscrape.com/")
if response.ok:
    print(response.text)
else:
    print("请求失败")