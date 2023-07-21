score=int(input())
if score >= 60 :
    print("及格")
else :
    print("不及格")

a = 1
b = 0
while a <= 10:  # while是条件循环，
    b += a  # b+a后，赋值给新的b
    a += 1  # a+1后赋值给新的a
    print(b)

for c in "python":  # c为变量，python为输出结果，for语句顺势打印出来
    print(c)
for v in range(8):  # range()用于数字，类似数组，从0开始固定排序
    print(v)

y = 1
while y < 6:
    j =0
    while j < y:    # 简单逻辑问题
        print("*",end='   ')   # 每达到所需的条件时，按照命令输入
        j +=1
    print("\n") # 上面的print是跟随循环语句的，而这个print是单独独立的，所以当条件
    # 不符时，则会执行命令，输入一调空的代码
    y +=1


for k in "python":
    if k == 'o':
        break   # 碰到o，break结束语句
    print(k,end='')
print()
for u in "python":
    if u =='o':
      continue # 碰到o，continue，自动跳过
    print(u,end='')