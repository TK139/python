a = int(input())
b = str(a)
i = 0
while i <= len(b):  # len()计算该字符的位数
    i +=1
print(i-1)
c = len(b)
print(c)
print()

def a():
    b = ['q','w','e','r']
    i = 0
    while i < len(b):
        print(b[i])   # 顺次下打印出来
        i +=1
a()
print()

def l():
    p =['t','y','u']
    for i in p:
        print(i)
l()