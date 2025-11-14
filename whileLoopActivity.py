#    numberInput = int(input('Please enter your numbers: '))
   
 #   while numberInput != 'quit':
 #   numberList.append(numberInput)
 #   print(numberList)
 #   print('ur code is working')
  #  numberList =[]
   
#Activity 1

#def numberListLoop():
#    numberList=[]
#   userNumber = input('type in a number')
 #   while userNumber != 'quit':
  #      newNumber= int(userNumber)
   #     numberList.append(newNumber)
    #    print(numberList)
     #   userNumber= input('type in a number')

#numberListLoop()

#Activity 2
def calcKinda():
    UsersNumbers =[]
    Enterednumbers = input('enter your first number')
    while UsersNumbers != 'quit':
        Enterednumbers = int(Enterednumbers)
        UsersNumbers.append(Enterednumbers) 
        print(UsersNumbers)
        Enterednumbers = input('type in a number')
        sum(UsersNumbers)
calcKinda()