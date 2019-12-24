from random import randint

a = []
b = []
num = 0

time = int(input('输入要进行几个数字排序： '))
for i in range(time):
    a.append(i)

while 1:
    num += 1
    while 1:
        i = randint(0, time - 1)
        if i not in b:
            b.append(i)
        if len(b) == time:
            break

    print(num)
    print(b)
    if a == b:
        print()
        break
    else:
        b.clear()
