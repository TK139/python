name="tk"
print("我的名字是"+name)  # +号连接前面是字符串，后面是上一个命名量

name="i"
print("%s"%name)    # 跟c一样，%s表示把字符串放入
class_num=45    # class表示关键词，需要用下划线命名
float=3.21
print("%d,%7.3f"%(class_num,float))  # %d表示把整数代入，%f表示浮点数，跟c一样
#  7在这里表示宽度，此数字有5个占位，为了补齐在前面加上两个，7.3；7是宽度3是小数位
