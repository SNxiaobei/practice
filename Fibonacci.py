#! /usr/bin/env python3
# -*- coding: utf-8 -*-
# 打印1-100之间的斐波那契数列
a, b = 0, 1
while b < 100:
    print(b)
    a, b = b, b + a
