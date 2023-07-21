c = 10000
for k in range(1, 21):
    import random
    a = random.randint(1, 10)
    if a < 5:
        print(f"员工{k},绩效{a}，不发工资")
        continue

    if a >= 5:
        print(f"员工{k},绩效{a}，发工资，余额还剩{c}")
        c -= 1000

    if c <= 0:
        print("余额不足")
        break
