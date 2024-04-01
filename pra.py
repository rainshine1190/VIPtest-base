import re,requests

url='http://www.baidu.com'
res = requests.get(url)
data = res.text
encoding = res.encoding
print(encoding)
data = res.content.decode('utf-8')
print(data)
#正则表达式
pattern = '写提取目标的正则'
result = re.findall(pattern,data)
print(result)