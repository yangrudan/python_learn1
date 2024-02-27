"""
Copyright (c) Cookie Yang. All right reserved.
"""
import requests

data = {'username': '002438',
        'password': "13141996jyD"}
headers = {'user-agent': 'my-app/0.0.1'}
response = requests.post("https://portal.zhejianglab.com/oa/home/login", data=data, headers=headers)
if response.ok:
    print(response.text)
else:
    print("请求失败")