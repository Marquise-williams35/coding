# Function needs to have a list of 4 words/ strings - DONE
# Function needs to take 1 word from list randomly - DONE
# Selected word needs to be randomized/ shuffled - DONE
# Allow user to guess the original / correct word. - DONE
# IF it is correct, they ELSE they lose - DONE

# Add logic that will allow the user to make 3 guessing attempts
# and show the user the number of attempts they have
 
import random

def WordScramblerGame():
    wordPool = ["computer",'moniter','programming','mouse']
    correctWord =''

    print("Welcome to scrambled! ")
    randomSelect = random.randint(0,3)

    if randomSelect == 0:
        correctWord = wordPool[0]
    elif randomSelect == 1:
        correctWord = wordPool[1]
    elif randomSelect == 2:
        correctWord = wordPool[2]
    elif randomSelect == 3:
        correctWord = wordPool[3]
    
    convertedString = list(correctWord)

    random.shuffle(convertedString)
    scrambled = "".join(convertedString)
    
    for x in range (3):
        print("Please guess the correct word: " + scrambled)
        userGuess = input()
        if userGuess == correctWord:
            print("You Win!")
            break
        else:
            print("Sorry, you lose.")

WordScramblerGame()