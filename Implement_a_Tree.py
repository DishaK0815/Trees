class TreeNode:
    # create a tree with given nodes
    def __init__(self, data):  #structure of Tree 
        self.data = data
        self.left = None
        self.right = None

# nodes of trees
Root = TreeNode('R')
NodeA = TreeNode('A')
NodeB = TreeNode('B')
NodeC = TreeNode('C')
NodeD = TreeNode('D')
NodeE = TreeNode('E')
NodeF = TreeNode('F')
NodeG = TreeNode('G')


# routes for Accessing nodes
Root.left = NodeA
Root.right = NodeB

NodeA.left = NodeC
NodeA.right = NodeD

NodeB.left = NodeE
NodeB.right = NodeF 

NodeF.left = NodeG

print("Root Node:", Root.data)
print("Left Child of Root:", Root.left.data)
print("Right Child of Root:", Root.right.data)

