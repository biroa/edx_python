from math import *
#pp  = principal
#air = annual interest rate
#dur = duration
#nump= number of payments
#r   = monthly interest rate
#n   = total number of monthly payments
#      for the entire duration of the loan

def remaining_balance_of_loan(pp, air, dur, nump):
    pp  = abs(float(pp))
    air = float(air)
    dur = abs(int(dur))
    nump= int(nump)
    r = (air/100/12)
    n = dur*12
    if r!=0:
        numerator = pow((1+r),n)-pow((1+r),nump)
        denominator = pow((1+r),n)-1
        mp = float(pp*(numerator/denominator))
    else:
        mp = float(pp/n)

    return mp

print('result:',remaining_balance_of_loan(1000.0,4.5,5,12))
