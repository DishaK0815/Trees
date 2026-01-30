class TreeNode:
    # create a tree with given nodes
    def __init__(self, data):  #structure of Tree 
        self.data = data
        self.left = None
        self.right = None

def InOrderTraversal(node):
    if node is None:
        return
    InOrderTraversal(node.left)
    print(node.data, end=",")
    InOrderTraversal(node.right)

# nodes of trees
Root = TreeNode(13)
node7 = TreeNode(7)
node15 = TreeNode(15)
node3 = TreeNode(3)
node8 = TreeNode(8)
node14 = TreeNode(14)
node19 = TreeNode(19)
node18 = TreeNode(18)

Root.left = node7
Root.right = node15

node7.left = node3
node7.right = node8

node15.left = node14
node15.right = node19

node19.left = node18

InOrderTraversal(Root) # Expected output: 3,7,8,13,14,15,18,19,


def SearchNode(node, target):
    if node is None:
        return False
    elif node.data == target:
        return True
    elif target < node.data:
        return SearchNode(node.left, target)
    else:
        return SearchNode(node.right, target)
    
# Searching for nodes
print("\nSearching for 8:", SearchNode(Root, 8))   # Expected output: True



def InsertNode_in_BST(node, value):
    if node is None:
        return TreeNode(value)
    if value < node.data:
        node.left = InsertNode_in_BST(node.left, value)
    else:
        node.right = InsertNode_in_BST(node.right, value)
    return node

# Inserting a new node
InsertNode_in_BST(Root, 10)
InOrderTraversal(Root) # Expected output: 3,7,8,10,13,14,15,18,19,

def DeleteNode_in_Bst(node, value):
    if node is None:
        return node
    if value < node.data:
        node.left = DeleteNode_in_Bst(node.left, value)
    elif value > node.data:
        node.right = DeleteNode_in_Bst(node.right, value)
    else:
        # Node with only one child or no child
        if node.left is None:
            return node.right
        elif node.right is None:
            return node.left
        # Node with two children: Get the inorder successor (smallest in the right subtree)
        temp = node.right
        while temp.left is not None:
            temp = temp.left
        node.data = temp.data
        node.right = DeleteNode_in_Bst(node.right, temp.data)
    return node

DeleteNode_in_Bst(Root, 15)
InOrderTraversal(Root) # Expected output: 3,7,8,10,13,14,18,19,