import time

f = open("D:/学习python/acb.txt","r",encoding="UTF-8")
print(type(f))
# 第一个路径，第二个打开文件模式：r只读，w只用于写入，a用于追加，第三个编码格式
print(f.read(10))   # 读取十个字节，不加东西表示全部读取
print(f.read())     # 前面读取后，自动没有，只能读取之后的
# readlines表示读取文件全部行，readline表示一次读取一行
f.close()    # 表示关闭文件，如果不关，pycharm将一直占用该文件
time.sleep(10)  # 表示睡眠时间，10秒
# with open() as f:   表示自动给close，类似于def函数
# ()内是索取文件的操作，f是你所命名的变量