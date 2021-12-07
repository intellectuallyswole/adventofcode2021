
import multiprocessing as mp

def processfish(fish):
    if fish == 0:
        return (6, 8)
    else:
        return (fish - 1)

def processfishies(fisharr):
    # return map(lambda fish: processfish(fish), fishies)
    fisharr = list(map(lambda x: int(x)-1, fisharr))
    newfish = fisharr.count(-1)
    fisharr.extend([8]*newfish)
    fisharr = list(map(lambda x: 6 if x==-1 else x, fisharr))
    return fisharr



if __name__ == "__main__":
    cc = mp.cpu_count()
    print(f"CPU count: {mp.cpu_count()}")
    with mp.Pool(processes==cc) as pool:
        fisharr = []
        steps = 80
        with open('input.txt') as inputf:
            for ln in inputf.readlines():
                fisharr += ln.split(",")
        # TEMP
        # fisharr = fisharr[:10]
        # ENDTEMP
        print(f"Initial size: {len(list(fisharr))}")

        for i in range(steps):
             fisharr=processfishies(fisharr)
             if steps % 10 == 0:
                 print(f"Num fishies after {i} steps: {len(list(fisharr))}")
             # processfishies(fisharr)
        print(f"Num fishies after {steps} steps: {len(list(fisharr))}")

