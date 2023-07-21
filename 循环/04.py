"""
i = 1
j = 1
while i < 10:
    while j < 10:
        print(i,"*",j,"=",i*j,sep="")
        i +=1
        j +=1
"""

a = 1
while a < 10:
    b = 1
    while b <=a:
        # print(f"{a}*{b}={a*b}\t",end="")
        print(b,"*",a,"=",a*b,"\t",end="",sep="")
        b +=1
    a +=1
    print()

for i in range(1,10):
    for j in range(1,i+1):
        print(f"{j}*{i}={i*j}\t",end="")
    print()