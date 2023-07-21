money = 500000
def a(num):
    print("查询余额")

def b(nem):
    global money
    money += nem
    print("取款")

def c (nim):
    money -= nim
    print("去款")

def main():
    print("输入您要办理的业务1234")
    return int(input(""))

while True:
    i =main()
    if i ==1:

