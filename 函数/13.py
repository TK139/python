def a(b):
    b =str(b)
    if b[0] ==b[-1] and b[1] ==b[-2]:
        print("回文数")
    else:
        print("bushi")
b = int(input())
a(b)
