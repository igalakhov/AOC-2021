from lib import *


# REMEMBER
# REPLACE \n with '' if needed

# s -> raw input
# ints -> integers
# intsf -> integers, custom split
# lines -> raw lines
# pats -> split by pattern like {}{N}{W}
# pats2 -> split by pattern like IWIWI (double split)
# su1() -> submit part 1
# su2() -> submit part 2
def solve(s, ints, intsf, lines, pats, pats2, su1, su2):
    ii = intsf(",")

    s = [(i, i) for i in ii[:]]

    for d in range(80):
        nl = []
        # print(d, s)
        for c, i in s:
            if c == 0:
                nl.append((6, 6))
                nl.append((8, 8))
            else:
                nl.append((c-1, i))
        s = nl

    su1(len(s))

    cnt = Counter()
    for i in ii:
        cnt[i] += 1

    for d in range(256):
        nc = Counter()

        for i, fq in cnt.items():
            if i == 0:
                nc[6] += fq
                nc[8] += fq
            else:
                nc[i-1] += fq

        cnt = nc

    su2(sum(j for j in cnt.values()))

if __name__ == '__main__':
    setup_solve(solve, 6, year=2021)
