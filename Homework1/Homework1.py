'''
Emma Ogle 
CS 301 
Homework 1 

'''


'''

Methods 
...
All functions used in this program are 
in this section. 

'''

def wordValidator(searchWord):
    if searchWord in words:
        print("\nThe word", searchWord, "was found in dictionary and is valid")
    else:
        print("\nword not found in dictionary")


def wordValidatorBool(searchWord):
   if searchWord in words:
       return True
   else:
       return False


def checkTiles(searchWord):
    tilesCopy = tiles.copy()
    wordAssembled = True

    for i in range(len(searchWord)):

        if searchWord[i] in tilesCopy:
            tilesCopy[tilesCopy.index(searchWord[i])] = ''

        else:
            wordAssembled = False
            break

    if wordAssembled:
        print("\n",searchWord,"found in tiles")
   
def convertTuple(tup):
    str = ''.join(tup)
    return str

def SBWordFinder(puzzleList, centerLetter):
    for i in range(len(words)):
        wordFound = True
        LFound = False
        for j in range(len(words[i])):
            if words[i][j] not in puzzleList:
                wordFound = False
                break
            if words[i][j] == centerLetter:
                LFound = True

        if wordFound and LFound and len(words[i]) >= 5:
            print("\n",words[i],"found")


#Finds eight letter words from words list 

def findEights():
    eights = []
    count = 0
    for i in range(len(words)):

        for j in range(len(words[i])):
            count += 1

        if count == 8:
            eights.append(words[i])

        count = 0
   
    return eights


#Gives each letter from the alphabet a 'score' based on how many occurences there are in eight letter words
def scoreAlphabet():
    alphabet = {
        'a' : 0,
        'b' : 0,
        'c' : 0,
        'd' : 0,
        'e' : 0,
        'f' : 0,
        'g' : 0,
        'h' : 0,
        'i' : 0,
        'j' : 0,
        'k' : 0,
        'l' : 0,
        'm' : 0,
        'n' : 0,
        'o' : 0,
        'p' : 0,
        'q' : 0,
        'r' : 0,
        's' : 0,
        't' : 0,
        'u' : 0,
        'v' : 0,
        'w' : 0,
        'x' : 0,
        'y' : 0,
        'z' : 0
        }

    for i in range(len(eightLetterWords)):
        for j in range(len(eightLetterWords[i])):
            if eightLetterWords[i][j] in alphabet.keys():
                alphabet[eightLetterWords[i][j]] += 1
           
    return alphabet


def sortAlphabet(dictionary):
    
    sortedKeys = sorted(dictionary, key=dictionary.get, reverse=True)
    sortedDict = {}

    for i in sortedKeys:
        sortedDict[i] = dictionary[i]

    letters = []
    letters = sortedDict.keys()

    return list(letters)
   








#Read words.txt and store words into list 

with open('words.txt') as f:
    words = f.readlines()

for i in range(len(words)):
    words[i] = words[i].rstrip('\n')       
    
        

# Question 1: What is the sum of the first n positive integers?

print("\nQuestion 1 : What is the sum of the first n positve integers?")

n = int(input("Enter value for n: "))

currentNum = 1
sum = 0

for i in range (n):
    sum += currentNum
    print(sum)
    currentNum += 1
   

print("The sum of the first", n, "integers is", sum)



# Question 2: Given a proposed word that someone wants to play, can you check that it is a valid word?

print("\nQuestion 2: Given a proposed word that someone wants to play, can you check that it is a valid word?")

search = input("Enter word to validate: ")

wordValidator(search)


   

# Question 3: Given a set of tiles and a word, can you check if the word can be made from the tiles? 

print("\nQuestion 3: Given a set of tiles and a word, can you check if the word can be made from the tiles?")

print("Enter characters for your 7 tiles.")

tiles = ['','','','','','','']

for i in range(7):
    tiles[i] = input("Enter another: ")

checkWord = input("Enter word to check for:")

if wordValidatorBool(checkWord):
    checkTiles(checkWord)
else:
    print("Word entered is not valid.")
        

# Question 4: Given a set of tiles, find all words you can make with them

print("\nQuestion 4: Given a set of tiles, find all words you can make with them (using tiles from last question)")

'''
Note:
In the homework, it was indicated in the example that we were supposed to find only the anagrams (7 letter words) from the scrabble tiles,
so that is all I am doing in this section. However, I would use a method similar to SBWordFinder used in Question 5
if I wanted to find all words possible regardless of size 

'''
print(tiles)


from itertools import permutations

wordsFound = False

permList = list(permutations(tiles))


for i in range(len(permList)):
    permWord = convertTuple(permList[i])
    if wordValidatorBool(permWord):
        wordsFound = True
        print("Word found:", permWord)


if not wordsFound:
    print("No words found in tiles")
   

# Question 5:  Can you write a function that tells all of the possible words for the Spelling Bee Puzzle?

print("\nQuestion 5:  Can you write a function that tells all of the possible words for the Spelling Bee Puzzle? \nMust be 5+ letters and contain the middle letter, L")

puzzle = ['r','a','b','l','c','i','n']

middleLetter = 'l'

'''
Note:
The specific letters from the puzzle in the assignment have been hardcoded into the program. The middle letter is also hardcoded
and used to adhere to the rules described in the homework. 

'''
  
SBWordFinder(puzzle,middleLetter)


# Question 6: What set(s) of eight letters forms the most possible bingos?

print("\nQuestion 6: What set(s) of eight letters forms the most possible bingos?")

eightLetterWords = findEights()

scoredAlphabet = scoreAlphabet()


sortedLetters = sortAlphabet(scoredAlphabet)

for i in range(8):
    print(sortedLetters[i])





    


