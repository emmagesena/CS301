## Assignment 2 ##

## Functions ##

def generateDictionary(list):
    strList = [str(int) for int in list]
    
    dict = {}

    for i in range(len(list)):
        dict[strList[i]] = list[i]

    print(dict)

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

## 