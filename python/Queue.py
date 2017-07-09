#!/usr/bin/env python
# -*- coding: utf-8 -*-

class Queue:
    def __init__(self, size = 99999):
        self.queue = []
        self.maxSize = size

    def isEmpty(self):
        return self.queue == []

    def enqueue(self, item):
        if self.maxSize == self.size():
            print("Queue is full")
        else:
            return self.queue.insert(0, item)

    def dequeue(self):
        if self.isEmpty():
            print("Queue is empty")
        else:
            return self.queue.pop()
    
    def full(self):
        return self.size() == self.maxSize
    
    def size(self):
        return len(self.queue)

    def output(self):
        print(self.queue)

if __name__ == "__main__":
    q = Queue(100)
    q.enqueue("233")
    q.output()
    q.dequeue()
    q.output()