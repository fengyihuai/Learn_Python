# -*- coding:UTF-8 -*-
# waiting for perfection
import requests
from lxml import etree
import sys
import os

url = "http://www.ivsky.com/tupian/"

# send a request and return a Response object related to the website
response = requests.get(url)
# Parses an HTML document from a string constan
root = etree.HTML(response.content)
# print(response.content)
# Performs a global XPath query against the document
a_list = root.xpath("//ul[@class='tpmenu']/li/a")
# print(a_list)
#  only download ziranfengguang

# select ziranfengguang
a = a_list[1]
# for a in a_list[1:]:
# text() Represents the text content between the tags
# 表示获取标签之间的文本内容
sub1_title = a.xpath("text()")[0]
# print(type(a))
# Get an attribute from the tag
# 获取标签中的某个属性
sub1_url = a.xpath("@href")[0]
if not sub1_url.startswith("http"):
    sub1_url = "http://www.ivsky.com" + sub1_url
    print(sub1_url)

sub1_response = requests.get(sub1_url)
sub1_root = etree.HTML(sub1_response.content)
# print(sub1_response.content)
sub1_a_list = sub1_root.xpath("//div[@id='sline2']/div/a")
# print(sub1_a_list)

# select tiankong
sub1_a = sub1_a_list[1]
sub2_title = sub1_a.xpath("text()")[0]
# print(sub2_title)
sub2_url = sub1_a.xpath("@href")[0]
if not sub2_url.startswith("http"):
    sub2_url = "http://www.ivsky.com" + sub2_url
    print(sub2_url)

# save pictures
# 建立图片文件夹，如果路径对应的文件夹不存在，（目的防止出现“文件夹已存在，创建失败”）
path = "images/" + sub1_title + "/" +sub2_title
pathHD = "images/" + sub1_title + "/" +sub2_title + "HD"

if not os.path.exists(path):
    os.makedirs(path)

if not os.path.exists(pathHD):
    os.makedirs(pathHD)

sub2_response = requests.get(sub2_url)
sub2_root = etree.HTML(sub2_response.content)

img_list = sub2_root.xpath("//ul[@class='pli']/li/div/a/img")
imgHD_list = sub2_root.xpath("//ul[@class='pli']/li/div/a")

for idx, img in enumerate(img_list):
    src = img.xpath("@src")[0]
    img_response = requests.get(src)
    # The form to name a picture document：
    name = img.xpath("@alt")[0] + "-" + str(idx) + ".jpg"
    f = open(path + "/" + name, "wb")
    f.write(img_response.content)
    f.close()

for idx, imgHD in enumerate(imgHD_list):
    srcHD_url = imgHD.xpath("@href")[0]
    srcHD_url = imgHD_list[0].xpath("@href")[0]
    if not srcHD_url.startswith("http"):
        srcHD_url = "http://www.ivsky.com" + srcHD_url
        print("solved picture:\n" + srcHD_url)
    srcHD_response = requests.get(srcHD_url)
    srcHD_root = etree.HTML(srcHD_response.content)
    srcHD_a_list = srcHD_root.xpath("//*[@id='imgis']")
    srcHD = srcHD_a_list[0].xpath("@src")[0]

    imgHD_response = requests.get(srcHD)
    # The form to name a picture document：
    name = srcHD_a_list[0].xpath("@alt")[0] + "-" + str(idx) + "HD.jpg"
    f = open(pathHD + "/" + name, "wb")
    f.write(imgHD_response.content)
    f.close()