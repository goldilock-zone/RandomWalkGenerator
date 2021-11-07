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

        if return_target < 0:
            if (percent_return < return_target) and (percent_return >= return_target - 3):
                run_flag = False
                output_list = out_list
        elif return_target >= 0:
            if (percent_return > return_target) and (percent_return <= return_target + 3):
                run_flag = False 
                output_list = out_list
    return out_list

def generateRandomWalk(*,company_name, initial_state, divisions_of_returns, size_of_list):
    end_out_list = []
    ctr = 1
    for i in divisions_of_returns:
        start_price = initial_state
        out_list = random_walk(initial_state = initial_state, volatility = 2, decimal_places = 2, number_of_elements = size_of_list, return_target = i)
        end_out_list.extend(out_list)
        initial_state = end_out_list[-1]
        end_price = initial_state

        plt.plot(end_out_list, color = "green")
        plt.xlabel('time')
        plt.ylabel('price')
        plt.title(f"{company_name} | Start Price {start_price} | End Price {end_price} ")
        plt.savefig(f"{company_name}_Timeslot{ctr}.pdf")
        plt.clf()
        ctr += 1

    return end_out_list

stock_price_array = generateRandomWalk(company_name = "Borosil Energy",initial_state = 100, divisions_of_returns=[-10,-1,2,-15,5,5,-2,7,6,0,4,1,15,-7,0,3,4,-5,2,4,15,1,2,-3,4], size_of_list = 100)



