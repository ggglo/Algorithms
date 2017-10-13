# -*- coding: utf-8 -*-
"""
Created on Fri Oct 13 10:52:45 2017

@author: win_young
"""

def BinarySearch(alist, item):
	lo, hi = 0, len(alist) - 1

	while lo <= hi:
		mid = int((hi + lo) / 2)
		print(mid)
		if alist[mid] > item:
			hi = mid - 1
		elif alist[mid] < item:
			lo = mid + 1
		else:
			return mid
	return -1

myList = [0, 1, 2, 8, 13, 17, 19, 32, 42, 56]
print(BinarySearch(myList, 8))