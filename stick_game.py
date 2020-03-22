#! /usr/bin/env python3
# -*- coding: utf-8 -*-
sticks = 22


def stick(sticks, name):
    if sticks == 1:
        print("%s输了" % name)
        return
    elif sticks < 1:
        print("%s输了" % name)
        return


while True:
    stick(sticks, "玩家")
    if sticks == 1:
        break
    elif sticks < 1:
        break
    player_stick = int(input("请输入你本局要选择的棍子数:"))
    if player_stick > 5 or player_stick < 0:
        print("你的选择不应大于5或小于1")
        continue
    num = sticks - player_stick
    stick(num, "电脑")
    if num == 1:
        break
    elif num < 1:
        break
    print("电脑选择%d根"% (5 - player_stick))

    sticks -= 5
    print("剩余棍子数：%s"% sticks)

