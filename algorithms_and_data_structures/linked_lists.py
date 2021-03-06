import copy
from collections import deque

class LinkedList:
    def __init__(self):
        self.head = None
    # end of init

    def printList(self):
        currentNode = self.head
        while currentNode != None:
            print(currentNode.value)
            currentNode = currentNode.next
    # end of printList
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
NodeEight = Node(6)
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

# llOne.printList()

# Remove Duplicates From a Linked List


def removeDuplicates(linkedList):
    repeatSet = set()
    removeNodes(linkedList.head, repeatSet, None)
# end of removeDuplicates


def removeNodes(node, repeatSet, prev):
    if node == None:
        return None
    elif not(node.value in repeatSet):
        repeatSet.add(node.value)
        removeNodes(node.next, repeatSet, node)
    else:
        prev.next = node.next
        removeNodes(node.next, repeatSet, prev)
    # end of if
# end of removeNodess

# testOne = copy.deepcopy(llOne)
# print("")
# removeDuplicates(testOne)
# testOne.printList()

# testTwo = copy.deepcopy(llTwo)
# print("")
# removeDuplicates(testTwo)
# testTwo.printList()

# uses runner technique to solve without a buffer


def removeDuplicatesBuffer(linkedList):
    head = linkedList.head
    while(head):
        prev = head
        nextHead = head.next
        while(nextHead != None):
            if(nextHead.value == head.value):
                prev.next = nextHead.next
                nextHead = nextHead.next
            else:
                prev = nextHead
                nextHead = nextHead.next
            # end of if
        # end of while
        head = head.next
    # end of while
# end of removeNodesBuffer

# testOne = copy.deepcopy(llOne)
# print("")
# removeDuplicatesBuffer(testOne)
# testOne.printList()

testTwo = copy.deepcopy(llTwo)
# print("")
# removeDuplicatesBuffer(testTwo)
# testTwo.printList()

# Takes O(n) time and O(n) space due to recursive calls

def nthNodeRecurseWrapper(index, linkedList):
    return nthNodeRecurse(index, linkedList.head, 0)
#end of nthNodeRecurse

def nthNodeRecurse(index, node, current):
    if((node.next == None or node == None) and current < index-1):
        return "out of bounds"
    elif (current == index):
        return node.value
    else:
        return nthNodeRecurse(index, node.next, current+1)
    #end of if
#end of nthNodeRecurse

def nthNode(index, linkedList):
    currentIndex = 0
    head = linkedList.head
    while(head != None):
        if currentIndex == index:
            return head.value
        else:
            head = head.next
            currentIndex += 1
        # end of if
    # end of while
    return "out of bounds"
# end of nthNode

# print("")
# print(nthNode(1, testTwo))
# print(nthNodeRecurseWrapper(1, testTwo))
# print(nthNode(3, testTwo))
# print(nthNodeRecurseWrapper(3, testTwo))

