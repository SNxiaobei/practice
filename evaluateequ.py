#!/usr/bin/env python3
# -*- coding: utf-8 -*-
sum = 0
i = 0
while i < 10:
    sum += 1 / (1 + i)
    i += 1
    print("%d %.4f" % (i, sum))
