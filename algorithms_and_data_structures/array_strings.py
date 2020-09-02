#!user/bin/env/python3

# Determin if a string is unique
# Method 1: O(n^2) time complexity, O(1) space complexity
def isUnique(input):
    for letter in input:
        if(input.count(letter) > 1):
            return False
    return True
#end of isUnique

print(isUnique("something"))
print(isUnique("this is not unique"))

# Method 2: Using array of boolean, considering ASCII, O(n) time complexity
def isUniqueOptimized(input):
    tempList = list(map(lambda a: False, range(0, 128)))
    for letter in input:
        if (tempList[ord(letter)]):
            return False
        else:
            tempList[ord(letter)] = True
    return True

print(isUniqueOptimized("something"))
print(isUniqueOptimized("this is not unique"))

# check permutations, see if two strings are the same permutation 
# O(n) method, use isUniqueOptimized but now check with other string

# determine if a word is a permutation of a palindrome
# dictionary method: O(n)
def palindromePermutation(input):
    tempDict = list(map(lambda a: False, range(0, 128)))
    for letter in input:
        tempDict[ord(letter)] += 1
    #end of for 
    oddNum = 0
    for value in tempDict:
        if not(value % 2 == 0):
            oddNum += 1
        #end of if
        if oddNum > 1:
            return False
    #end of for
    return True
#end of palindromePermutation

print(palindromePermutation("tacocat"))
print(palindromePermutation("actotac"))
print(palindromePermutation("fdafdsf"))

               
#oneAway see if two words are one edit away, the three possible edits are
#remove a letter, replace a letter and add a letter
#Method one : time complexity O(n)
def oneAway(strOne, strTwo):
    indexOne = 0
    indexTwo = 0
    while(indexOne < len(strOne)):
        if strOne[indexOne] != strTwo[indexTwo]:
            indexOne+=1
            indexTwo+=1
            if indexOne + 1 == len(strOne):
                return True
            elif indexTwo + 1 == len(strTwo):
                return True
            elif strOne[indexOne+1:] == strTwo[indexTwo:]:
                return True
            elif strOne[indexOne:] == strTwo[indexTwo+1:]:
                return True
            elif strOne[indexOne:] == strTwo[indexTwo:]:
                return True
            else:
                return False
        indexOne+=1
        indexTwo+=1
    return True
#end of oneAway

print(oneAway("pale", "ale"))
print(oneAway("kale", "sale"))
print(oneAway("null", "kule"))






