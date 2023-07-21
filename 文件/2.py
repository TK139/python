with open("D:/学习python/acb.txt","r",encoding="UTF-8") as f:
    a=f.read()
    b=a.count("j")  #count可以统计一个字符串的字符数
    print(b)
