import  urllib.request
a = 'https://www.baidu.com'
b = {
'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.0.0 Safari/537.36 Edg/114.0.1823.67'
}#https加密协议，采用反爬（UA）
c = urllib.request.Request(url=a, headers=b)
d = urllib.request.urlopen(c)
e = d.read().decode('utf-8')
print(e)
import urllib.parse
name = urllib.parse.quote('')
#ascii码编码转换