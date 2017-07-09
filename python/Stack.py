#!/usr/bin/env python
# -*- coding: utf-8 -*-


class Stack:
    def __init__(self, size=99999):
        self.stack = []
        self.maxSize = size
        self.top = -1

    def isEmpty(self):
        return self.top == -1

    def push(self, item):
        if self.full():
            print ("Stack is full")
        else:
            self.stack.append(item)
            self.top += 1

    def pop(self):
        if self.isEmpty():
            print("Stack is empty")
        else:
            self.top -= 1
            return self.stack.pop()

    def full(self):
        return self.maxSize == self.top

    def size(self):
        return len(self.stack)

    def output(self):
        print (self.stack)

if __name__ == "__main__":
    s = Stack()
    s.push("231")
    s.output()