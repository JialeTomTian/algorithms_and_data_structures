import copy

class LinkedList:
    def __init__(self):
        self.head = None
    # end of init
    def printList(self):
        currentNode = self.head
        while currentNode != None:
            print(currentNode.value)
            currentNode = currentNode.next
    #end of printList
# end of LinkedList


class Node:
    def __init__(self, value):
        self.value = value
        self.next = None
    # end of init
# end of node


NodeOne = Node(5)
NodeTwo = Node(6)
NodeThree = Node(7)
NodeFour = Node(8)
NodeFive = Node(5)
NodeSix = Node(7)

llOne = LinkedList()
llOne.head = NodeOne
NodeOne.next = NodeTwo
NodeTwo.next = NodeThree
NodeThree.next = NodeFour
NodeFour.next = NodeFive
NodeFive.next = NodeSix

NodeSeven = Node(7)
NodeEight = Node(7)
NodeNine = Node(8)
NodeTen = Node(8)
NodeEleven = Node(6)
NodeTwelve = Node(7)

llTwo = LinkedList()
llTwo.head = NodeSeven
NodeSeven.next = NodeEight
NodeEight.next = NodeNine
NodeNine.next = NodeTen
NodeTen.next = NodeEleven
NodeEleven.next = NodeTwelve

llOne.printList()

#Remove Duplicates From a Linked List
def removeDuplicates(linkedList):    
    repeatSet = set()
    removeNodes(linkedList.head, repeatSet, None)
#end of removeDuplicates

def removeNodes(node, repeatSet, prev):
    if node==None:
        return None
    elif not(node.value in repeatSet):
        repeatSet.add(node.value)
        removeNodes(node.next, repeatSet, node)
    else:
        prev.next = node.next
        removeNodes(node.next, repeatSet, prev)
    #end of if
#end of removeNodes

testOne = copy.deepcopy(llOne)
print("")
removeDuplicates(testOne)
testOne.printList()

testTwo = copy.deepcopy(llTwo)
print("")
removeDuplicates(testTwo)
testTwo.printList()
