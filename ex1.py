#!/usr/bin/env python3
# -*- coding: utf-8 -*-

k = int(input(" k = "))
num = input(" numbers = ")
num = num.split(" ")
listNum = []
for i in num:
	listNum.append(int(i))
print(num)
for i in listNum:
	index = listNum.index(i)
	for j in listNum[index+1:]:
		if i + j == k:
			print(" {0} = {1} + {2}".format(k,i,j))

"""
This problem was recently asked by Google.

Given a list of numbers and a number k, return whether any two numbers from the list add up to k.

For example, given [10, 15, 3, 7] and k of 17, return true since 10 + 7 is 17.

Bonus: Can you do this in one pass?"""



