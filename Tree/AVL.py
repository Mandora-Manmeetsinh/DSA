# ============================================================== #
# AVL Tree is  a non-linear data-structure .
# AVL Tree is a self-balancing Binary Search Tree (BST) where the difference between heights of
# left and right subtrees cannot be more than one for all nodes.
# AVL Tree is a height-balanced binary search tree in which the heights of the two child subt
# rees of any node differ by at most one. If at any time during the insertion or
# deletion process, the tree becomes unbalanced, the tree is automatically balanced by one
# or more tree rotations.
# AVL Tree is a self-balancing Binary Search Tree (BST) where the difference between heights of
# AVL Tree Rotation :-
# Left Rotation :- Rotate Tree's non-balanced node in left side .
# Right Rotation :- Rotate Tree's non-balanced node in right side .
# ============================================================== #
# AVL Tree Implemention with code :-

class Node :
    def __init__(self,data) -> None:
        self.data = data
        self.next = next

class AVL_Tree :
    def __init__(self) -> None:
        self.head=None
        self.tail=None
        self.next=next

    def insert_node(self) :
        data = int(input("Enter the data : "))
        if self.head is None :
            self.head = Node(data)
            self.tail = self.head
            return
        else :
            temp = self.head
            while temp.next is not None :
                temp = temp.next
                temp.next = Node(data)
                self.tail = temp.next
    
    def remove_node(self) :
        data = int(input("Enter the data : "))
        temp = self.head
        while temp.next is not None :
            if temp.data == data :
                temp.next = temp.next.next
                break
            temp = temp.next

    def display_Tree(self) :
        temp = self.head
        while temp is not None :
            print(temp.data,end=" ")
            temp = temp.next

A = AVL_Tree()
A.insert_node()
A.insert_node()
A.display_Tree()