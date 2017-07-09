#!/usr/bin/env python
# -*- coding: utf-8 -*-


class Deque:
    def __init__(self, size = 99999):
        self.items = []
        self.maxSize = size

    def isEmpty(self):
        return self.items == []

    def addFront(self, item):
        if self.size() == self.maxSize:
            print("Deque is full")
        else:
            self.items.append(item)

    def addRear(self, item):
        if self.size() == self.maxSize:
            print("Deque is full")
        else:
            self.items.insert(0, item)

    def removeFront(self):
        if self.isEmpty():
            print("Deque is empty")
        else:
            return self.items.pop()

    def removeRear(self):
        if self.isEmpty():
            print("Deque is empty")
        else:
            return self.items.pop(0)
    
    def full(self):
        return self.size() == self.maxSize
    
    def size(self):
        return len(self.items)

    def output(self):
        print (self.items)


if __name__ == "__main__":
    d = Deque()
    d.addFront("3")
    d.output()
    d.removeRear()
    d.output()
    d.removeRear()
    d.output()