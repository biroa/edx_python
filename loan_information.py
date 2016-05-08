from math import *

#pp  = principal
#air = annual interest rate
#dur = duration
#nump= number of payments
#r  = monthly interest rate
#n  = total number of monthly

#payments for the entire duration of the loan
def loan_information(pp,air,dur):

    # Your function for calculating payment goes here
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
    
    # Your function for calculating remaining balance goes here
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
            rmb = float(pp*(numerator/denominator))
        else:
            rmb = float(pp/n)

        return rmb

    #LOAN AMOUNT: 1000.0 INTEREST RATE (PERCENT): 4.5
    print('LOAN AMOUNT:',pp,'INTEREST RATE (PERCENT):',air)
    #DURATION (YEARS): 5 MONTHLY PAYMENT: 18
    mpm = monthly_payment_for_a_loan(pp,air,dur)
    rmbm = remaining_balance_of_loan(pp,air,dur,12)
    print('DURATION (YEARS):',dur,'MONTHLY PAYMENT:',int(mpm))
    i=0
    mpmy = 0
    rmby = 0
    while(i<dur):
        #YEAR: X BALANCE: Y TOTAL PAYMENT Z
        mpmy = mpmy+ monthly_payment_for_a_loan(pp,air,dur)*12
        rmby = remaining_balance_of_loan(pp,air,dur,(i+1)*12)
        print('YEAR:',i+1,'BALANCE:',int(rmby),'TOTAL PAYMENT',int(mpmy))
        i=i+1

# Your main program goes here
principle=float(input("Enter loan amount: "))
annual_interest_rate=float(input("Enter annual interest rate (percent): "))
duration=int(input("Enter loan duration in years: "))
loan_information(principle,annual_interest_rate,duration)
