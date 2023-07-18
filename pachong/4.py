import urllib.parse
data = {
    'wd':'周杰伦',
    'sex':'男'
}
a = urllib.parse.urlencode(data)
print(a)