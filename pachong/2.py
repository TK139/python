import urllib.request
url_page = 'http://www.baidu.com'
#urlretrieve('路径，可以是变量名'，‘文件名’)
urllib.request.urlretrieve(url_page,'baidu.html')
#html源码
urllib_img = 'https://tse3-mm.cn.bing.net/th/id/OIP-C.pL7chy0YVCShKlT1MCBsYwHaEK?w=293&h=180&c=7&r=0&o=5&dpr=2&pid=1.7'
urllib.request.urlretrieve(urllib_img,'deemo.jpg')
#图片
urllib_mp4 = 'https://www.bilibili.com/video/BV1ix411e7vC?t=0.0'
urllib.request.urlretrieve(urllib_mp4,'deemo.mp4')
#视频