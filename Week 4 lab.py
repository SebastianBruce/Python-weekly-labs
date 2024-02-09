#Part 1
#Sebastian Bruce, 200561191
#01, 29, 2024, 5pm
#pick random letter from string

import random
'''
def randomChar(userString):
    
    #generate random number from 0 to the max length of string
    number = random.randint(0, len(userString))

    #return the character
    return userString[number]

#print and call
print(randomChar("Hello World!"))
'''


#Part 2
#Sebastian Bruce, 200561191
#01, 29, 2024, 5pm
#

def findRandom(userString2):
    
    #generate random number from 0 to the max length of string
    number = random.randint(0, len(userString2) - 1)

    #save the character
    randomLetter = userString2[number]

    #declare count variable to be changed later
    count = 0

    #check if each letter is the same as the random letter
    for i in range(len(userString2[number:])):
        if userString2[i + number] == randomLetter:
            count = count + 1

    #print results with formatting
    print("There are ", count, " instances of ", randomLetter, " in the string: \"", userString2, "\"", " after the ", number, " character.")

    return 0

def validateInput():

    #ask user for input
    userInput = input("Enter a string with no numbers: ")

    #declare flag to be changed later
    isValid = False
    
    #declare count variable to be changed later
    count = 0

    #while isValid is false run this
    while not isValid:

        #if the password has a number
        if userInput[count] == "1" or userInput[count] == "2" or userInput[count] == "3" or userInput[count] == "4" or userInput[count] == "5" or userInput[count] == "6" or userInput[count] == "7" or userInput[count] == "8" or userInput[count] == "9" or userInput[count] == "0":

            count = 0;

            #tell user their input is invalid and reprompt them
            print("Invalid input, make sure string has no numbers\nYou entered: ", "\"", userInput, "\"")
            userInput = input("Try again: ")
            
            continue

        #count is incremented every time the character is not a number
        count = count + 1;

        #this runs when the whole password is checked and no number is found
        if count == len(userInput):

            #set to true so while loop stops
            isValid = True


        #return the string the user entered
        return userInput
    

findRandom(validateInput())
