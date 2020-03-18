#!/usr/bin/env python3
# -*- coding: utf-8 -*-

num = [1,2,3,4,5]
result = []
for i in num:
	s = 1
	index = num.index(i)
	temp = num[:index] + num[index+1:]
	for j in temp:
		s = s * j
	result.append(s)

print(result)


"""This problem was asked by Uber.

Given an array of integers, return a new array such that each element at index i of 
the new array is the product of all the numbers in the original array except the one at i.

For example, if our input was [1, 2, 3, 4, 5], the expected output would be 
[120, 60, 40, 30, 24]. If our input was [3, 2, 1], the expected output would be [2, 3, 6]."""