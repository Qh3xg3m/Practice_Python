#!/usr/bin/env python3
# -*- coding: utf-8 -*-

def nto(x):
	if x < 2:
		lg = False
	else:
		lg = True
		for uoc in range(2,x):
			if x % uoc == 0:
				lg = False
	return(lg)

def main(x):
	lg = True
	if nto(x):
		i = x
		while x != 0:
			if nto(x)==False:
				lg=False
			x = x // 10
		if lg == True:
			print(i)
# print cac so sieu nguyen to tu 0 --> 10000
for x in range(10001):
	main(x)


