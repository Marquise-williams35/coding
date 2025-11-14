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
        print('whats up vhat, welcome to tiktok teens , 67')
        tt_teens.append(usrAge)
    else:
        print('welcome to tiktok')
        tt_standard.append(usrAge)
#signup()

#step 1:
#perform all types of simple math
#be able to calculate a unit of space like area or perimiter. 
length = input('please enter a number: ')
width = input('please enter another number: ')
height = input('please enter one more number:')
print(int(length) * int(width) * int(height))


#step 2:
#use a loop to let the user enter as many numbers as they want and also solve it in anyway that they want.
