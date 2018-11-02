# -*- coding:UTF-8 -*-
# 5、从PubMed的HTML页面上提取标题和摘要文本。
#     http://www.ncbi.nlm.nih.gov/pubmed?
#     '18235848', '22607149', '22405002', '21630672'
from urllib import parse
import requests
import re


# http://www.ncbi.nlm.nih.gov/pubmed?
# '18235848', '22607149', '22405002', '21630672'

# Get url text
def getHtmlText(url):
    try:
        r = requests.get(url, timeout=30)
        r.raise_for_status()
        return r.text
    except:
        return ""

# def rehtml(unfo, html):
#     title = str(re.findall(r'<h1>(.*)</h1>', html, re.S))[6:-7]
#     abstract = str(re.findall(r'<h3>Abstract</h3>(.*)</p></div>', html, re.S))[19:-2]
#     unfo.append(title)
#     unfo.append(abstract)

# def main(matches):
def main():
    uids = ['18235848', '22607149', '22405002', '21630672']
    title = re.compile(r'<h1>(.*)</h1>')
    abstract = re.compile(r'<h3>Abstract</h3>(.*)</p></div>')
    for uid in uids:
        dic = {'term':uid}
        uinfo = list()
        # Transform request data(dictionary class) to url encoding
        data = parse.urlencode(dic)
        # 1. get source code of this html
        url = 'http://www.ncbi.nlm.nih.gov/pubmed?'+data
        print('Website is: '+url)
        html = getHtmlText(url)
        # 3. parsing source code of html
        # rehtml(uinfo, html)
        uinfo.append(str(title.findall(html))[6:-7])
        uinfo.append(str(abstract.findall(html))[19:-2])
        print("Title is:" + uinfo[-2])
        print("Abstract is:" + uinfo[-1])

if __name__ == '__main__':
    # matches = [r'<h1>.*</h1>', r'<h3>Abstract</h3>.*</p></div>']
    # main(matches)
    main()
