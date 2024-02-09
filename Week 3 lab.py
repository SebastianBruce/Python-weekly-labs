#Part A
#Sebastian Bruce, 200561191
#01, 22, 2024, 5pm
#pick randomly from 5 words

import random

#return a random word
def randomWord(randomNumber):
    #based off the random number passed, a word is picked and returned from the if statements
    if randomNumber == 1:
        return "Monday"
    elif randomNumber == 2:
        return "Tuesday"
    elif randomNumber == 3:
        return "Wednesday"
    elif randomNumber == 4:
        return "Thursday"
    else:
        return "Friday"
    
#call and print function and pass a random number from 1-5    
print(randomWord(int(random.randint(1,5))))



#Part B
#Sebastian Bruce, 200561191
#01, 22, 2024, 5pm
#determine string length and concatinate them

#determine smallesr and largest words and return the length of both combined
def stringLength(word1, word2, word3):
    #get length of words
    word1Len = len(word1)
    word2Len = len(word2)
    word3Len = len(word3)

    #find largest word
    if word1Len > word2Len and word1Len > word2Len:
        largest = word1
    elif word2Len > word1Len and word2Len > word3Len:
        largest = word2
    else:
        largest = word3

    #find smallest word
    if word1Len < word2Len and word1Len < word2Len:
        smallest = word1
    elif word2Len < word1Len and word2Len < word3Len:
        smallest = word2
    else:
        smallest = word3

    global together #use global variable
    
    #combine smallest and largest and return its length
    together = smallest + largest 
    return len(together)

#call function and pass 3 user inputs, determine then print if odd or even
if stringLength(input("Enter a word"), input("Enter a word"), input("Enter a word")) % 2 == 0:
    print(together, " is an EVEN number and has ", len(together), " letters.")
else:
    print(together, " is an ODD number and has ", len(together), " letters.")




    
