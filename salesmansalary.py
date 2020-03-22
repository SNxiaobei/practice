#!/usr/bin/env python3
# -*- coding: utf-8 -*-
camera_num = int(input("请输入相机数量："))
camera_price = int(input("请输入相机单价："))
salary_sum = camera_num * 200 + camera_num * (camera_price * 0.02) + 1500
print("小明本月卖出了%d台相机，工资：%d" % (camera_num, salary_sum))
