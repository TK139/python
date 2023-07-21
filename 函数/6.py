def a():
    b=1
    print(b)
def c():
    d=2
    print(d)
a()
c()
print()

a =1
def b():
    print(a)
    def d():    # 形参
        print(a)
    d() # 标记一个d(),作为实参，如果不加的话，将无法输出
b()