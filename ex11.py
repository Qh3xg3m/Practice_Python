#!/usr/bin/env python3
# -*- coding: utf-8 -*-

Str = input(" List String : ")
listStr = Str.split(" ")
prefix = input(" Prefix : ")

for i in listStr:
	try:
		if i.index(prefix) == 0:
			print(i)
	except:
		continue

"""
Good morning! Here's your coding interview problem for today.

This problem was asked by Twitter.

Implement an autocomplete system. That is, given a query string s and a set of all 
possible query strings, return all strings in the set that have s as a prefix.

For example, given the query string de and the set of strings [dog, deer, deal], return [deer, deal].

Hint: Try preprocessing the dictionary into a more efficient data structure to speed up queries.
"""