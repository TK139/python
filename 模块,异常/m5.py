def k(a,b):
    print(a+b)

if __name__ == '__main__':
    # main函数可以理解成主函数的意思，因为有他的加持
    # 所以结果只会在m5文件中执行，其他的调用是调不出来的。
    # 另外只要输入一个main就可以输出全部内容了
    k(1,2)

# __all__=[tset_a]表示只能取all里的test_a，用于解决from m3 import *