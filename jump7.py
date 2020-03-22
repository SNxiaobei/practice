# -*- coding: utf-8 -*-
# 过七小游戏
for i in range(1, 101):
    if i % 7 != 0 and i %10 != 7 and i // 10 != 7:
        print(i)
