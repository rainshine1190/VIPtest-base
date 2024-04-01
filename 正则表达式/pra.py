"""
功能描述：
编写人：liangchao
编写日期：
实现逻辑：
导包
    1-
    2-
    3-

"""
import re
import time

str="""
		<meta http-equiv="X-UA-Compatible" content="IE=edge,chrome=1">
		<meta http-equiv="content-type" content="text/html;charset=utf-8">
		<meta content="always" name="referrer">
        <meta name="theme-color" content="#ffffff">
        <link rel="shortcut icon" href="https://www.baidu.com/favicon.ico" type="image/x-icon" />
        <link rel="icon" sizes="any" mask href="https://www.baidu.com/favicon.ico">
        <link rel="search" type="application/opensearchdescription+xml" href="/content-search.xml" title="百度搜索" />
		<link rel="apple-touch-icon-precomposed" href="https://psstatic.cdn.bcebos.com/video/wiseindex/aa6eef91f8b5b1a33b454c401_1660835115000.png"> 

"""

with open('data.txt','a') as fp:
    for i in range(1000000):
        fp.write(str)

with open('data.txt','r') as fp:

    data = fp.readlines()
    # pattern = re.compile('title="(.*?)" />')
    pattern = 'title="(.*?)" />'
    start = time.time()
    print('开始匹配')
    for i in data:
        # res = pattern.findall(i)
        res = re.findall(pattern,i)

    print('结束匹配')
    end = time.time()
    elpase = end - start
    print(elpase)