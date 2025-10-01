# ====================================================== #
# Queue is a Linear Data-Structure .
# Queue perform operation in FIFO manner.
# LIFO -> First In First Out
# ====================================================== #
# Queue Operation
# ====================================================== #
# 1. Enqueue -> Add element to the queue
# 2. Dequeue -> Remove element from the queue
# 3. Front -> Get the front element of the queue
# 4. Rear -> Get the rear element of the queue
# ====================================================== #
# Queue Implementation
# ====================================================== #

class Queue :
    def __init__(self) :
        self.queue = []
        self.front = -1
        self.rear = -1
        
    def enqueue(self, data) :
        self.queue.append(data)
        self.rear += 1
        if self.front == -1 :
            self.front = 0
            print("Enqueue Success")
        else :
            print("Enqueue Success")

    def dequeue(self) :
        if self.front == -1 :
            print("Queue is Empty")
        else :
            self.queue.pop(0)
            print("Dequeue Success")

    def front(self) :
        if self.front == -1 :
            print("Queue is Empty")
        else :
            print("Front Element is : ", self.queue[0])

    def rear(self) :
        if self.front == -1 :
            print("Queue is Empty")
        else :
            print("Rear Element is : ", self.queue[self.rear])
            print("Rear Element is : ", self.queue[-1])

    def display(self) :
        if self.front == -1 :
            print("Queue is Empty")
        else :
            print("Queue is ", self.queue)



Obj = Queue()
Obj.enqueue(1)
Obj.enqueue(2)
Obj.enqueue(3)
Obj.enqueue(4)
Obj.enqueue(5)
Obj.display()
Obj.dequeue()
Obj.dequeue()
Obj.display()
# Obj.front()
# Obj.rear()

from collections import deque

d = deque()
d.append(10)
d.append(20)
d.append(30)

print("Queue :- " , d)

dq = d.popleft()

if d :
  front = d[0]
  print("front element [peek] :- " , front)
  
isempty = len(d)==0
print("length of Queue :- " , len(d))

for i in d :
  print(i , end=" ")