import random
import matplotlib.pyplot as plt

def random_walk(*,initial_state, volatility, decimal_places, number_of_elements, return_target):
    lower_range = -volatility*(10**decimal_places)
    upper_range = volatility*(10**decimal_places)
    output_list = []
    run_flag = True
    while run_flag:
        out_list = []
        temp_init = initial_state
        for i in range(number_of_elements):
            out_list.append(initial_state)
            add_val = random.randrange(lower_range,upper_range,2)
            add_val = add_val/(10**decimal_places)
            initial_state += add_val
            initial_state = round(initial_state, decimal_places)
        initial_state = temp_init
        percent_return = (out_list[-1] - out_list[0])*100/out_list[0]
        print(percent_return)
        if return_target < 0:
            if (percent_return < return_target) and (percent_return >= return_target - 3):
                run_flag = False
                output_list = out_list
        elif return_target >= 0:
            if (percent_return > return_target) and (percent_return <= return_target + 3):
                run_flag = False 
                output_list = out_list
    return out_list

def generateRandomWalk(*, initial_state, divisions_of_returns, size_of_list):
    end_out_list = []
    for i in divisions_of_returns:
        out_list = random_walk(initial_state = initial_state, volatility = 4, decimal_places = 2, number_of_elements = size_of_list, return_target = i)
        end_out_list.extend(out_list)
        initial_state = end_out_list[-1]
        print(initial_state)

    return end_out_list

stock_price_array = generateRandomWalk(initial_state = 100, divisions_of_returns=[10,10,-2,12,24,-10, -12, -9], size_of_list = 252)
print(stock_price_array)
print(len(stock_price_array))

plt.plot(stock_price_array)
plt.show()