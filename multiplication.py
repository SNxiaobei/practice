#! /usr/bin/env python3
# -*- coding: utf-8 -*-
row = 1
while row <= 9:
    line = 1
    while line <= row:
        print("%d * %d = %d" % (line, row, line * row), end="\t")
        line += 1
    print()
    row += 1


