# functions - a function of a set of instructions for a computer to follow
# function syntax(rulrs of how its written)
# a function comes in 2 phases: function definition and function call

#phase 1: function definition
#we are describing the instruction for our custom code
#we are addung logic to the computers vocabulary
#this does not run- it only the computer the meaning not the action

# phase 2: function call
# once we have the definitionn, we can now run the instrustions by writing the function name

#we indent to inform the computer that we are about to write
#code instructions. if we dont, we  will get an error
#example():
  # print("good day")
 #   a = input('13:')
#print (a)

# create a function that calculates 2 uniqe user inputted numbers
def calculate():
    a = input('please enter a number: ')
    b = input('please enter another number: ')
    print(int(a) + int(b))
    print(int(a) - int(b))
    print(int(a) / int(b))
    print(int(a) * int(b))

calculate()