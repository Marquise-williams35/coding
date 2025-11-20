import random

#design
#plan for how program 'flow'; essentially, how will users 
#use the program step-by-step
'step 1: welcome user to the game'
'step 2:give user the option to play the game or check rules, settings, etc'
'step 3: if user selects the rules, show them the rules, elsestart the game'
'step 4: inform the user the game has started an instruct them sto select from rock,paper, and scissors'
'step 5: computer makes random selection'
'step 6:determine if the player loss, won, or tied and keep score'
'step 7: (loop) show the user the r,p,s options and they will continue to play until round 4'
'step 7.5: check to see if the user has one consecuative rounds- if they win 3 straight - give them a special messsage'
'step 8: determine and inform the user if the user won and return them to the main menu'

#development

def rpsGame():
    rpsOptions_cpu = ['rock','paper','scissors']

    print('welcome to the rock, paper, scissors')
    print ('please select one of the following: enter p to start the game or rules or enter r to see the rules')
    selection = input()
    if selection == 'r':
        print('here are the game rules ....')
    elif selection == 'p':
        print('The game will begin now')
        choiceUsr = input('please make a selection, r= rock, p=paper, s=scissors')
        choiceCpu = random.choice(rpsOptions_cpu)
        if choiceUsr == 'r':
            selectWrd = 'rock'
        elif choiceUsr == 'p':
            selectWrd = 'paper'
        elif choiceUsr == 's':
            selectWrd = 'scissors'
        print('user selected:' + selectWrd)
        print('Cpu selected:' + choiceCpu)
    else:
        print('sorry, we dont understand your selection')
    selection = input()

rpsGame()