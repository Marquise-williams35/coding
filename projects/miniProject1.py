
def NFLquiz():
    print('welcome to your 5 question NFL quiz')
    score = 0
    print('question 1: who has the highest recieving yards in the leauge as of week 13?')
    print('A: Devonte Adams','B: JSN','C: George Pickens')
    answer = input()
    if answer == 'b':
        score +=1
        print('correct!!')
    else:
        print('incorrect')  
    print('question 2: who has the most rushing yards as of week 13? ')
    print('A: Dalvin Cook', 'B: javonte williams','C: jonathan taylor')
    answer = input()
    if answer == 'c':
        score +=1
        print('correct')
    else:
        print('incorrect')
    print('Question 3: Who has the most sacks in the nfl as of week 13?')
    print('A: Quinein Williams','B: Myles garrett', 'C: Will Anderson')
    answer = input()
    if answer == 'b':
        score +=1
        print('correct')
    else:
        print('incorrect')
    print('Question 4: What quarterback has the most passin yards as of week 13?')
    print("A: Drake maye","B: Dak Prescott","C: Lamar Jackson")
    answer = input()
    if answer == 'b':
        score +=1
        print('correct')
    else:
        print('incorrect')
    print('Question 5: Who will win the super bowl?')
    print('A: Cowboys','B: Patriots','C: Bengals')
    answer = input()
    if answer == 'a':
        score +=1
        print('correct and ur goated')
    else:
        print('incorrect')
    
    print('you have scored a ' + str(score))

#NFLquiz()

def PythonQuiz():
    print('welcome to your 5 question python quiz')
    score = 0
    print('question 1: what is a comparison opperator?')
    print('A: a line of code used to test if a sequence is presented in an object')
    print('B: a line of code used to compare two values')
    print('C: a line of code used with numeric values to perform common mathematical operations')
    answer = input()
    if answer == 'b':
        score +=1
        print('correct!!')
    else:
        print('incorrect')
    print('question 2: what is a list?')
    print('A: Code used to store multiple items in a single variable.')
    print('B: Code surrounded by either single quotation marks, or double quotation marks.')
    print('C: Code that can store data of different types, and different types can do different things.')
    answer = input()
    if answer == 'a':
        score +=1
        print('correct!!')
    else:
        print('incorrect')
    print('question 3: True or false: "A interger variable can use only numbers"?')
    print('A: False')
    print('B: True')
    answer = input()
    if answer == 'b':
        score +=1
        print('correct!!')
    else:
        print('incorrect')
    print('question 4: Booleans will tell you if a code is true or false ')
    print('A:True')
    print('B: False')
    answer = input()
    if answer == 'a':
        score +=1
        print('correct!!')
    else:
        print('incorrect')
    print('Time for a hard one')
    print('question 5: what does a float do?')
    print('A: Changes any number data type into a decimal number ')
    print('B: Returns a sequence of numbers, starting from 0 by default, and increments by 1')
    print('C: Prints the specified message to the screen, or other standard output device.')
    answer = input()
    if answer == 'a':
        score +=1
        print('correct!!')
    else:
        print('incorrect')
    print('you have scored a ' + str(score))
PythonQuiz()


