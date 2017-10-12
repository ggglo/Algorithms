# -*- coding: utf-8 -*-
"""
Created on Thu Oct 12 09:44:54 2017

@author: win_young
"""

class BinaryTree:
	def __init__(self, data):
		self.left = None
		self.right = None
		self.data = data
		
	def insert(self, data):
		"""
		插入节点数据
		"""
		if data < self.data:
			if self.left is None:
				self.left = BinaryTree(data)
			else:
				self.left.insert(data)
		elif data > self.data:
			if self.right is None:
				self.right = BinaryTree(data)
			else:
				self.right.insert(data)
		
	def tranverse(self, data, parent = None):
		"""
      遍历二叉树
      """
		if data < self.data:
			if self.left is None:
				return None, None
			else:
				return self.left.tranverse(data, self)
		elif data > self.data:
			if self.right is None:
				return None, None
			else:
				return self.right.tranverse(data, self)
		else:
			return self, parent
		
	def delete(self, data):
		"""
		删除节点
		"""
		node, parent = self.tranverse(data)
		if node is not None:
			childCnt = node.childrenCount()
			if 0 == childCnt:
				#没有子节点直接删除
				if parent.left is node:
					parent.left = None
				else:
					parent.right = None
				del node
			elif 1 == childCnt:
				#
				if node.left is None:
					n = node.right
				else:
					n = node.left
				if parent.left is node:
					parent.left = n
				else:
					parent.right = n
					
				del node
			else:
				parent = node
				successor = node.right
				while successor.left:
					parent = successor
					successor = parent.left
				node.data = successor.data
				if parent.left is successor:
					parent.left = successor.right
				else:
					parent.right = successor.right
	
	def compare_trees(self, node):
		"""
		比较两颗树
		"""        
		if node is None:
			return False
		if self.data != node.data:
			return False
		res = True
		if self.left is None:
			if node.left:
				return False
		else:
			res = self.left.compare_trees(node.left)
		if res is False:
			return False
		if self.right is None:
			if node.right:
				return False
		else:
			res = self.right.compare_trees(node.right)
		return res
	
	def printTree(self):
		"""
		打印树
		"""
		if self.left:
			self.left.printTree()
		print(self.data)
		if self.right:
			self.right.printTree()
		
	def childrenCount(self):
		cnt = 0
		if self.left:
			cnt += 1
		if self.right:
			cnt += 1
		return cnt
	
	
bt = BinaryTree(30)
bt.insert(100)
bt.insert(200)
bt.insert(20)
bt.insert(60)
bt.insert(110)
bt.insert(90)
bt.printTree()
bt.delete(110)
bt.printTree()