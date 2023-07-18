money=500000
num=None
def main():
    print("查询余额\t按1")
    print("存款\t\t按2")
    print("取款\t\t按3")
    print("推出\t\t按4")
    return input("输入业务")

def cha():
    global money
    print(f"余额为{money}")

def cun(sum):
    global money
    money +=num
    print(money)

def qu(sum):
    global money
    money -=num
    print(money)

while True:
    a=main()
    if a == '1':
        cha()
        continue
    elif   a == '2':
        num=int(input("多少"))
        cun(num)
        continue
    elif a=='3':
        num=int(input("多少"))
        qu(num)
        continue
    else :
        break