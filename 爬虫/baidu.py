"""
Copyright (c) Cookie Yang. All right reserved.
"""
import urllib.request


response = urllib.request.urlopen('http://www.baidu.com')
print(response.read().decode('utf-8'))