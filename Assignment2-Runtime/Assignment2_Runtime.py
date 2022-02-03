## Assignment 2 ##

import time
import random

## General Functions ##

def generateDictionary(list):
    strList = [str(int) for int in list]
    
    dict = {}

    for i in range(len(list)):
        dict[strList[i]] = list[i]

## Testing functions ## 

def testList_Append(testList):
    list = testList.copy()

    t0 = time.time()
    ## 
    list.append(1)
    ##
    t1 = time.time()

    return t1-t0

def testList_insertFront(testList):
    list = testList.copy()

    t0 = time.time()
    ##
    list.insert(0,1)
    ##
    t1 = time.time()

    return t1-t0



'''
Might want to edit testList_insertMiddle to make it more 
efficient, the way I inserted in the middle of the
list may be kind of dumb lol 
'''

def testList_insertMiddle(testList):
    list = testList.copy()

    t0 = time.time()
    ##
    middle = int(len(list)/2)
    list.insert(middle, 1)
    ##
    t1 = time.time()

    return t1-t0

def testList_insertRandom(testList):
    list = testList.copy()

    t0 = time.time()
    ##
    list.insert(random.randint(0,len(list)-1),1)
    ##
    t1 = time.time()

    return t1-t0

def testList_deleteEnd(testList):
    list = testList.copy()

    t0 = time.time()
    ##
    ''' 
    Apparently this was the most efficient way to delete
    a list item directly 

    ''' 
    del list[-1]

    ##
    t1 = time.time()

    return t1-t0

def testList_deleteFront(testList):
    list = testList.copy()

    t0 = time.time()

    ##
    del list[0]
    ##

    t1 = time.time()

    return t1-t0

def testList_deleteMiddle(testList):
    list = testList.copy()

    t0 = time.time()

    ##
    del list[int(len(list)/2)]
    ##

    t1 = time.time()

    return t1-t0

def testList_deleteRandom(testList):
    list = testList.copy()

    t0 = time.time()

    ##
    del list[random.randint(0,len(testList)-1)]
    ##

    t1 = time.time()

    return t1-t0


def testList_inList(testList):
    t0 = time.time()

    ##
    check = random.randint(0,len(testList)-1)

    if check in testList:
        print("Element found")
    ##

    t1 = time.time()

    return t1-t0



## Generate lists ##

ten = list(range(1,11))
hund = list(range(1,101))
thou = list(range(1,1001))
tenthou = list(range(1,10001))
hundthou = list(range(1,100001))
mill = list(range(1,1000001))

## Generate dictionaries ##

dictTen = generateDictionary(ten)
dictHund = generateDictionary(hund)
dictThou = generateDictionary(thou)
dictTenThou = generateDictionary(tenthou)
dictHundThou = generateDictionary(hundthou)
dictMill = generateDictionary(mill)

## Run tests ## 

## List Append Tests ##


