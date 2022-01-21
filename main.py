import basic_functions, interest_functions, loan_functions

# TODO: set up testing

if __name__ == '__main__':
    # value = basic_functions.future_value(1000, 0.005, 12, present_value = 1061.68)
    value = loan_functions.standard_loan_payment(76008.88, .005, 60)
    print(value)
