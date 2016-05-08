##age = int(input('give me your age: '))
##
##if age <= 0:
##    print('Unborn')
##elif age > 0 and age <= 150:
##    print('ALIVE')
##elif age > 150:
##    print('VAMPIRE')

##number = int(input('give me your age: '))
##
##if number % 2 == 0 and number % 3 == 0:
##    print('BOTH')
##elif number % 2 == 0 or number % 3 == 0:
##    print('ONE')
##else:
##    print('NEITHER')

n = int(input('give a number: '))


if n<0 or n>165:
    print('INVALID')
else:

    if n>50:
        baseSalary = 40*8
        extraSalary = 10*9
        aboveExtraSalary = (n-50)*10
        sumSalary= baseSalary+extraSalary+aboveExtraSalary
    elif n>=41 and n <=50:
        baseSalary = 40*8
        extraSalary = (n-40)*9
        sumSalary= baseSalary+extraSalary
    elif n<=40:
        baseSalary = n*8
        sumSalary= baseSalary

    print('YOU MADE',sumSalary , 'DOLLARS THIS WEEK')
