import math

# LOAN PAYMENT
'''
Calculates loan payments (same as the formula used for ordinary annuity). 
Used for standard loans amortized for a specific period of time with a fixed rate.
It is important to keep the rate per period and number of periods consistent with one another in the formula.
If the loan payments are made monthly, then the rate per period needs to be adjusted to the monthly rate 
and the number of periods would be the number of months on the loan.
If payments are quarterly, the terms of the loan payment formula should be adjusted accordingly.
'''
def standard_loan_payment(pv, r, n):
    '''
    :param pv: present value
    :param r: rate per period
    :param n: number of payments
    :return: payment on a loan
    '''
    p = (r*(pv))/(1-(1+r)**-n)
    return round(p, 2)


# BALLOON BALANCE OF A LOAN
'''
Calculates the amount due at the end of a balloon loan. 
A balloon loan is a loan that has a term that is shorter than its amortization, meaning
the loan payment will be amortized, or calculated, for a certain amount of years 
but the loan will be paid off before all payments calculated are made, thus leaving a balance due. 
An example would be a loan that is calculated for 30 years, but the remaining balance after 
10 years must be paid in one full sum. This example is commonly referred to as a 10/30 balloon.
Often used with mortgages and leases.
'''
def remaining_balance_loan(b, p, r, n):
    '''
    :param b: original balance
    :param p: payment
    :param r: rate per payment
    :param n: number of payments
    :return: future value (remaining or balloon balance)
    '''
    fv = b*(1+r)**n - (p * ( ((1+r)**n) -1 )/r)
    return round(fv,2)

#TODO: change description