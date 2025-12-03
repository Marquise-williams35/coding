#For Loops a type of constructs that runs code instructions a finite amount of time over a group of data

#for keyword -does all the loop work


#for x in range(5):
    #word = input('please type in a word')
   # print(word)

def tf():
    for x in range(3):
        print('true or false: 3 is greater than 2')
        answer = input()
        if answer != 'true':
            print('wrong, try again')
            print('attempt:'+ str(x))
        else:
            print('great job')
            break

tf()

#looping through strings
#word = 'python'
#for letter in word:
  #  print(letter)
   # if letter =='p':
    #    print('did you mean: paper?')
    #elif letter == 'y':
     #   print('did you mean: python?')

#looping through a list of numbers


phoneShipment = []
defectivePhones= []
for x in range(10):
    print('1-make phone case')
    print('2- solder motherboard and chips for the case')
    print('3- put on screen')
    print('4- check if phone can turn on')
    doesPhonework = input('does this phone work? ')
    if doesPhonework != 'true':
        phone = 'this is phone number: ' +str(x)
        print('this phone does not work. ')
        defectivePhones.append(phone)
    else:
        print('5- place phone into the shipment box')
        phone = 'this number is phone number ' + str(x)
        phoneShipment.append(phone)

    print(phoneShipment)
    print(defectivePhones)