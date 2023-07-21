print("输入一个数字，要求在1~10之间,一共有三次机会")
if int(input()) > 5:
    print("错误，范围在5以下")

    if int(input())<=4:
        print("错误")

        if int(input())< 5:
            print("错误")
        else :
            print("正确")
else:
    print("z")