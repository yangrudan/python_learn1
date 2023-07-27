# -*- coding: utf-8 -*-
""" 
@Time:        2023/7/20 18:14
@Author:      CookieYang
@FileName:    draw00.py
@SoftWare:    CLion
@brief:       功能简介
"""
import requests
import io
import base64
from PIL import Image, PngImagePlugin

if __name__ == '__main__':
    url = "http://48.xxx.xx.163:8080"
    payload = {
        "prompt": "puppy dog",
        "steps": 5
    }
    token = "admin:password"
    encoded_token = base64.b64encode(token.encode("utf-8")).decode("utf-8")
    headers = {
        "Content-Type": "application/json",
        "Authorization": f'Basic {encoded_token}'
    }
    response = requests.post(url=f'{url}/sdapi/v1/txt2img', json=payload, headers=headers)
    r = response.json()
    for i in r['images']:
        image = Image.open(io.BytesIO(base64.b64decode(i.split(",", 1)[0])))
        png_payload = {
            "image": "data:image/png;base64," + i
        }
        response2 = requests.post(url=f'{url}/sdapi/v1/png-info', json=png_payload)
        pnginfo = PngImagePlugin.PngInfo()
        pnginfo.add_text("parameters", response2.json().get("info"))
        image.save('output.png', pnginfo=pnginfo)