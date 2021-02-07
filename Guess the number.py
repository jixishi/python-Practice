# coding=utf-8
import random

a = random.randint(1, 9)
b = random.randint(1, 9)
a = ((a * b + a / b) * a+b*5)*4
a = int(a)
yes = "猜对了"
no = "猜错了,"
print("######################")
print("#      猜数字游戏      #")
print("#      范围不定哦      #")
print("#      可以二分法      #")
print("######################")
c = int(input("请输入猜测值："))
if c == a:
    print(yes)
else:
    while c != a:
        if c > a:
            print(no + "太大了！")
            c = int(input("请输入猜测值："))
        else:
            if c < a:
                print(no + "太小了！")
                c = int(input("请输入猜测值："))
    print(yes)
