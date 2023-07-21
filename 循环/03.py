import random
num =random.randint(1,50)
count=0
flag = True
while flag:
    a = int(input("输入你想要的数字"))
    count +=1
    if a ==num :
        print("恭喜你，第一次就猜对了")
        flag = False
    else :
        if a>num:
            print("数字大了")
        elif a<num:
            print("数字小了")
print(f"恭喜你猜对了，猜了{count}次")




