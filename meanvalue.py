#!/usr/bin/env python3
# -*- coding: utf-8 -*-
count = int(input("请输入你要输入的个数："))
i = 0
sum = 0  # 定义变量记录和
while i < count:
    num = float(input("请输入数字："))
    sum += num  # 每输入一个数字都进行一次加法
    i += 1
mean = sum / count
print("这%d个数的平均值为%0.2f" % (count, mean))

