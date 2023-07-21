def a(a,b):
    result = a+b
    print(result)
a(1,2)  # print必须在函数里写才有效，如果在外面则无效

def a(x,y):
    c = x+y
    return c    # return返回给r
r = a(1,2)   # a的实参给了r  理解：a(1,2)已经给了进去，算出结果为3，然后返回给r，名义上是c但是c和r相同所以返还给r
print(r)    # 这样print可以输出r这个变量了       r已经等于a()这个函数了，所以里面的结果也就是r的了

def a():
    print("ni")
a()
print()

def a(b):
    if b >=18:
        return "l"
    else:
        return None     #   None表示否，一般用于声明无初始内容的变量
o = a(16)
if not o:   # not 否，两个否则表示如果符合这个条件，则
    print("no")
else:
    print("ok")
print()


def a():
    print(1)
def b():
    print(2)
    a()   # 按照缩进原则，先调用b,b从中发现了a然后调用a，所以先2再1，最后3
    print(3)
b()


