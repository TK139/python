a = [1,2,3,4,[5,6,7]]
index = a.index(2)  # index查询下标，第几位
print(index)
# b = a.index(5)  # 嵌套的查不出，除非把整个列表打出，里面的元素查不出来
# print(b)
c = a[4].index(6)   # 或者这样
print(c)

i = [1,2,3]
i[1] = 3    # 直接修改值
print(i)

j = [1,2,4,1,12,13,1,2]
print(j.count(1))   # count()内写入列表中的元素，然后统计列表中有几个相同的数
k = len(j)  # 查询列表中有几个元素，len是函数。
print(k)

print(max(j))   # max是最大，min是最小
print(min(j))
