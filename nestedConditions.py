# Nested Conditions = a conditional statement that has other conditional statements within it(or conditions inside conditions)

#def chickenShop():
#    print(' Welcome to Mar Eats. What would you like?')
#    selection = input('please select your main food item')
#    print('1. chicken alferdo')
#    print('2. fried chicken ')
#    print('3.baked chicken and potatos')
#    print('4. sauced chicken wings')
#    print('5. mystery chicken')
#    selection = int(input('please select your main food item '))
#    if selection == 1:
#        print(' you have selected the chicken alfredo')
#        print('what side would you like?')
#        print('1. bread sticks')
#        print('2. garlic knots')
#        side = int(input())
#        if side == 1:
#            print('Great choice on the chicken alfedo and breadsticks')
#        elif side == 2:
#            print(' yummy, I love chicken alfredo and garlic knots')
#        else:
#            print('sorry we dont understand your side')

#chickenShop()





def atm():
    balance = 5000
    pin = 2025

    print('Please type in your bank pin number:')
    userPin= int(input())

    if (userPin == pin):
        print(' welcome to Mar Banking. what would you like to do?')
        print('1. withdrawl')
        print('2. deposit')
        print('3. check your balance')
        select = int(input('please select an option'))
        if select == 1:
            amount = int(input('how much would you like to widthdrawl?'))
            if amount > balance:
                print(' sorry, you do not have that much in your account brokey')               
            else:    
                newBalance = balance- amount
                print('you are taking out :' + str(amount))
                print('you have this amount left:' + str(newBalance))        
        
        elif select == 2:
            print('How much would you like to deposit?')
            amount=int(input())
            newBalance = balance + amount
            print(' you are adding:' + str(amount))
            print('your new balance is :' + str(newBalance))

        elif select == 3:
            print('your balance is :' + str(balance))

        else:
            print('sorry we dont understand your selection')
            atm()

atm()



groceries = ['words', 41, 67, True, 'new words']
print('1. withdrawl')
print('2. deposit')
print('3. check your balance')

atmMenu = ['widthdrawl','deposit','accountBalance']

print()