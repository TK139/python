import pickle

a =[1,2,3]
c =[1,6,0]
b =[5,a,c]
print(b[1])    # 环环嵌套,小列表包含在大列表之中

k =[3,6,9,11,13,15]
print(k[1:4])   # 原理相同，不包括最后的数
print(k[1:4:2])  # 中间隔开
print(k[2:])    # 保留开头
print(k[:3])    # 去掉结尾

n = [1,2,3,4,5]
for l in n:
    print(l)

o = [1,2,3,4]
print(5 in o)   # 5在不在 o之中
