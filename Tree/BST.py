# ============================================================== #
# BST is a type of Tree.
# BST is a binary tree where each node has at most 2 children, which are referred to
# as the left child and the right child.
# A node with no children is referred to as a leaf node.
# A node with two children is referred to as an internal node.
# A binary search tree (BST) is a binary tree where each node has a comparable value,
# such that nodes to the left have values less than or equal to it, and nodes to the
# right have values greater than or equal to it.
# ============================================================== #
# BST Implemention :- 
# 1. Insertion
# 2. Deletion
# 3. Searching
# ============================================================== #
# Insertion :-
# 1. If the tree is empty, the new node is added as the root.
# 2. If the new value is less than the root, the node is added to the left subtree.
# 3. If the new value is greater than the root, the node is added to the right subtree.
# ============================================================== #
# Deletion :-
# 1. If the node to be deleted has no children, it is simply removed.
# 2. If the node to be deleted has one child, the child is attached to the parent of the node to be deleted.
# 3. If the node to be deleted has two children, the inorder successor of the node to be deleted is found. The inorder successor of a node is the next node in the inorder traversal of the tree. The inorder successor of a node with two children is the node with the smallest value in the right subtree of the node.
# ============================================================== #
# Searching :-
# 1. If the tree is empty, the value is not found.
# 2. If the value of the node is equal to the value to be searched, the node is found.
# 3. If the value of the node is less than the value to be searched, the search is continued in the right subtree.
# 4. If the value of the node is greater than the value to be searched, the search is continued in the left subtree.
# ============================================================== #
# Time Complexity :-
# 1. Insertion :- O(h) where h is the height of the tree.
# 2. Deletion :- O(h) where h is the height of the tree.
# 3. Searching :- O(h) where h is the height of the tree.
# ============================================================== #
# Space Complexity :-
# 1. Insertion :- O(1)
# 2. Deletion :- O(1)
# 3. Searching :- O(1)
# ============================================================== #
# BST Implemention using code :- 
class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

class BST :
    def __init__(self):
        self.root = None

    def insert(self,data) :
        if self.root == None:
            self.root = Node(data)
        else:
            self._insert(data, self.root)

    def _insert(self, data, node):
        if data < node.data:
            if node.left == None:
                node.left = Node(data)
            else:
                self._insert(data, node.left)
        else:
            if node.right == None:
                node.right = Node(data)
            else:
                self._insert(data, node.right)

    def delete(self, data) :
        if self.root == None:
            print("Tree is empty")
        else:
            self.root = self._delete(data, self.root)

    def _delete(self, data, node):
        if node == None:
            return node
        if data < node.data:
            node.left = self._delete(data, node.left)
        elif data > node.data:
            node.right = self._delete(data, node.right)
        else:
            if node.left == None:
                return node.right
            elif node.right == None:
                return node.left
            node.data = self._find_min(node.right).data
            node.right = self._delete(node.data, node.right)
        return node

    def _find_min(self, node):
        if node.left == None:
            return node
        return self._find_min(node.left)

    def display(self) :
        if self.root == None:
            print("Tree is empty")
        else:
            self._display(self.root)

    def _display(self, node):
        if node.left:
            self._display(node.left)
        print(node.data , " -> ")
        if node.right:
            self._display(node.right)

A = BST()
A.insert(10)
A.insert(5)
A.insert(15)
A.insert(3)
A.insert(7)
A.insert(12)
A.insert(18)
A.display()
print(dir(A.display()))