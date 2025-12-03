def pythonQuiz():
    print('welcome to your 5 question NFL quiz')
    score = 0
    questions = []
    print('question 1: who has the highest recieving yards in the leauge as of week 13?')
    print('A: idk','B: JSN','C: George Pickens')
    answer = input()
    if answer != 'b':
        print('Incorrect!!')
    else:
        print('Correct')  
    print('question 2: who has the most rushing yards as of week 13? ')
    print('A: Dalvin Cook', 'B: javonte williams','C: jonathan taylor')
    answer = input()
    if answer != 'c':
        print('Incorrect')
    else:
        print('correct')
    print('Question 3: Who has the most sacks in the nfl as of week 13?')
    print('A: Quinein Williams','B: Myles garrett', 'C:idk')
    answer = input()
    if answer != 'b':
        print('Incorrect')
    else:
        print('correct')
    print('Question 4: What quarterback has the most passin yards as of week 13?')
    print("A: Drake maye","B: Dak Prescott","C: Lamar Jackson")
    answer = input()
    if answer != 'a':
        print('Incorrect')
    else:
        print('correct')
    print('Question 5: Who will win the super bowl?')
    print('A: Cowboys','B: Patriots','C: Bengals')
    answer = input()
    if answer != 'a':
        print('Incorrect')
    else:
        print('correct')
    print('you have scored a ' + str(score))

pythonQuiz()