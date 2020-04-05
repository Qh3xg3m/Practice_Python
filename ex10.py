#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import time
def f():
	return("OK!")

n = int(input(" Time: ")) * 0.001
time.sleep(n)
print(f())


"""
Good morning! Here's your coding interview problem for today.

This problem was asked by Apple.

Implement a job scheduler which takes in a function f and an integer n, 
and calls f after n milliseconds.
"""