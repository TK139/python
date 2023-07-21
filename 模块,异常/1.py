try:
    print(name)     # try是错误的
except:
    print("name")   # except是修改后的

try:
    print(name)
except (NameError,ZeroDivisionError) as e:  # 异常类型
    print("出现了变量未定义，或者除以0的异常错误")

try:
    print(name)
    print(1/0)
except Exception as e:  # 捕获全部异常
    print("出现异常")
else:
    print("没有异常")
finally:
    print("有没有异常都要执行")