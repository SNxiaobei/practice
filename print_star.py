#! /usr/bin/env python3
# -*- coding: utf-8 -*-
row = int(input("请输入要打印的行数："))
while row > 0:
    x = "*" * row
    row -= 1
    print(x)


