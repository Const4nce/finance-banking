import basic_functions

# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    # value = future_value(1000, 0.005, 12, present_value = 1061.68)
    value = basic_functions.continuous_compound_interest(10000, 10.25, 5, ending_balance=False)

    print(value)