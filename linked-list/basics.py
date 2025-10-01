# ============================================================= #
# Linked-List is a data-structure .
# In that , we have total two parts :- Data and Address .
# Each and every node is connected to node by address .
# ============================================================== #
# Linked-List Implemention
# ============================================================= #

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

    def insert_at_beginning(self, data):
        new_node = Node(data)
        new_node.next = self.head
        self.head = new_node

    def insert_at_end(self, data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
        else:
            current_node = self.head
            while current_node.next is not None:
                current_node = current_node.next
            current_node.next = new_node

    def insert_after_node(self, data, prev_node):
        if prev_node is None:
            print("Previous node is not in the linked list")
            return
        new_node = Node(data)
        new_node.next = prev_node.next
        prev_node.next = new_node

    def delete_node(self, node):
        if node is None:
            print("Node is not in the linked list")
            return
        if node == self.head:
            self.head = node.next
        else:
            current_node = self.head
            while current_node.next is not node:
                current_node = current_node.next
            current_node.next = node.next

    def print_list(self):
        current_node = self.head
        while current_node is not None:
            print(current_node.data, end=" -> ")
            current_node = current_node.next

linked_list = LinkedList()
linked_list.insert_at_beginning(10)
linked_list.insert_at_beginning(20)
linked_list.insert_at_beginning(30)
linked_list.insert_at_end(40)
linked_list.insert_after_node(50, linked_list.head.next)
linked_list.insert_at_end(20)
linked_list.insert_after_node(30, linked_list.head)
linked_list.delete_node(linked_list.head)
linked_list.print_list()