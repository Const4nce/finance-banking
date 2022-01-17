import basic_functions

# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    # value = future_value(1000, 0.005, 12, present_value = 1061.68)
    value = basic_functions.future_value_factor(0.01, 12, future_value=500)

    print(value)