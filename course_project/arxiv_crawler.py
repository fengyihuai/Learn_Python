# -*- coding:UTF-8 -*-

'''在开源期刊网站https://arxiv.org右上方搜索框搜索
本专业关键词1（例如：unet），搜索条件是，最新发表时间
排序，获得50个数据。将搜索结果中的期刊地址（url链接）
打印到命令行中
附加要求(二选一)：...
'''

import re
import requests
import urllib

def key_size_search(keyword, size, printed=False, print_num=0):
    try:
        url = "https://arxiv.org/search/advanced?advanced="
        payload = {"terms-0-operator": "AND", "terms-0-term": "python", \
                   "terms-0-field": "all", "size": "50"}

        payload["terms-0-term"] = keyword
        if size in [20, 50, 100, 200]:

            payload["size"] = str(size)

            r = requests.get(url, params=payload)
            print(r.status_code, r.url)
            ar_address = re.compile(r"<a href=\"(.*)\">arXiv:[0-9\.]+</a>")
            address_url = ar_address.findall(r.text)

            if printed:
                print("\nkeyword:{}, size:{}, address:".format(keyword, len(address_url)))
                if print_num == 0:
                    print_num = len(address_url)
                # for i in range(print_num):
                #     print(address_url[i])
                print('\n'.join(address_url[:print_num]))

            return address_url
        else:
            print("itmes' size must be 20, 50, 100 or 200")

    except:
        return ""

# 1 按上述步骤获取关键词2（例如：deeplab）的搜索结果
# ，将前100个关键词1（unet）的搜索结果和前100个关键词2（deeplab）的搜索结果
# 分别保存到两个txt文件中，再次读取文件后，使用正则表达式找到两部分搜索结果中
# 重合的文献地址。代码需要输出准确运行时间，正则匹配越快，作业完成度越高。
def url_save_txt(file_name, url_list):
    f = open(file_name+'.txt', 'w')
    for i in range(len(url_list)):
        f.write("%s\n" % url_list[i])
    f.close()
    print("%s.txt file is saved\n" % (file_name + ".txt"))

def read_match_urltxt(file_name1, file_name2):
    url_list1 = equalurl_list = list()
    url_list1 = open(file_name1, 'r').read().split()
    url_str2 = open(file_name2, 'r').read()

    for i in range(len(url_list1)):
        if re.findall(r'{}'.format(url_list1[i]), url_str2):
            equalurl_list.append(url_list1[i])
    return equalurl_list


# 2 获取关键词1（unet）搜索页面中前三篇文献的完整描述。包含不限于：名称，
# 作者，概述，全文等。内容越完整，作业完成度越高。
def arxiv_description(url):
    try:
        r = requests.get(url)
        pattern_list = [r"Title:</span>(.*)</h1>",
                        r"Authors:</span><a.*>(.*)</a>",
                        r"class=\"dateline\">\((.*)\)</div>",
                        r"<td class=\"tablecell comments mathjax\">(.*)</td>",
                        r"<span class=\"primary-subject\">(.*)</span>(.*)</td>",
                        r"arXiv:[\w\.]+</a>.*</td>",
                        r"arXiv:[\w\.]+</a>.*</span>",
                        r"Abstract:</span>(.*)</blockquote>",
                        r"<a href=\"(.*)\"\saccesskey=\"f\""]
        pattern_lable = ["Title", "Authors", "Dateline", "Comments",
                         "Subjects", "Cite as", "or Cite as",
                         "Abstract", "PDF-link"]

        info = list()
        for i in range(len(pattern_list) - 2):
            info.append(re.findall(pattern_list[i], r.text)[0])
        info.append(re.findall(pattern_list[i + 1], r.text.replace('\n', '*'))[0])
        info.append(url + re.findall(pattern_list[i + 2], r.text)[0])

        print("\n>>>Article address:", url)
        for i in range(len(pattern_list)):
            print(pattern_lable[i], ':', info[i])

    except:
        return ""

def main():
    uid = ["electroencephalogram", "event-related potential"]

    k1s2_adurl = key_size_search(uid[0], 100, printed=True, print_num=50)
    url_save_txt(uid[0], k1s2_adurl)

    k2s2_adurl = key_size_search(uid[1], 100)
    url_save_txt(uid[1], k2s2_adurl)

    same_urllist = read_match_urltxt("electroencephalogram.txt", "event-related potential.txt")
    print("the same urls are:\n{}".format('\n'.join(same_urllist)))

    # k1s2_adurl = key_size_search(uid[0], 100, printed=True, print_num=50)
    for i in range(3):
        arxiv_description(k1s2_adurl[i])

if __name__ == '__main__':
    main()