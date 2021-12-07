
if False:
    # Part A
    with open('input.txt') as input_f:
        depth = 0
        dist = 0
        for lin in input_f:
            (move, sz) = lin.split(" ")
            sz = int(sz)
            if move == "forward":
                dist += sz
            elif move == "up":
                depth -= sz
            elif move == "down":
                depth += sz
        print(f"Depth {depth}, distance {dist}, mult {depth*dist}")


with open('input.txt') as input_f:
    depth = 0
    dist = 0
    aim = 0
    for lin in input_f:
        (move, sz) = lin.split(" ")
        sz = int(sz)
        if move == "forward":
            dist += sz
            depth += aim * sz
        elif move == "up":
            aim -= sz
        elif move == "down":
            aim += sz
    print(f"B: Depth {depth}, distance {dist}, mult {depth*dist}")


