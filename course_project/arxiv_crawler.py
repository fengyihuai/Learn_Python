# -*- coding:UTF-8 -*-

'''在开源期刊网站https://arxiv.org右上方搜索框搜索
本专业关键词1（例如：unet），搜索条件是，最新发表时间
排序，获得50个数据。将搜索结果中的期刊地址（url链接）
打印到命令行中
附加要求(二选一)：1 按上述步骤获取关键词2（例如：deeplab）的搜索结果
，将前100个关键词1（unet）的搜索结果和前100个关键词2（deeplab）的搜索结果
分别保存到两个txt文件中，再次读取文件后，使用正则表达式找到两部分搜索结果中
重合的文献地址。代码需要输出准确运行时间，正则匹配越快，作业完成度越高。
2 获取关键词1（unet）搜索页面中前三篇文献的完整描述。包含不限于：名称，
作者，概述，全文等。内容越完整，作业完成度越高。
'''

import re
import requests
import time

# 基于arxiv网站的关键词与显示检索条目可控函数，最终返回对应的
# 文献期刊地址并可将其网址输出到命令行（可选项）
# 注：默认按最新发表时间排序
def key_size_search(keyword, size, printed=False, print_num=0):
    try:
        # arxiv网站的高级检索网站地址
        url = "https://arxiv.org/search/advanced?advanced="
        # 高级检索参数，包括每页显示条数size，和检索词terms-0-term，构造传递的url参数
        payload = {"terms-0-term": "python", \
                   "terms-0-field": "all", "size": "50"}
        # 注：网站默认选择按最新发表时间显示文献条目，无需
        # 再度指定"order":"-announced_date_first"
        # payload = {"terms-0-term": "python", "terms-0-field": "all",\
        #            "size": "50", "order":"-announced_date_first"}
        # 输入检索词
        payload["terms-0-term"] = keyword
        if size in [20, 50, 100, 200]:
            # 输入每页显示条数，仅限20，50，100，200-网站设定
            payload["size"] = str(size)
            # 发送请求，尝试获取对应url网址的网页，返回Response对象
            r = requests.get(url, params=payload)
            print(r.status_code, r.url)
            # 使用正则表达式找出文献期刊地址
            ar_address = re.compile(r"<a href=\"(.*)\">arXiv:[0-9\.]+</a>")
            address_url = ar_address.findall(r.text)

            # printed为bool变量，为真，打印print_num条检索结果
            if printed:
                print("\nkeyword:{}, size:{}, address:".format(keyword, len(address_url)))
                # pirnt_num为输入或输入为0，以检索条目数为打印数
                if print_num == 0:
                    print_num = size
                # for i in range(print_num):
                #     print(address_url[i])
                # 下面的代买执行速度是上面的10倍
                print('\n'.join(address_url[:print_num]))
            # 返回检索到的文献期刊地址
            return address_url
        else:
            print("itmes' size must be 20, 50, 100 or 200!!!")

    except:
        return ""

# 文献期刊地址列表的txt文件保存
def url_save_txt(file_name, url_list):
    # 以“写”方式打开文件"xxx.txt",xxx为检索词，没有就新建
    f = open(file_name+'.txt', 'w')
    # 写文件
    for i_url in url_list:
        f.write("%s\n" % i_url)
    # 关闭文件
    f.close()
    print("%s.txt file is saved\n" % (file_name + ".txt"))

# 两个存储url地址的文献期刊地址相同项的找寻
def read_match_urltxt(file1, file2):
    # 创建两个空列表
    url_list1 = equalurl_list = list()
    # 读出文件1的列表，并按行分割为列表的每个元素
    url_list1 = open(file1, 'r').read().split()
    # 读出文件2，得到文件2内的网址字符串
    url_str2 = open(file2, 'r').read()
    # 网址字符串2中的相同网址，存入相同网址列表中
    # 由用网址列表1的各个元素构造正则表达式，查找
    for i_url in url_list1:
        if re.findall(r'{}'.format(i_url), url_str2):
            equalurl_list.append(i_url)
    # 返回相同网址列表
    return equalurl_list

# 文献的各个描述项的打印输出
def arxiv_description(url):
    try:
        # 发送请求，尝试获取对应url网址（文献期刊地址）的
        # 网页，返回Response对象
        r = requests.get(url)
        # 各个文献描述项的正则表达式
        pattern_list = [r"Title:</span>(.*)</h1>",
                        r"Authors:</span><a.*>(.*)</a>",
                        r"class=\"dateline\">\((.*)\)</div>",
                        r"<td class=\"tablecell comments mathjax\">(.*)</td>",
                        r"<span class=\"primary-subject\">(.*)</span>(.*)</td>",
                        r"arXiv:[\w\.]+</a>.*</td>",
                        r"arXiv:[\w\.]+</a>.*</span>",
                        r"Abstract:</span>(.*)</blockquote>",
                        r"<a href=\"(.*)\"\saccesskey=\"f\""]
        # 各个文献描述项的标记（名称）
        pattern_lable = ["Title", "Authors", "Dateline", "Comments",
                         "Subjects", "Cite as", "or Cite as",
                         "Abstract", "PDF-link"]
        # 文献信息空列表
        info = list()
        # 用正则表达式从网页匹配出各个描述项的内容，其中对re库的某个特殊bug
        # 进行了修正-Abstract（无法识别网页一串字符中的\n），以及构造完整网
        # 址-PDF-link
        for i in range(len(pattern_list) - 2):
            info.append(re.findall(pattern_list[i], r.text)[0])
        info.append(re.findall(pattern_list[i + 1], r.text.replace('\n', '*'))[0])
        info.append(url + re.findall(pattern_list[i + 2], r.text)[0])
        # 打印文献信息
        print("\n>>>Article address:", url)
        for i in range(len(pattern_list)):
            print(pattern_lable[i], ':', info[i])

    except:
        print("error: check the code in arxiv_description!!!")

def main():
    # 问题1代码执行的开始时间
    start = time.clock()
    # 给定专业关键词
    uid = ["electroencephalogram", "event-related potential"]
    # 爬取出第一个检索关键词的前100篇（已按最新发表时间排序）文献期刊地址，
    # 并打印输出前50篇
    k1_adurl = key_size_search(uid[0], 100, printed=True, print_num=50)
    # 将文献期刊地址保存
    url_save_txt(uid[0], k1_adurl)

    # 爬取出第2个检索关键词的前100篇（已按最新发表时间排序）文献期刊地址
    k2_adurl = key_size_search(uid[1], 100)
    # 将文献期刊地址保存
    url_save_txt(uid[1], k2_adurl)

    # 找出两个文献期刊地址的txt存储文件的相同地址
    same_urllist = read_match_urltxt("electroencephalogram.txt", "event-related potential.txt")
    # 打印相同地址
    print("the same urls are:\n{}".format('\n'.join(same_urllist)))

    # 问题1代码结束执行的结束时间
    end = time.clock()


    # 问题2：前三篇关键词1（uid[0]）的文献描述项的打印输出
    for i in range(3):
        arxiv_description(k1_adurl[i])

    # 输出问题1涉及功能代码运行时间
    print("----------------------------------------------------")
    print("\nRunning time for problem 1 is:", end-start)
    print("----------------------------------------------------")

if __name__ == '__main__':
    main()