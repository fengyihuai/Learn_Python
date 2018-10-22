# -*- coding:UTF-8 -*-
import requests

r1 = requests.get('http://www.jianshu.com/')
print(r1.text)

payload = {'newwindow':'1', 'q':'python', 'oq':'python'}
r2 = requests.get("https://www.google.com/search", params=payload)
print(r2.text)