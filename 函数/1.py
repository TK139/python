a = "python"
b = "instream"
c = "useing"
def my_len(data):
    count=0
    for i in data:
        count +=1
        print(i)
    print(f"循环{count}次")


my_len(a)
my_len(b)
my_len(c)