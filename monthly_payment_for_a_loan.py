from math import *
#pp  = principal
#air = annual interest rate
#dur = duration
#r   = monthly interest rate
#n   = total number of monthly payments
#      for the entire duration of the loan

def monthly_payment_for_a_loan(pp, air, dur):
    pp = abs(float(pp))
    air = float(air)
    dur = abs(int(dur))
    r = (air/100/12)
    n = dur*12
    if r!=0:
        numerator = r*pow((1+r),n)
        denominator = pow((1+r),n)-1
        mp = float(pp*(numerator/denominator))
    else:
        mp = float(pp/n)

    return mp
    
    

print('result:',monthly_payment_for_a_loan(1000.0,4.5,5))
