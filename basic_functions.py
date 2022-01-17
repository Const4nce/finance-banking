import numpy as np

# PRESENT VALUE
'''
calculates the present day value of an amount that is received at a future date;
Time value of money is the concept that receiving something today is worth more 
than receiving the same item at a future date. The presumption is that it is 
preferable to receive $100 today than it is to receivethe same amount one year from today.
But what if the choice is between $100 present day or $106 a year from today? 
A formula is needed to provide a quantifiable comparison between an amount today and 
an amount at a future time, in terms of its present day value.

main function: when cashflow in future period is available
alternative function: when future value is available 
'''


def present_value(cashflow_period_1, rate, periods, **kwargs):
    fv = kwargs.get('future_value', None)
    if fv:
        pv = fv * (1/((1+rate)**periods))
    else:
        pv = cashflow_period_1/(1+rate)**periods
    return round(pv, 2)


# FUTURE VALUE
'''
calculate the value of a cash flow at a later date than originally received.
If one wanted to determine what amount they would like to receive one year from
 now in lieu of receiving $100 today, the individual would use the future value formula. 

main function: when cashflow in present period is available
alternative function: when present value is available '''


def future_value(cashflow_period_0, rate, periods, **kwargs):
    pv = kwargs.get('present_value', None)
    if pv:
        fv = pv * ((1+rate)**periods)
    else:
        fv = cashflow_period_0 * ((1+rate)**periods)
    return round(fv, 2)


# FUTURE VALUE FACTOR
'''
calculates the future value of an amount per dollar of its present value. 
An amount of $105 to be received a year from now may be okay if the individual 
wants $100 today, assuming that the individual can earn 5% otherwise in one year.
'''


def future_value_factor(rate, periods):
    fvf = (1+rate)**periods
    return round(fvf, 2)


# NUMBER OF PERIODS
def number_of_periods(future_value, present_value, rate):
    n_periods = (np.log(future_value/present_value))/(np.log(1+rate))
    return round(n_periods, 2)


# SIMPLE INTEREST
'''
calculates the interest accrued on a loan or savings account that has simple interest. 
An example of a simple interest calculation would be a 3 year saving account at a 10% rate
 with an original balance of $1000. By inputting these variables into the formula, 
 $1000 times 10% times 3 years would be $300.
 Simple interest is money earned or paid that does not have compounding. 
 Compounding is the effect of earning interest on the interest that was previously earned.
 With this formula it is assumed that no amount was earned on the interest that was earned in prior years.
'''


def simple_interest(amount, rate, time, **kwargs):
    eb = kwargs.get('ending_balance', False)
    if not eb:
        si = amount*rate*time
    elif eb:
        si = amount*(1+rate*time)
    return si