# given two linked lists get the sum
# bonus (from leetcode medium): return result as a linkedList
# time complexity: O(n) space complexity: O(n)
def twoSum(llOne, llTwo):
    sumOne = 0
    powerOne = 0
    sumTwo = 0
    powerTwo = 0
    headOne = llOne.head
    headTwo = llTwo.head
    while(headOne != None):
        sumOne += headOne.value * (10 ** powerOne)
        headOne = headOne.next
        powerOne += 1
    # end of while
    while(headTwo != None):
        sumTwo += headTwo.value * (10 ** powerTwo)
        headTwo = headTwo.next
        powerTwo += 1
    # end of while
    answer = sumOne + sumTwo
    
    answerNode = Node(answer % 10)
    answerPower = 1
    prevNode = answerNode
    print(answer)
    while(answer > 10 ** answerPower):
        currentNode = Node(answer // (10**answerPower) % 10)
        prevNode.next = currentNode
        prevNode = currentNode
        answerPower+=1
    #end of while
    prevNode.next = None
    outputList = LinkedList()
    outputList.head = answerNode
    return outputList
#end of twoSum

def twoSumRecurse(llOne, llTwo):
    valOne = twoSumHelp(llOne.head)
    valTwo = twoSumHelp(llTwo.head)
    print(valOne+valTwo)
#end of twoSumRecurse

def twoSumHelp(node, currentSum=0, currentIndex=0):
    if(node == None):
        return currentSum
    else:
        tempVal = node.value*(10**currentIndex)
        return twoSumHelp(node.next, currentSum+tempVal, currentIndex+1)
#end of twoSumHelp

# Determine if a linkedlist's items are a palindrome
# Iterative Approach with a Stack and the runner technique 
def palindrome(llist):
    odd = False
    slow = llist.head
    fast = llist.head
    tempStack = deque() #append() and pop() makes it like a stack if you use one of appendleft() with pop it is a queue
    while(fast != None and fast.next != None):
        tempStack.append(slow.value)
        slow = slow.next
        fast = fast.next.next #if you hit None, it will be detected by the while loop
    #end of while
    #We can use whether fast is None or nut to determine whether the linkedList is even or odd
    if(fast != None):
        odd=True
    #end of if
    if(odd):
        slow=slow.next
    while(slow != None):
        if(slow.value != tempStack.pop()):
            return False
        slow=slow.next
    #end of while
    return True
#end of palindrome



# print("")
# llOne.printList()
# print("")
# llTwo.printList()
# print("")
# print(palindrome(llTwo))

# Determining the intersection of two linkedLists
# Strategy 
def determiningIntersection(llOne, llTwo):
    finishOne = llOne.head
    finishTwo = llTwo.head
    lengthOne = 0 #find the length of the lists
    lengthtWO = 0

    while(nodeOne != None):
        lengthOne += 1
        finishOne = finishOne.next
    #end of while

    while(nodeTwo != None):
        lengthTwo += 1
        finishTwo = finishTwo.next
    #end of while

    if(finishOne != finishTwo):
        return False
    #end of if

    startOne = llOne.head
    startTwo = llTwo.head

    if lengthOne > lengthTwo:
        difference = lengthOne-lengthTwo
        for counter in range(difference):
            startOne = startOne.next
        #end of if
    else: 
        difference = lengthTwo-lengthOne
        for counter in range(difference):
            startTwo = startTwo.next
        #end of if

    while(startTwo != None):
        if(startTwo == startOne):
            return startTwo
        else:
            startOne = startOne.next
            startTwo = startTwo.next
        #end of if
    #end of while
    return False

# Determine if a linked list has a loop
# Efficiency O(n) time complexity, also since only two pointers are used, the space complexity is only O(1)
def loopDetection(llist):
    slowPointer = currentNode.head
    fastPointer = currentNode.head
    while(fastPointer != None and fastPointer.next != None):
        fastPointer = fastPointer.next.next
        slowPointer = slowPointer.next
        if(fastPointer == slowPointer):
            return True
        #end of if
    #end of while
    return False
#end of loopDetection

# Find head of loop
# Time complexity: O(n)
def loopHead(llist):
    slowPointer = currentNode.head
    fastPointer = currentNode.head
    while(fastPointer != None and fastPointer.next != None):
        fastPointer = fastPointer.next.next
        slowPointer = slowPointer.next
        if(fastPointer == slowPointer):
            break
        #end of if
    #end of while
    if(fastPointer == None or fastPointer.next == None):
        return None
    #end of if
    slowPointer = currentNode.head
    while(fastPointer != slowPointer):
        slowPointer = slowPointer.next
        fastPointer = fastPointer.next
    #end of while
    return fastPointer
#end of loopHead

def reverseList(llist):
    currentNode = llist.head
    nextNode = None
    prevNode = None
    while(currentNode != None):
        nextNode = currentNode.next
        currentNode.next = prevNode
        prevNode = currentNode
        currentNode = nextNode
    #end of while
    llist.head = prevNode
#end of reverseList

# testTwo = copy.deepcopy(llTwo)
# testTwo.printList()
# print("")
# reverseList(testTwo)
# testTwo.printList()