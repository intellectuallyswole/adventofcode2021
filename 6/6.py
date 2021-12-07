from typing import List
import multiprocessing as mp
from functools import cache, partial, reduce

@cache
def processfishsteps(fish: int, steps: int) -> int:
    if steps <= 0:
        return 1
    else:
        ret = processfishwork(fish)
        processrec = partial(processfishsteps, steps=steps-1)
        for fishi in ret:
            return reduce(lambda x, y: x+y,  map(processrec, ret), 0)
            return processfishsteps(fishi, steps - 1)

@cache
def processfishwork(fish: int) -> List[int]:
    if fish == 0:
        return [6, 8]
    else:
        return [fish - 1]

# Unused
# Takes a fish array
def processfishies(fisharr):
    # return map(lambda fish: processfish(fish), fishies)
    fisharr = list(map(lambda x: x-1, fisharr))
    newfish = fisharr.count(-1)
    fisharr.extend([8]*newfish)
    fisharr = list(map(lambda x: 6 if x==-1 else x, fisharr))
    return fisharr




if __name__ == "__main__":
    import pymp
    cc = mp.cpu_count()
    print(f"CPU count: {mp.cpu_count()}")
    fisharr = []
    # steps = 10
    steps = 256
    with open('6/input.txt') as inputf:
        for ln in inputf.readlines():
            fisharr += ln.split(",")
    fisharr = list(map(lambda x: int(x), fisharr))
    # TEMP
    # fisharr = fisharr[:10]
    # ENDTEMP
    print(f"Initial size: {len(list(fisharr))}")

    sum_arr = pymp.shared.array(cc, dtype='uint8')
    with pymp.Parallel(cc) as p:
        fr = p.thread_num * len(fisharr)//cc
        to = (p.thread_num +1)* len(fisharr)//cc
        subarray = fisharr[fr:to]
        partial_sum = 0
        p.print(f"[{p.thread_num}] Subarray: {fr}-{to}")
        for i in range(len(subarray)):
            # ret = len(processfish(subarray[i], steps))
            ret = processfishsteps(subarray[i], steps)
            p.print(f"Partial sum at {i}: {ret}")
            partial_sum += ret
        p.print(f"[{p.thread_num}]: Done. Final sum: {partial_sum}")
        sum_arr[p.thread_num] = partial_sum
    print(f"Num fishies after {steps} steps: {sum_arr.sum()}")


