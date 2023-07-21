# 尝试把一个文件复制粘贴到另一个文件
f = open("D:/学习python/a.txt","r",encoding="UTF-8")
w = open("D:/学习python/a.txt.bak","w",encoding="UTF-8")
i = f.read()    # 这里把f文件全部读取完，然后把他声明一个变量,这个变量里有我的东西
w.write(i)      # 写入有个特性：一般来说写入的东西是字符串。 所以它可以写入变量所以实现
print(i)        # 输出我读取的东西
f.close()
w.close()