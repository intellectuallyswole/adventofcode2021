def fuel_for_pos(crab_pos, dest_pos):
    return abs(crab_pos - dest_pos)

def fuel_cost_to_move_to_pos(input_stream, dest_pos, fuel_pos_fn):
    fuel_sum = 0
    for crab in input_stream:
        fuel_sum += fuel_pos_fn(crab, dest_pos)
    return fuel_sum



def calc_min_fuel_pos(input_stream):
    crab_list = list(map(lambda x: int(x), input_stream))
    max_horiz = max(crab_list)
    print(f"Loaded {len(crab_list)} elements, max is {max_horiz}.")

    min_fuel_cost_p1 = len(crab_list)*max_horiz
    for i in range(0, max_horiz):
        cost = fuel_cost_to_move_to_pos(crab_list, i, fuel_for_pos)
        min_fuel_cost_p1 = min(cost, min_fuel_cost_p1)
    print("Min fuel p1 "+str(min_fuel_cost_p1))

    min_fuel_cost_p2 = len(crab_list)*max_horiz*max_horiz
    for i in range(0, max_horiz):
        cost = fuel_cost_to_move_to_pos(crab_list, i, fuel_for_pos_p2)
        if cost < min_fuel_cost_p2:
            print(f"Lowering min fuiel cost from {min_fuel_cost_p2} to {cost}. New efficient location: {i}")
        min_fuel_cost_p2 = min(cost, min_fuel_cost_p2)
    return min_fuel_cost_p1, min_fuel_cost_p2

def fuel_for_pos_p2(crab_pos, dest_pos):
    summ = 0
    for i in range(1, abs(crab_pos - dest_pos)+1):
        summ += i
    return summ

print(f"Fuel for (2->2): {fuel_for_pos_p2(2,2)}")
print(f"Fuel for (2->3): {fuel_for_pos_p2(2,3)}")
print(f"Fuel for (2->4): {fuel_for_pos_p2(2,4)}")

import sys
with open(sys.argv[1]) as input_list:
    split_list = [x.split(',') for x in input_list.readlines()]
    # I hate this list flattening syntax
    flat_list = [item for sublist in split_list for item in sublist]
    (p1, p2) = calc_min_fuel_pos(flat_list)
    print(f"Fuel: p1: {p1}. p2: {p2}.")
