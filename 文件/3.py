a = open("D:/学习python/abd.txt","w",encoding="UTF-8")
a.write("hello")    # write写入文件，可以创建文件，也可以写入东西,但里面的东西他会删除变成你所写的新内容
a.flush()   # flush刷新，必须加上，不然不会出现你的操作
a.close()   # 但是close里面包含flush这个命令可以不加
# w：没有文件他会创建一个文件，如果有了，那就会清空从而改写他

a = open("D:/学习python/abd.txt","a",encoding="UTF-8")
a.write(" world")   # a表示追加，原来的内容不会改变。
a.flush()
a.close()