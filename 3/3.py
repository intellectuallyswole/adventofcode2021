
def most_common_bits(lns):
    ones_ct = [0]*ln_len
    for ln in lns:
        for i in range(len(ln)):
            ones_ct[i] += int(ln[i])
    return ones_ct

def main_a():
    ln_len = 12
    num_lines = 0
    ones_ct = []
    with open('input.txt') as inputf:
        for ln in inputf:
            num_lines += 1
            ln = ln.strip("\n")
            if num_lines == 1:
                if len(ln) != ln_len:
                    ln_len = len(ln)
                    print(f"Setting line length to {len(ln)}")
                ones_ct = [0]*ln_len
            for i in range(len(ln)):
                ones_ct[i] += int(ln[i])
        gamma_str = ""
        mid_lvl = num_lines // 2
        print(f"Ones: {ones_ct}. Lines: {num_lines}")
        for i in range(len(ones_ct)):
            gamma_str += "1" if ones_ct[i] > mid_lvl else "0"

        gamma = int(gamma_str, base=2)
        epsilon = 2**ln_len - 1 - gamma
        print(f"G: {gamma}. E: {epsilon}. Power: {gamma*epsilon}")

def mcb_at_ind(lns, i):
    ones_ct = 0
    num_lines = 0
    for ln in lns:
        num_lines += 1
        ones_ct += int(ln[i])
    return 1 if ones_ct >= num_lines //2 else 0



def main_b():
    ln_len = 12
    ones_ct = [0]*ln_len
    num_lines = 0
    with open('input.txt') as inputf:
        lns = inputf.readlines()
        for i in range(ln_len):
            mcb = mcb_at_ind(i)
            lns = filter(...)
            if len(lns) == 1:
                return lns[0]




if __name__ == "__main__":
    main_b()
