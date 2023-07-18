import urllib.request
import urllib.parse
def a(page):
    base_url='https://movie.douban.com/j/chart/top_list?type=25&interval_id=100%3A90&action=&'
    data={
        'start':(page-1)*20,
        'limit':20
    }
    date = urllib.parse.urlencode(data)
    url = base_url+data
    print(url)
    headers={
        'User-Agent':
'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.0.0 Safari/537.36 Edg/114.0.1823.67'
    }
    request=urllib.request.Request(url=url,headers=headers)
    return request

def get(request):
    response=urllib.request.urlopen(request)
    connet=response.read().decode('utf-8')
    return connet

def load():
    with open('douba'+str(page) +'.json','w',encoding='utf-8') as fp:
        fp.write(connet)

if __name__ == '__main__':
    lstart=int(input("请输入开始页码"))
    end=int(input("请输入结束页码"))
    for page in range(lstart,end+1):
        request=a(page)
        connet=get(request)
        load(page,connet)