import basic_functions

# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    my_si = basic_functions.simple_interest(1000, 0.1, 3, ending_balance=True)
    # value = future_value(1000, 0.005, 12, present_value = 1061.68)
    print(my_si)