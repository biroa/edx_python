n = int(input('give a number: '))


if n<0 or n>168:
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
