## Assignment 2 ##
## by Hope Dannar, Emma Ogle, Logan Kulesus ##

import time
import random


# Benchmarking Function

def benchmark(f, data, name):
    # f is the inputted function that we will be benchmarking, the function
    #   returns the total time it took for the list/dict function to operate
    # data is the inputted lists of list/dictionaries that will run as N elements
    # name is a string input that will be the outputted name of the .csv file
    # intvl = 10 will mean each length N will run in the given function 10 times
    intvl = 100

    f_out = open(name + ".csv", "w+")

    for n_elements in data:
        # --Write the number of elements N of a given list/dictionary--
        f_out.write(str(len(n_elements)) + ',')

        # --Run function intvl times and take average--
        avg_runtime = 0
        for i in range(intvl):
            avg_runtime += f(n_elements)
        avg_runtime = avg_runtime / intvl

        # --Write average runtime given specific list length--
        f_out.write(str(avg_runtime) + "\n")

    # --Close out file when all data is written--
    f_out.close()


## General Functions ##


def generateDictionary(list):
    strList = [str(int) for int in list]

    dict = {}

    for i in range(len(list)):
        dict[strList[i]] = list[i]

    return dict

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
    list.insert(0, 1)
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
    middle = int(len(list)/2)

    t0 = time.time()
    ##

    list.insert(middle, 1)
    ##
    t1 = time.time()

    return t1-t0


def testList_insertRandom(testList):
    list = testList.copy()

    t0 = time.time()
    ##
    list.insert(random.randint(0, len(list)-1), 1)
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
    middle = int(len(list))

    t0 = time.time()

    ##
    del list[middle//2]
    ##

    t1 = time.time()

    return t1-t0


def testList_deleteRandom(testList):
    list = testList.copy()

    t0 = time.time()

    ##
    del list[random.randint(0, len(testList)-1)]
    ##

    t1 = time.time()

    return t1-t0


def testList_inList(testList):
    found = False
    check = random.randint(0, len(testList)-1)

    t0 = time.time()

    ##
 
    if check in testList:
        found = True
    ##

    t1 = time.time()

    return t1-t0


def testList_len(testList):
    t0 = time.time()

    ##
    temp = len(testList)
    ##

    t1 = time.time()

    return t1-t0


# Adding an item to a dictionary
def testDictionary_add(testdictionary):
    dictionary = testdictionary.copy()
    t0 = time.time()
    x = len(dictionary)
    dictionary["item"] = x+1
    t1 = time.time()
    return t1-t0

# Removing an item from a dictionary
# This takes a dictionary and removes the item that is index 1


def testDictionary_delete(testdictionary):
    dictionary = testdictionary.copy()
    key = str(len(dictionary) // 2)
    t0 = time.time()
    del dictionary[key]
    t1 = time.time()
    return t1-t0

# Check for an element


def testDictionary_inDictionaryMid(testdictionary):
    dictionary = testdictionary.copy()
    key = str(len(dictionary) // 2)
    # This can be changed when we know what is in the dictionary
    t0 = time.time()
    if key in dictionary:  # Nothing in the if statement because its outcome is does not matter
        key = True
    t1 = time.time()
    return t1-t0

# Check length of dictionary


def testDictionary_len(testdictionary):
    dictionary = testdictionary.copy()
    t0 = time.time()
    temp = len(dictionary)
    t1 = time.time()
    return t1-t0


## Generate lists ##
one = list(range(1, 11))
onehund = list(range(1, 100001))
twohund = list(range(1, 200001))
threehund = list(range(1, 300001))
fourhund = list(range(1, 400001))
fivehund = list(range(1, 500001))
sixhund = list(range(1, 600001))
sevhund = list(range(1, 700001))
eighthund = list(range(1, 800001))
ninehund = list(range(1, 900001))
mil = list(range(1, 1000001))

listLengths = [one, onehund, twohund, threehund,
               fourhund, fivehund, sixhund, sevhund, eighthund, ninehund, mil]
# clear unneeded variables to free up memory
del one, onehund, twohund, threehund, fourhund, fivehund, sixhund, sevhund, eighthund, ninehund, mil



## Run list tests ##

benchmark(testList_Append, listLengths, "testList_Append")
benchmark(testList_insertFront, listLengths, "testList_insertFront")
benchmark(testList_insertMiddle, listLengths, "testList_insertMiddle")
benchmark(testList_insertRandom, listLengths, "testList_insertRandom")
benchmark(testList_deleteEnd, listLengths, "testList_deleteEnd")
benchmark(testList_deleteFront, listLengths, "testList_deleteFront")
benchmark(testList_deleteMiddle, listLengths, "testList_deleteMiddle")
benchmark(testList_deleteRandom, listLengths, "testList_deleteRandom")
benchmark(testList_inList, listLengths, "testList_inList")
benchmark(testList_len, listLengths, "testList_len")


## Generate dictionaries and free up memory ##

dictOne = generateDictionary(listLengths[0])
dictOneHund = generateDictionary(listLengths[1])
dictTwoHund = generateDictionary(listLengths[2])
dictThreeHund = generateDictionary(listLengths[3])
dictFourHund = generateDictionary(listLengths[4])
dictFiveHund = generateDictionary(listLengths[5])
dictSixHund = generateDictionary(listLengths[6])
dictSevHund = generateDictionary(listLengths[7])
dictEightHund = generateDictionary(listLengths[8])
dictNineHund = generateDictionary(listLengths[9])
dictMil = generateDictionary(listLengths[10])

dictLengths = [dictOne, dictOneHund, dictTwoHund, dictThreeHund,
               dictFourHund, dictFiveHund, dictSixHund, dictSevHund, dictEightHund, dictNineHund, dictMil]  # <--- These will plug into bench func
# clear unneeded variables to free up memory
del listLengths, dictOne, dictOneHund, dictTwoHund, dictThreeHund, dictFourHund, dictFiveHund, dictSixHund, dictSevHund, dictEightHund, dictNineHund, dictMil


# Run dictionary tests

benchmark(testDictionary_add, dictLengths, "testDictionary_add")
benchmark(testDictionary_delete, dictLengths, "testDictionary_delete")
benchmark(testDictionary_inDictionaryMid, dictLengths,
          "testDictionary_inDictionaryMid")
benchmark(testDictionary_len, dictLengths, "testDictionary_len")
print("CSV Files Finished")


