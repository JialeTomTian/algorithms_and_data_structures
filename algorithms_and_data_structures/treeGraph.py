def inOrder(node):
    if not(node == None):
        inOrder(node.left)
        print(node.value)
        inOrder(node.right)
    #end of if
#end of inOrder

def preOrder(node):
    if not(node == None):
        print(node.value)
        preOrder(node.left)
        preOrder(node.right)

def postOrder(node):
    if not(node == None):
        postOrder(node.left)
        postOrder(node.right)
        print(node.value)

class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

class Tree:
    def __init__(self, node):
        self.root = node
    #end of __init__
    def inOrderPrint(self):
        inOrder(self.root)
    #end of inOrderPrint

    def preOrderPrint(self):
        preOrder(self.root)
    #end of preOrderPrint

    def postOrderPrint(self):
        postOrder(self.root)
    #end of postOrderPritn


root = Node(8)
nodeOne = Node(4)
nodeTwo = Node(10)
nodeThree = Node(2)
nodeFour = Node(6)
nodeFive = Node(20)

root.left = nodeOne
root.right = nodeTwo
nodeOne.left = nodeThree
nodeOne.right = nodeFour
nodeTwo.right = nodeFive

treeOne = Tree(root)
treeOne.inOrderPrint()
print("")
treeOne.postOrderPrint()
print("")
treeOne.preOrderPrint()


