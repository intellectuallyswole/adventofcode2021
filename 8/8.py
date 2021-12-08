
mapletters = {
    'abcefg': 0, 'cf': 1, 'acdeg': 2, 'acdfg': 3, 'bcdf': 4,
    'abdfg': 5, 'abdefg': 6, 'acf': 7, 'abcdefg': 8, 'abcdfg': 9
}

def maina():
    with open('input.txt') as f:
        cnt = 0
        vls = [2, 3,4,7]
        for ln in f:
            out_vals = ln.split('|')[1].strip("\n").split(" ")
            print(f"Out vals: {out_vals}")
            for word in out_vals:
                if len(word) in vls:
                    cnt += 1
        print(f"Count: {cnt}")

def strip(haystack, needle):
    for c in needle:
        haystack = haystack.replace(c, "")
    return haystack

def main():
    partial_sum = 0
    with open('input.txt') as f:
        for ln in f:
            val = guess_ln(ln)
            print(f"Value: {val}")
            partial_sum += val
    print(f"Final sum: {partial_sum}")

from typing import Dict, List
def decodedigit(digitword: str, c_map: Dict) -> int:
    decodedword = ""
    for c in digitword:
        decodedword += c_map[c]
    print(f"Decoding {digitword} to {decodedword} using {c_map}")
    decodedword = ''.join(sorted(decodedword))
    print(f"Sorted: {decodedword}")
    return mapletters[decodedword]

def decodenumeral(digits: List[str], c_map: Dict) -> int:
    numstr = ""
    print(f"Decoding numeral {digits}...")
    for digitword in digits:
        numstr += str(decodedigit(digitword, c_map))
    return int(numstr)


def guess_ln(ln) -> int:
    # map from observed segment to the segment it maps to, if everything is correct
    c_map = {'a': None, 'b': None, 'c': None, 'd': None, 'e': None, 'f': None, 'g': None}
    obs_vals, out_vals = ln.strip("\n").split('|')
    print(f"Obs vals {obs_vals}. Out vals: {out_vals}")
    obs_vals = set(obs_vals.split(" "))
    out_vals = out_vals.split(" ")
    out_vals = list(filter(lambda x: len(x) > 0, out_vals))
    zero = None
    one = [x for x in obs_vals if len(x) == 2][0]
    two = None
    three = None
    four = [x for x in obs_vals if len(x) == 4][0]
    five = None
    six = None
    seven = [x for x in obs_vals if len(x) == 3][0]
    eight = [x for x in obs_vals if len(x) == 7][0]
    nine = None

    assert len(one) == 2
    assert len(seven) == 3
    assert len(eight) == 7
    assert len(four) == 4

    for c in seven:
        if c not in one:
            c_map[c] = 'a'
        # else: the other letters map to c and f

    bd = strip(four, one)
    print(f"Four: {four}. One: {one}. bd: {bd}")
    assert len(bd) == 2

    twothreefive = list(filter(lambda x: len(x) == 5, obs_vals))
    assert len(twothreefive) == 3
    for word in twothreefive:
        if len(strip(word, one)) == 3:
            three = word
        elif len(strip(word, bd)) == 3:
            five = word
        else:
            two = word
    assert three is not None
    assert five is not None
    assert two is not None
    zero69  = list(filter(lambda x: len(x) == 6, obs_vals))
    assert len(zero69) == 3
    for word in zero69:
        if len(strip(word, one)) == 5:
            six = word
        elif len(strip(word, bd)) == 4:
            nine = word
        else:
            zero = word
    assert six is not None
    assert nine is not None
    assert zero is not None
    c_map[strip(eight, zero)] = 'd'
    for c in 'abcdefg':
        if c in two and not c in three:
            c_map[c] = 'e'
        elif c in three and not  c in two:
            c_map[c] = 'f'

        if c in five and  not c in three:
            c_map[c] = 'b'
        elif c in three and not c in five:
            c_map[c] = 'c'

    # need g
    c_map[strip(three, four+seven)] = 'g'
    print(f"C Map: {c_map}")

    assert 7 == len(c_map.keys())
    assert len(set(c_map.values())) == len(c_map.keys())

    val = decodenumeral(out_vals, c_map)
    return val


# 5 segs: 2 3 5
# 6 segs: 0 6 9

"""
  0:      1:      2:      3:      4:
 aaaa    ....    aaaa    aaaa    ....
b    c  .    c  .    c  .    c  b    c
b    c  .    c  .    c  .    c  b    c
 ....    ....    dddd    dddd    dddd
e    f  .    f  e    .  .    f  .    f
e    f  .    f  e    .  .    f  .    f
 gggg    ....    gggg    gggg    ....

  5:      6:      7:      8:      9:
 aaaa    aaaa    aaaa    aaaa    aaaa
b    .  b    .  .    c  b    c  b    c
b    .  b    .  .    c  b    c  b    c
 dddd    dddd    ....    dddd    dddd
.    f  e    f  .    f  e    f  .    f
.    f  e    f  .    f  e    f  .    f
 gggg    gggg    ....    gggg    gggg

"""

if __name__ == "__main__":
    main()
