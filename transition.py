#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# 使用公式 C = (F - 32) / 1.8 将华氏温度转为摄氏温度。
fahrenheit = 0
print("Fahrenheit Celsius")
while fahrenheit <= 250:
    celsius = (fahrenheit -32) / 1.8  # 转换为摄氏度
    print("%5d %7.2f"% (fahrenheit, celsius))
    fahrenheit += 25

