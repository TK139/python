import urllib.request
#使用urllib获取百度的源码
url = 'http://www.baidu.com'
#定义一个url  访问你想要访问的地址
response = urllib.request.urlopen(url)
#模拟浏览器向服务器发送请求
#content = response.read().decode('utf-8')
#read读，decode（‘编码的格式’）
print(response.read().decode('utf-8'))
# read readline readlines getcode geturl getheaders