import urllib.request
a='https://movie.douban.com/j/chart/top_list?type=25&interval_id=100%3A90&action=&start=0&limit=20'
b={
    'User-Agent':
'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.0.0 Safari/537.36'
}
c=urllib.request.Request(url=a,headers=b)
d=urllib.request.urlopen(c)
e=d.read().decode('utf-8')
print(e)

k=open('i.json','w',encoding='utf-8')
k.write(e)
k.close()

