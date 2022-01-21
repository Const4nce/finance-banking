import math

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

#DOUBLING TIME SIMPLE INTEREST
'''
calculates how long it would take to double the balance on an account with simple interest.
'''

def doubling_time_simple_interest(rate):
    '''
    :param rate: periodic rate
    :return: how long it will take to double amount with given rate
    '''
    time = 1/rate
    return time

#DOUBLING TIME CONTINUOUS COMPOUNDING
'''
Calculates the length of time it takes to double one's money in an account/investment with continuous compounding.
The formula will return a time to double based on the term of the rate. 
For example, if the monthly rate is used, the answer to the formula will return the number of months it
takes to double. If the annual rate is used, the answer will then reflect the number of years to double.
'''

def doubling_time_continuous_compounding(rate):
    '''
    :param rate: rate of return
    :return: length of time (in months or years given the rate)
    '''
    dtcc = math.log(2)/rate
    return(dtcc)