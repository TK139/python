f = open("D:/学习python/bill.txt","r",encoding="UTF-8")
w = open("D:/学习python/bill.txt.bak","w",encoding="UTF-8")
for i in f:
    i = i.strip()   # strip删除开头和结尾的字符，现在是为了删除\n
    if i.split(",")[1] == "100":    # split表示分隔符   ,为分割，所以去我的文件的位次，判断这个字符是否是
        continue    # 跳过
    w.write(i)      # 把i里面符合要求的写入到w(写入文件)这个变量里
    w.write("\n")   # 换行

f.close()
w.close()