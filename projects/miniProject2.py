def GpaCalc():
    class_name = input('please enter your subject: ')
    print('enter each grade for ' + (class_name) +' class')
    semesterWeeks = (17)
    week_1_grades = input()
    week_2_grades = input()
    week_3_grades = input()
    week_4_grades = input()
    week_5_grades = input()
    week_6_grades = input()
    week_7_grades = input()
    week_8_grades = input()
    week_9_grades = input()
    week_10_grades = input()
    week_11_grades = input()
    week_12_grades = input()
    week_13_grades = input()
    week_14_grades = input()
    week_15_grades = input()
    week_16_grades = input()
    week_17_grades = input()
    fullSemesterGrades= (int(week_1_grades) + int(week_2_grades) + int(week_3_grades) + int(week_4_grades) + int(week_5_grades) + int(week_6_grades) + int(week_7_grades) + int(week_8_grades) + int(week_9_grades) + int(week_10_grades) + int(week_11_grades)+ int(week_12_grades)+ int(week_13_grades)+ int(week_14_grades)+ int(week_15_grades)+ int(week_16_grades)+ int(week_17_grades))
    finalGrade = str(fullSemesterGrades/semesterWeeks)
    print('your final ' + (class_name) + ' grade is ' + (finalGrade))

#GpaCalc()

def gpaCalculator():
    print(' What subject is this GPA for? ')
    subject = input()
    print("the user entered: "+ subject)
    week = 0
    sum = 0
    for week in range(17):
        print('Please enter the grade for week : '+ str(week))
        grade = int(input())
        sum += grade
        week += 1
        gpa = sum / 10
    if gpa > 70 and gpa < 80:
        print('C')
    elif gpa > 80  and gpa < 90:
        print('B')
    elif gpa > 90  and gpa <100:
        print('A')
    else:
        print('F')
    print('your gpa for '+ subject + ' is ' + str(gpa))

gpaCalculator()