#1

'''
class Stack:
    def __init__(self):
        self.items = []
    def isEmpty(self):
        return self.items == []
    def push(self, item):
        self.items.append(item)
    def pop(self):
        return self.items.pop()
    def peak(self):
        return self.items[len(self.items) - 1]
    def size(self):
        return len(self.items)
s = Stack()
s.push(1)
s.push(3)
s.push(6)
print(s.isEmpty())
print(s.size())
print(s.items)
'''

#2

'''
from pythonds.basic.stack import Stack
s = Stack()
print(s.isEmpty())
s.push(3)
s.push(6)
print(s.items)
s.push('dog')
print(s.items)
s.push(True)
print(s.size())
print(s.items)
s.pop()
print(s.items)
s.peek()
print(s.items)
'''
#3

from pythonds.basic.stack import Stack

def revstring(mystr):
    myStack = Stack()
    for ch in mystr:
        myStack.push(ch)
    revstr = ''
    while not myStack.isEmpty():
        revstr = revstr + myStack.pop()
    return revstr

print(revstring('apple'))