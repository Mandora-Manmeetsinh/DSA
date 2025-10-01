# ====================================================== #
# Stack is a Linear Data-Structure .
# Stack perform operation in LIFO manner.
# LIFO -> Last In First Out
# ====================================================== #
# Stack Operations
# ====================================================== #
# 1. Push : Add an element to the top of the stack.
# 2. Pop : Remove an element from the top of the stack.
# 3. Peek or Top : Get the top element of the stack.
# 4. IsEmpty : Check if the stack is empty.
# 5. IsFull : Check if the stack is full.
# ====================================================== #
# Stack Implementation using List

class Stack :
    def __init__(self,k) -> None:
        self.stack = []*k
        self.k=k

    def is_full(self) :
        if len(self.stack) == self.k :
            return "Stack is Full"
        
    def is_empty(self) :
        if len(self.stack) == 0 :
            return "Stack is Empty"
        
    def push(self) :
        if self.is_full() :
            return "Can not insert Element"
        else :
            self.stack.append(input("Enter the Element : "))

    def pop(self) :
        if self.is_empty() :
            return "Can not delete Element"
        else :
            return self.stack.pop()
        
    def top(self) :
        if self.is_empty() :
            return "Can not get the top Element"
        else :
            return self.stack[-1]
        
    def show(self) :
        if self.is_empty() :
            return "Can't append data"
        else :
            return self.stack

A = Stack(5)
print(A.is_empty())  
print(A.is_full())
A.push()
print(A.show())
A.push()
print(A.show())
A.push()
print(A.show())
# print(A.is_empty())  
# print(A.top())
# A.pop()
# print("After removing a element :- " , A.show())
# A.pop()
# print("After removing a element :- " , A.show())


print()
print(A.show())
print(A.show())