def signup():
    dob = int(input('what year were you born?'))
    tt_kids = []
    tt_teens = []
    tt_standard = []
    currntYr = 2025
    usrAge = currntYr - dob
    if usrAge <12:
        print(' welcome to tiktok kids')
        tt_kids.append(usrAge)
    elif usrAge > 12 and usrAge < 18:
        print('whats up, welcome to tiktok teens , 67')
        tt_teens.append(usrAge)
    else:
        print('welcome to tiktok')
        tt_standard.append(usrAge)
signup()

#step 1:
#let users graph points from a equation
#users can solve problems from first grade all the way up to college level
#perform all types of simple math
#be able to calculate a unit of space like area or perimiter. 
length = input('please enter a number: ')
width = input('please enter another number: ')
height = input('please enter one more number:')
print(int(length) * int(width) * int(height))


#step 2:
'use a loop to let the user enter as many numbers as they want '
'also let users use any form of math like, addition, subtraction, etc'
'i would also like to allow users to enter formulas but instead of solving the question for them it can give them a step by step on how to solve the equation'

#example:
def add():
    num1= int(input('please type in a number'))
    num2 =int(input('please type in another number'))
    sum = num1+ num2
    print('sum =' + str(sum))
    bonusNum = input('would you like to add another number to the sum: ')
    if bonusNum == 'y':
        numX = int(input('please type in number'))
        sum += numX
        print(sum)

#add()