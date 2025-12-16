#question 1
def ageChecker(age):
    if age >=18:
        print('you can vote')
    elif age <=18:
        print('you cannot vote')



#question 2
def maxNumber():
    a = int(input('please enter your first number:'))
    b = int(input('please enter another number:'))
    c = int(input('please enter one more number:'))
    hiNumber = max(a,b,c)
    print(hiNumber)
maxNumber()
#question 3
def movieTicketprice(age):
    if age <=13:
        print('price= 10.00')
    elif age >=14 and age <25:
        print('price= 15.00')
    elif age >=2 and age <55:
        print('price= 20.00')
    elif age >=55:
        print('price= 10.00')
#movieTicketprice(27)