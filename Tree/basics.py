# ============================================================== #
# Tree is  a non-linear data-structure . 
# Tree components :- 
# 1. Root node :- The First Node of the Tree . 
# 2. Child :- The node which is directly connected to the parent node.
# 3. Parent :- The node which is directly connected to the child node.
# 4. Leaf node :- The node which does not have any child node.
# 5. Sibling :- The nodes which have the same parent node.
# 6. Degree :- The number of children of a node.
# 7. Height :- The number of edges from the root node to the leaf node.
# 8. Depth :- The number of edges from the root node to the node.
# 9. Subtree :- The set of nodes which are connected to the node.
# 10. Level :- The number of edges from the root node to the node.
# ============================================================== #
# Tree Traversal :-
# 1. Preorder :- Root -> Left -> Right
# 2. Inorder :- Left -> Root -> Right
# 3. Postorder :- Left -> Right -> Root
# ============================================================== #
# Tree Types :- 
# 1. Binary Tree :- A tree in which each node has at most two children.
# 2. Binary Search Tree :- A binary tree in which each node has a value greater than
# all values in its left subtree and less than all values in its right subtree.
# 3. AVL Tree :- A self-balancing binary search tree.
# 4. B Tree :- A tree in which each node has at most m children.
# 5. B+ Tree :- A B-tree variant that allows faster block processing for disk operations
# 6. Red-Black Tree :- A self-balancing binary search tree in which each node
# has an extra bit, and in each node, all leaves are at the same depth.
# 7. Splay Tree :- A self-balancing binary search tree in which recently accessed nodes
# are promoted to the top of the tree.
# ============================================================== #
# Tree Implementation :-
# 1. Array :- The array is used to store the tree elements.
# 2. Linked List :- The linked list is used to store the tree elements.
# 3. Pointer :- The pointer is used to store the tree elements.
# ============================================================== #
# Tree Operations :-
# 1. Insertion :- Inserting a node in the tree.
# 2. Deletion :- Deleting a node in the tree.
# 3. Searching :- Searching a node in the tree.
# 4. Traversal :- Traversing the tree.
# ============================================================== #
# Tree Applications :-
# 1. Compiler :- The compiler uses the tree to represent the syntax of the program.
# 2. Operating System :- The operating system uses the tree to represent the file system.
# 3. Database :- The database uses the tree to represent the data.
# ============================================================== #
# Tree Advantages :-
# 1. Fast :- The tree is fast in searching, insertion, and deletion.
# 2. Efficient :- The tree is efficient in storing and retrieving data.
# 3. Flexible :- The tree is flexible in representing data in different ways.
# ============================================================== #
# Tree Disadvantages :-
# 1. Complex :- The tree is complex in understanding and implementing.
# 2. Limited :- The tree is limited in the number of nodes it can store.
# ============================================================== #
# Tree Implementation with code using Linked-List :-
# 1. Node :- The node is the basic unit of the tree.
# 2. Tree :- The tree is the data structure that stores the nodes.
# 3. Insertion :- The insertion is the process of adding a node to the tree.
# 4. Deletion :- The deletion is the process of removing a node from the tree.
# 5. Searching :- The searching is the process of finding a node in the tree.
# 6. Traversal :- The traversal is the process of visiting all the nodes in the tree
# ============================================================== #

class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

def create_tree():
    root = Node(1)
    root.left = Node(2)
    root.right = Node(3)
    return root

def insert(node, data):
    if node is None:
        return Node(data)
    if data < node.data:
        node.left = insert(node.left, data)
    else:
        node.right = insert(node.right, data)
    return node

def delete(node, data):
    if not node:
        return None
    if data < node.data:
        node.left = delete(node.left, data)
    elif data > node.data:
        node.right = delete(node.right, data)
    else:
        if not node.left:
            return node.right
        if not node.right:
            return node.left
        temp = node.right
        while temp.left:
            temp = temp.left
        node.data = temp.data
        node.right = delete(node.right, temp.data)
    return node

def print_tree(node, level=0, is_last=True, prefix=''):
    if node is not None:
        print(prefix + ('└── ' if is_last else '├── ') + str(node.data))
        prefix += '    ' if is_last else '│   '
        children = [child for child in [node.left, node.right] if child]
        for i, child in enumerate(children):
            is_last_child = i == len(children) - 1
            print_tree(child, level + 1, is_last_child, prefix)

root = create_tree()
insert(root, 4)
insert(root, 2)
insert(root, 1)
print_tree(root)