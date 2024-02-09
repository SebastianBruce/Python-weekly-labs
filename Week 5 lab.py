#Part 1
#Sebastian Bruce, 200561191
#02, 05, 2024, 5pm
#shuffle a list and remove 3 values

import random
'''
def shuffleAndRemove(listOfTen):

    #declare variables and pick a random number
    randomOne = random.randint(0,9)
    randomTwo = random.randint(0,9)
    randomThree = random.randint(0,9)

    #ensure no 2 numbers are ever the same
    while(randomOne == randomTwo or randomTwo == randomThree or randomOne == randomThree):
        randomOne = random.randint(0,9)
        randomTwo = random.randint(0,9)
        randomThree = random.randint(0,9)

    #shuffle the list
    random.shuffle(listOfTen)

    #convert each random integer to its respective value in the list
    randomOne = str(listOfTen[randomOne])
    randomTwo = str(listOfTen[randomTwo])
    randomThree = str(listOfTen[randomThree])

    #print the values removed
    print("The values removed are:", randomOne, randomTwo, randomThree)

    #remove the values
    listOfTen.remove(randomOne)
    listOfTen.remove(randomTwo)
    listOfTen.remove(randomThree)

    #return the new list
    return listOfTen

#call the function
shuffleAndRemove(['one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine', 'ten'])
'''






#Part 2
#Sebastian Bruce, 200561191
#02, 05, 2024, 5:30pm
#get list from user and sort it

def getInputAndValidate():

    #declare list
    listOfFive = []

    #run 5 times, store a user string to the list
    for i in range(5):

        #get user input
        userString = input("Enter string "  + str(i + 1) + " made of letters and numbers: ")

        #declare switch that will be made true if input is valid
        isValid = False

        #run the loop until user input is valid
        while not(isValid):

            #check if string has letters AND numbers only
            if userString.isdecimal() or userString.isalpha():
                userString = input("Invalid string, make sure its only letters and numbers: ")
                continue

            #flip switch to true if all characters are valid
            isValid = True

            #add user string to the list
            listOfFive.append(userString)

    #return full list       
    return listOfFive

def sortList(userList):
    
    #run 4 times
    for i in range(4):

        #store a letter from the first string at the index of i
        firstWordLetter = userList[0][i]

        #run 4 times
        for j in range(4):

            #test stored letter against first letter of each word
            if firstWordLetter == userList[j + 1][0]:

                #if it hits, store that word
                grabbedWord = userList[j + 1]

                #remove that word
                userList.pop(j + 1)

                #append that word to the end of the list
                userList.append(grabbedWord)

    #return the list
    return userList
                    
#call the functions
print(sortList(getInputAndValidate()))
