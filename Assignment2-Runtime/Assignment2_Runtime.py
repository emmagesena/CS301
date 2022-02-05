## Assignment 2 ##

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
    del list[random.randint(0, len(testList)-1)]
    ##

    t1 = time.time()

    return t1-t0


def testList_inList(testList):
    t0 = time.time()

    ##
    found = False
    check = random.randint(0, len(testList)-1)

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
ten = list(range(1, 11))
hund = list(range(1, 101))
thou = list(range(1, 1001))
tenthou = list(range(1, 10001))
hundthou = list(range(1, 100001))
mill = list(range(1, 1000001))
tenmill = list(range(1, 10000001))
listLengths = [ten, hund, thou, tenthou,
               hundthou, mill, tenmill]
# clear unneeded variables to free up memory
del ten, hund, thou, tenthou, hundthou, mill, tenmill


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

dictTen = generateDictionary(listLengths[0])
dictHund = generateDictionary(listLengths[1])
dictThou = generateDictionary(listLengths[2])
dictTenThou = generateDictionary(listLengths[3])
dictHundThou = generateDictionary(listLengths[4])
dictMill = generateDictionary(listLengths[5])
dictTenMill = generateDictionary(listLengths[6])
dictLengths = [dictTen, dictHund, dictThou, dictTenThou,
               dictHundThou, dictMill, dictTenMill]  # <--- These will plug into bench func
# clear unneeded variables to free up memory
del listLengths, dictTen, dictHund, dictThou, dictTenThou, dictHundThou, dictMill, dictTenMill


# Run dictionary tests

benchmark(testDictionary_add, dictLengths, "testDictionary_add")
benchmark(testDictionary_delete, dictLengths, "testDictionary_delete")
benchmark(testDictionary_inDictionaryMid, dictLengths,
          "testDictionary_inDictionaryMid")
benchmark(testDictionary_len, dictLengths, "testDictionary_len")
