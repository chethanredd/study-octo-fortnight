import time
class stack:
    def __init__(self):
        self.item = []
    def isempty(self):
        self.item == []
    def push(self,item):
        self.item.append(item)
    def pop(self):
        return self.item.pop()
    def size(self):
        return len(self.item)
    def display(self):
        return (self.item)

s=stack()
start=time.time()
print(s.isempty())
print("push operation")
s.push(90)
s.push(54)
s.push(32)
s.push(80)
print(s.display())
print("size", s.size())
print("pop operation")
print(s.pop())
print(s.pop())
print("stack=", s.display())
end=time.time()
print("Run time of this program is:", end-start)