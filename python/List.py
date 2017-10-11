# -*- coding: utf-8 -*-
"""
Created on Wed Sep 11 14:09:07 2017

@author: win_young
"""

class Node:
	def __init__(self, initdata):
		self.data = initdata
		self.next = None
	
	def getData(self):
		return self.data
	
	def getNext(self):
		return self.next
	
	def setData(self, newdata):
		self.data = newdata
		
	def setNext(self, nextNode):
		self.next = nextNode
		
temp = Node(93)
temp.setData(100)
print(temp.getData())

class UnorderedList:
	def __init__(self):
		self.head = None
		
	def isEmpty(self):
		return self.head == None
	
	def add(self, item):
	   temp = Node(item)
	   temp.setNext(self.head)
	   self.head = temp
		
	def size(self):
	   current = self.head
	   count = 0
	   while current != None:
		   count += 1
		   current = current.getNext()
	   return count
	
	def search(self, item):
	   current = self.head
	   found = False
	   while current != None and not found:
		   if current.getData() == item:
			   found = True
		   else:
			   current = current.getNext()
	   return found
	
	def remove(self, item):
	   current = self.head
	   previous = None
	   found = False
	   while not found:
		   if current.getData() == item:
			   found = True
		   else:
			   previous = current
			   current = current.getNext()
		   
	   if previous == None:
		   self.head = current.getNext()
	   else:
		   previous.setNext(current.getNext())
		   
myList = UnorderedList()
myList.add(31)
myList.add(77)
myList.add(17)
print(myList.search(17))
myList.remove(77)
print(myList.search(77))	   