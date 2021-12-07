
def main_a(input):
    prev = None
    inc_count = 0
    import pdb; pdb.set_trace()
    for x in input:
        x = int(x)
        if prev is not None:
            if x > prev:
                inc_count = inc_count + 1
        prev = x
    return inc_count

def main_b(input):
    prevsum = None
    inc_count = 0
    import pdb; pdb.set_trace()
    # cast each line in the file to an int, store in list
    list_x = list(map(lambda x: int(x), input))


    # 1 2 3 4 5
    # (1, 2, 3) (2, 3, 4) (3, 4, 5)
    # N = 5, i [0, 4]
    # i in range 0, 2
    for i in range(0, len(list_x) - 2):
        cursum = list_x[i] + list_x[i+1] + list_x[i+2]
        if prevsum is not None:
            if cursum > prevsum:
                inc_count = inc_count + 1
        prevsum = cursum
    return inc_count

import sys

with open(sys.argv[1]) as input:
    print("B: "+str(main_b(input)))
    print(f"A: {main_a(input)}")

