#down = input('what down is it?')
#yards = input( 'how many yards do we need for the first down?')



#if down == 1 and yards < 5:
 #   print(' run the ball')
#elif down == 2 and yards < 0:
 #   print('pass the ball')
#elif down == 3 and yards == 6:
 #   print('pass the ball')
#else:
   # print('punt')    
#def permitcheck():
    #elif age >= 16: 
   #    print(' you are elligible for a permit')
  #      else:
 #       print(' you are not elligible for a permit')
        
#permitcheck(16)

#conditional statements- code instructions that have different outcomes vased on inputted data
#input --> condition -->

#conditional statement Syntax
# if keyword - controls the condition we want to satisfy

# elif keyword - same thing as the if keyword

#else keyword - our default outcome. The thing that happens when our conditions are NOT satistied

#def weather():
#    weather = input('what is the weather like today?')
#    if weather == 'sunny':
#        print('it bis beautiful outside. Bring sunglasses')
 #   elif weather == "rainy":
#        print(' remember to bring an umbrella')
#    elif weather == "windy":
#        print( ' wear heavy boots')

def positivenegativecheck(number):
    if number <= 0:
        print('this number is negative')
    elif number >= 0:
        print('this number is positive')

 #positivenegativecheck(-6)

def gradescore(grade):
    if grade >=90:
        print('you have an A')
    elif grade >= 80:
        print('you have a B')
    elif grade >= 70:
        print('you have a C')
    elif grade <= 60:
        print('you are failing')

gradescore(67)