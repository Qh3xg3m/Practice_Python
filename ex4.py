#!/usr/bin/env python3
# -*- coding: utf-8 -*-

numbers = [1,-5,2,3,-2,4]
if len(numbers) == 0:
	print(1)
	exit()

numbers.sort()
count = 0
for i in numbers:
	if i < 0:
		count = count + 1
numbers =  numbers[count:]

if len(numbers) == 0:
	print(1)
	exit()

for i in range(len(numbers)-1):
	if numbers[i]>=0 and numbers[i+1]-numbers[i]>1:
		print(numbers[i]+1)
		exit()
print(numbers[len(numbers)-1]+1)


"""This problem was asked by Stripe.

Given an array of integers, find the first missing positive integer in linear time 
and constant space. In other words, find the lowest positive integer that does not exist 
in the array. The array can contain duplicates and negative numbers as well.

For example, the input [3, 4, -1, 1] should give 2. The input [1, 2, 0] should give 3.

You can modify the input array in-place."""


