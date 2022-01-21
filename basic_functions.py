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
calculates the future value of an amount per unit of its present value. 
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
def number_of_periods(future_value, present_value, rate, **kwargs):
    annuity = kwargs.get('annuity', False)
    amount = kwargs.get('amount', None)
    if annuity:
        if amount == None:
            raise ValueError("amount is required for number of periods annuity")
        n_periods = math.log((1+(future_value*rate)/amount)/math.log(1+rate))
    else:
        n_periods = (math.log(future_value/present_value))/(math.log(1+rate))
    return round(n_periods, 2)


# NUMBER OF PERIODS - ANNUITY
# DOUBLING TIME
'''
calculates the length of time required to double an investment or money in an account with interest.
The rate in the doubling time formula represents the rate per period. 
To calculate the amount of time to double  money in an account that is compounded monthly, 
then the rate needs to express the monthly rate and not the annual rate.
The monthly rate can be found by dividing the annual rate by 12. With this situation, 
the doubling time formula will give the number of months that it takes to double money and not years.
The effective annual rate or annual percentage yield can also be used as the rate in this formula. 
'''

def doubling_time(rate):
    '''
    :param rate: rate per period
    :return: number of years/months it takes to double money
    '''
    time = math.log(2)/math.log(1+rate)
    return time


# Rule of 72
'''
Simple formula to estimate the length of time required to double an investment.
The rule of 72 is primarily used in off the cuff situations where an individual needs to make 
a quick calculation instead of working out the exact time it takes to double an investment. 
The rule of 72 can also be used to estimate the rate needed to double an investment within a specific time period.
'''
def rule_72_time(rate):
    '''
    :param rate: rate expressed as a whole number
    :return: length of time required to double an investment
    '''
    time = 72/rate
    return time

def rule_72_rate(time):
    '''
    :param time: length of time available to double the investment
    :return: rate needed to double an investment within given time
    '''
    rate=72/time
    return rate