#Implementation of a Queue and Stack in Python

class Stack:
    def __init__(self):
        self.values = []
    #end of init

    def push(self, value):
        self.values.append(value)
    #end of push

    def pop(self):
        if(self.values == []):
            return None
        return self.values.pop()
    #end of pop

    def peak(self):
        if(self.values == []):
            return None
        return self.values[-1]
    #end of peak

    def isEmpty(self):
        return self.values == []
    #end of isEmpty

    def print(self):
        for counter in range(1, len(self.values)+1):
            print(self.values[counter*-1])
        #end of for
    #end of print
#end of stack

class Queue:
    def __init__(self):
        self.values = []
    #end of init

    def add(self, item):
        self.values.insert(0, item)
    #end of add

    def remove(self):
        if(self.values == []):
            return None
        return self.values.pop()
    #end of remove

    def peak(self):
        if(self.values == []):
            return None
        return self.values[-1]
    #end of peak

    def isEmpty(self):
        return self.values == []
    #end of isEmpty

    def print(self):
        for counter in range(0, len(self.values)):
            print(self.values[counter])
#end of queue

stackOne = Stack()
stackOne.push(2)
stackOne.push(10)
stackOne.push(3)
stackOne.push(7)
stackOne.push(1)
stackOne.push(4)

stackOne.print()
print("")
queueOne = Queue()
queueOne.add(2)
queueOne.add(10)
queueOne.add(3)
queueOne.add(7)
queueOne.add(1)
queueOne.add(4)
queueOne.print()

def sortStack(inputStack):
    outputStack = Stack()
    tempVal = -1
    while(not inputStack.isEmpty()):
        tempVal = inputStack.pop()
        while(True):
            if(outputStack.isEmpty()):
                break
            elif (outputStack.peak() <= tempVal):
                break
            else:
                inputStack.push(outputStack.pop())
            #end of if
        outputStack.push(tempVal)
    return outputStack
#end of sortStack    
print("")
result = sortStack(stackOne)
result.print()