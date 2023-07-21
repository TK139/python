a = 1
def b():
    global a
    a +=1
    print(a)
b()
print(a)
print()

d = 1   # 全局变量
def a():
    d =2    # 局部变量
    print(d)
a()
print(d)    # 所以还是全局变量的值，想要变化就在局部赋值的时候，glabal