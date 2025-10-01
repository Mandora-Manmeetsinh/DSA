class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedListCircular:
    def __init__(self, capacity):
        self.head = None
        self.capacity = capacity
        self.size = 0

    def is_empty(self):
        return self.head is None

    def is_full(self):
        return self.size == self.capacity

    def insert_node(self, data):
        if self.is_full():
            return "Can not insert node"
        else:
            new_node = Node(data)
            if self.head is None:
                self.head = new_node
                new_node.next = self.head
            else:
                temp = self.head
                while temp.next!= self.head:
                    temp = temp.next
                temp.next = new_node
                new_node.next = self.head
            self.size += 1

    def remove_node(self):
        if self.is_empty():
            return "Can not remove node"
        else:
            temp = self.head
            while temp.next!= self.head:
                prev = temp
                temp = temp.next
            prev.next = temp.next
            self.head = temp.next
            self.size -= 1

    def display(self):
        if self.is_empty():
            print("Linked list is empty")
        else:
            temp = self.head
            while True:
                if temp.next!= self.head:
                    print(temp.data, end=" -> ")
                else:
                    print(temp.data, end=" -> ")
                temp = temp.next
                if temp == self.head:
                    break
            print(self.head.data)

A = LinkedListCircular(5)
A.insert_node(1)
A.insert_node(2)
A.insert_node(3)
A.insert_node(4)
A.remove_node()
# A.remove_node()
A.display()