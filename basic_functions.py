import numpy as np
import math
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


def future_value_factor(rate, periods, **kwargs):
    factor = kwargs.get('factor', True)
    fv = kwargs.get('future_value', None)
    if factor:
        fvf = (1 + rate) ** periods
    if fv:
        fvf = (1 + rate) ** periods * fv
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


# COMPOUND INTEREST
'''
calculates the amount of interest earned on an account or investment where the amount earned is reinvested.
By reinvesting the amount earned, an investment will earn money based on the effect of compounding.
Compounding is the concept that any amount earned on an investment can be reinvested to create additional 
earnings that would not be realized based on the original principal, or original balance, alone. 
The interest on the original balance alone would be called simple interest. 
The additional earnings plus simple interest would equal the total amount earned from compound interest.
The rate per period (r) and number of periods (n) in the compound interest formula must match how often 
the account is compounded. For example, if an account is compounded monthly, then one month would be one period.
Suppose an account with an original balance of $1000 is earning 12% per year and is compounded monthly.
Due to being compounded monthly, the number of periods for one year would be 12 and the rate would be 1% (per month).
'''

def compound_interest(amount, rate, periods,**kwargs):
    apy = kwargs.get('APY', False)
    ending_balance = kwargs.get('ending_balance', False)
    if not apy:
        ci = amount*((1+rate)**periods-1)
    elif apy:
        #when apy is true the function returns the effective rate
        ci = (1+rate)**periods-1
    elif ending_balance:
        ci = amount*((1+rate)**periods)
    return ci


# CONTINUOUS COMPOUND INTEREST
'''
interest earned on an account that is constantly compounded, essentially leading to an infinite amount of 
compounding periods.The effect of compounding is earning interest on an investment, or at times paying interest 
on a debt, that is reinvested to earn additional monies that would not have been gained based on
the initial (principal)balance alone. By earning interest on prior interest, one can earn at an exponential rate.
Instead of compounding interest on an monthly, quarterly, or annual basis, continuous compounding 
will effectively reinvest gains perpetually.
'''
def continuous_compound_interest(amount, rate, time):
    cci=(amount * (pow((1 + rate/100), time)) ) - amount
    return round(cci,2)

# TODO: add result as rate argument