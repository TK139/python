import m4
m4.a(1,2)   # 调用m3文件里的函数，文件m3最后命令是print(x+y),所以最后结果输出两数相加之和
from m4 import a
a(1,2)

from m5 import k