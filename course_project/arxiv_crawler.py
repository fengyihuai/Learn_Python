# -*- coding:UTF-8 -*-

'''在开源期刊网站https://arxiv.org右上方搜索框搜索
本专业关键词1（例如：unet），搜索条件是，最新发表时间
排序，获得50个数据。将搜索结果中的期刊地址（url链接）
打印到命令行中'''

import re
import requests
import urllib


def main():
    url = "https://arxiv.org/search/?"
    payload = {'query':'electroencephalogram', 'searchtype':'all', 'source':'header'}
    r = requests.get(url, params=payload)
    print(r.status_code, r.url)
    ar_address = re.compile(u"<a href=(.*)>arXiv")
    address_url = ar_address.findall(r.text)




if __name__ == '__main__':
    main()