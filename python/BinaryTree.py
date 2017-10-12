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
		node, parent = self.transverse(data)
		