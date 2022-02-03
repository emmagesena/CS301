## Assignment 2 ##

import time
import random

## Benchmarking Function

def benchmark(f, data):
    # lengths is the inputted lists of list/dictionaries that will run as N elements
    # intvl = 10 will mean each length N will run in the given function 10 times
    intvl = 10
    
    f_out = open("runtimes_bench_output.csv", "w+")
    
    for n_elements in data:
        # --Write the number of elements N of a given list/dictionary--
        f_out.write(str(len(n_elements) + ',')
        
        # --Run function intvl times and take average--
        avg_runtime = 0
        for i in range(intvl):
            avg_runtime += f(n_elements)
        avg_runtime = avg_runtime / intvl
        
        # --Write average runtime given specific list length--
        f_out.write(str(avg_runtime) + "\n")
    
    # --Close out file when all data is written--
    f_out.close()

f_out = open("benchoutput.csv", "w+")

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
listLengths = [ten, hund, thou, tenthou, hundthou, mill] # <--- These will plug into bench func

## Generate dictionaries ##

dictTen = generateDictionary(ten)
dictHund = generateDictionary(hund)
dictThou = generateDictionary(thou)
dictTenThou = generateDictionary(tenthou)
dictHundThou = generateDictionary(hundthou)
dictMill = generateDictionary(mill)
dictLengths = [dictTen, dictHund, dictThou, dictTenThou, dictHundThou, dictMill] # <--- These will plug into bench func

## Run tests ## 

## List Append Tests ##


'''
Following code is just to check my test functions are
running correctly, we will want to 
use them in a more sophisticated way to collect data 
'''
#result = testList_Append(ten)
#print(result)

#result =  testList_Append(mill)
#print(result)

#result = testList_insertFront(ten)
#print(result)

#result = testList_insertFront(mill)
#print(result)

#result = testList_insertMiddle(ten)
#print(result)

#result = testList_insertMiddle(mill)
#print(result)

#result = testList_insertRandom(ten)
#print(result)

#result = testList_insertRandom(mill)
#print(result)
