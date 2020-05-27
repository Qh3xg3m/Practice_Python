# #!/usr/bin/env python3
# # -*- coding: utf-8 -*-

# đề bài: https://imgur.com/a/xb8Z5VF

arr = [2, 4, 1, 9, 8] # 25
arr = [1,2,3] # 7
arr.sort()

Sum = 1
for i in arr:
	Sum = Sum + i
	
if arr[0] != 1:
	print(1)
else:
	minMoney = 0
	for i in range(len(arr)-1):
		minMoney = minMoney + arr[i]
		if arr[i+1] > minMoney+1:
			print(minMoney+1)
			exit()
		print(Sum)
		exit()
			


