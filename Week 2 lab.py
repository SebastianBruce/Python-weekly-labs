#Excersize 1
if 14 == 14:
    print("They are equal")

#Excersize 2
number = input("Input a number")
number = int(number)

if number > 10:
    print("Your number is greater than 10")
else:
    print("Your number is less than 10")

#Excersize 3
if number > 0:
    print("Your number is positive")
elif number < 0:
    print("Your number is negative")
else:
    print("Your number is 0")

#Excersize 4
letter = input("Input a letter")
if letter == "a" or letter == "e" or letter == "i" or letter == "o" or letter == "u" or letter == "y":
    print("Your input is a vowel")
    print(number)
else:
    print("Your input is not a vowel")

#Excersize 5
number2 = input("Input a number")
number2 = int(number2)

if number > number2:
    print(number, "is greater than ", number2)
else:
    print(number2, "is greater than ", number)

#Excersize 6
year = input("Input a year")
year = int(year)
if year % 4 == 0:
    print(year, "is a leap year")
else:
    print(year, "is not a leap year")

#Excersize 7
age = input("Enter your age")
age = int(age)
if age > 12 and age < 20:
    print("You are a teenager")
else:
    print("You are not a teenager")

#Excersize 8
number3 = input("Input a number")
number3 = int(number3)
if number3 % 2 == 0:
    print(number3, "is even")
else:
    print(number3, "is odd")

#Excersize 9
number4 = input("Input a number")
number4 = int(number4)
printedNumber = 0

while number4 > 0:
    printedNumber = printedNumber + 2
    print(printedNumber)
    number4 = number4 - 2

#Excersize 10
for i in range(5):
    print(i + 1)

#Excersize 11
number5 = input("Input a number")
number5 = int(number5)
while not number5 > 5:
    number5 = input("Input a number")
    number5 = int(number5)

#Excersize 12
number6 = input("Input a number")
number6 = int(number6)
for i in range(number6):
    print(number6 * (i + 1))

#Excersize 13
number7 = 10
while number7 > 0:
    print(number7)
    number7 = number7 - 1

#Part A
#Excersize 14
#Sebastian Bruce, 200561191
#01, 15 2024, 6pm
#Ask user for color, check if its light or dark
userColor = input("Pick a color: Black, White, Yellow, Red, Blue, Orange")
if userColor == "black" or userColor == "red" or userColor == "blue":
    print(userColor, "is a dark color")
elif userColor == "white" or userColor == "yellow" or userColor == "orange":
    print(userColor, "is a light color")
else:
    print("not an option")


#Part B
#Sebastian Bruce, 200561191
#01, 15 2024, 6pm
#Ask user for number that is even and greater than 9
userNumber = input("Input a number greater than 9")
userNumber = int(userNumber)    
printedNumber = 0

while userNumber % 2 == 1 or userNumber < 9:
    userNumber = input("Input an even number greater than 9")
    userNumber = int(userNumber)
while userNumber > 0:
    printedNumber = printedNumber + 2
    print(printedNumber)
    userNumber = userNumber - 2


    

